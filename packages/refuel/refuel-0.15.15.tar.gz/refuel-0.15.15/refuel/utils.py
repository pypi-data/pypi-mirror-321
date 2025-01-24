import json
import uuid
from functools import wraps
from typing import Dict, List, Optional

from loguru import logger

from refuel.types import FilterType, FilterValueType, OrderByDirectionType

REFUEL_DATE_FORMAT = "%Y-%m-%d"

VALID_FILTER_OPERATORS = {
    ">",
    "<=",
    "=",
    "<",
    "IS NOT NULL",
    "IS NULL",
    "<>",
    ">=",
    "ILIKE",
    "NOT ILIKE",
    "NOT LIKE",
    "LIKE",
    "SIMILAR",
}

VALID_LLM_MODELS = {
    "GPT-4 Turbo": "gpt-4-1106-preview",
    "GPT-4o": "gpt-4o",
    "GPT-4o Mini": "gpt-4o-mini",
    "GPT-4": "gpt4",
    "GPT-3.5 Turbo": "gpt-3.5-turbo",
    "Claude 3.5 (Sonnet)": "claude-3-5-sonnet-20240620",
    "Claude 3 (Opus)": "claude-3-opus-20240229",
    "Claude 3 (Haiku)": "claude-3-haiku-20240307",
    "Gemini 1.5 (Pro)": "gemini-1.5-pro-preview-0409",
    "Mistral Small": "mistral-small-latest",
    "Mistral Large": "mistral-large-latest",
    "Refuel LLM-2": "refuel-llm-2-large",
    "Refuel LLM-2-small": "refuel-llm-2-small",
}

ENRICHMENT_TYPES = ["webpage_transform", "webpage_scrape", "web_search"]
TASK_TYPES = ["classification", "multilabel_classification", "attribute_extraction"]


def infer_filter_type(filter: Dict) -> FilterType:
    field = filter.get("field")
    operator = filter.get("operator")
    if operator == "SIMILAR":
        return FilterType.SIMILAR
    if field in ["llm_label", "confidence", "expected_label"]:
        return FilterType.LABEL
    return FilterType.METADATA


def format_filters(
    filters: List[Dict],
    dataset_dict: Dict,
    task_dict: Optional[Dict] = None,
) -> List[str]:
    formatted_filters = []
    for f in filters:
        field = f.get("field")
        operator = f.get("operator")
        value = f.get("value", "")

        if not operator or operator not in VALID_FILTER_OPERATORS:
            logger.error(f"Error: invalid filter operator\nfilter = {f}")
            continue

        subtask = f.get("subtask", None)
        subtask_id = None
        if subtask:
            if not task_dict:
                logger.error(
                    f"Error: filtering with subtask, but task is not provided!. Filter: {f} will be ignored.",
                )
                continue
            subtasks = task_dict.get("subtasks", [])
            for subtask_dict in subtasks:
                if subtask_dict.get("name") == subtask:
                    subtask_id = subtask_dict.get("id")
            if not subtask_id:
                logger.error(
                    f"Error: Subtask does not exist!\nsubtask = {subtask}. Filter: {f} will be ignored.",
                )
                continue

        filter_type = infer_filter_type(f)
        if filter_type == FilterType.SIMILAR:
            f_formatted = {
                "filter_type": filter_type,
                "operator": operator,
                # This is not a bug
                "field": value,
            }
        elif filter_type == FilterType.LABEL:
            dataset_schema = dataset_dict.get("dataset_schema", {})
            dataset_columns = dataset_schema.keys()
            if value in dataset_columns:
                value_type = FilterValueType.METADATA
            else:
                value_type = FilterValueType.CONST
            f_formatted = {
                "filter_type": filter_type,
                "field": field,
                "operator": operator,
                "value": value,
                "subtask_id": subtask_id,
                "value_type": value_type,
            }
        else:
            f_formatted = {
                "filter_type": filter_type,
                "field": field,
                "operator": operator,
                "value": value,
            }
        formatted_filters.append(json.dumps(f_formatted))
    return formatted_filters


def format_order_by(
    order_by: List[Dict],
    task_dict: Optional[Dict] = None,
) -> List[str]:
    formatted_order_by = []
    for o in order_by:
        field = o.get("field")
        if not field:
            logger.error(
                f"Error: order_by: {o} is missing a required parameter 'field'. \n Expected format: {{'field': 'field_name', 'direction': 'ASC/DESC', 'subtask' (optional): 'subtask_name'}}",
            )
            continue
        direction = o.get("direction", OrderByDirectionType.ASC)
        subtask = o.get("subtask", None)
        subtask_id = None
        if subtask:
            if not task_dict:
                logger.error(
                    f"Error: sorting with subtask, but task is not provided!. Sort: {o} will be ignored.",
                )
                continue
            subtasks = task_dict.get("subtasks", [])
            for subtask_dict in subtasks:
                if subtask_dict.get("name") == subtask:
                    subtask_id = subtask_dict.get("id")
            if not subtask_id:
                logger.error(
                    f"Error: Subtask does not exist!\nsubtask = {subtask}. Sort: {o} will be ignored.",
                )
                continue
        o_formatted = {
            "field": field,
            "direction": direction,
            "subtask_id": subtask_id,
        }
        formatted_order_by.append(json.dumps(o_formatted))
    return formatted_order_by


def is_valid_uuid(input: str) -> bool:
    if not input:
        return False
    try:
        uuid.UUID(input, version=4)
        return True
    except ValueError:
        return False


def ensure_project(func) -> None:
    # decorator to check if project id is set
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self._project_id:
            application = (
                kwargs.get("application") if kwargs else args[0] if args else None
            )
            if not application:
                logger.error(
                    "Please set a project for the client session: client.set_project(project_name)",
                )
                return []
            if (
                application not in self.catalog_applications
                and application not in self.catalog_applications.values()
            ):
                logger.error(
                    f"Application {application} not found in catalog applications. If "
                    "you are trying to label an application in a project, please set "
                    "project for the client session: client.set_project(project_name)",
                )
                return []
        return func(self, *args, **kwargs)

    return wrapper


class RefuelException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        self.error_message = f"Request failed with status code: {self.status_code}, response: {self.message}"
        super().__init__(self.error_message)


class RetryableRefuelException(RefuelException):
    def __init__(self, status_code, message):
        super().__init__(status_code, message)
