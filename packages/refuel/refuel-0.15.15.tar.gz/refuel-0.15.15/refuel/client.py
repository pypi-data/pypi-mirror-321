import concurrent.futures as pyfutures
import copy
import os
from concurrent.futures import as_completed
from datetime import datetime, timezone
from functools import lru_cache
from http import HTTPStatus
from time import sleep
from typing import Dict, List, Optional

import pandas as pd
from loguru import logger
from requests_futures.sessions import FuturesSession
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from refuel.constants import APP_CATALOG_PROJECT_ID, CONTACT_SUPPORT_MESSAGE
from refuel.types import TaskType
from refuel.utils import (
    ENRICHMENT_TYPES,
    TASK_TYPES,
    VALID_LLM_MODELS,
    RefuelException,
    RetryableRefuelException,
    ensure_project,
    format_filters,
    format_order_by,
    is_valid_uuid,
)


class RefuelClient:
    # Default config settings
    API_BASE_URL = "https://cloud-api.refuel.ai"
    API_KEY_ENV_VARIABLE = "REFUEL_API_KEY"
    TIMEOUT_SECS = 60
    DEFAULT_MAX_QUERY_ITEMS = 1000
    QUERY_STEP_SIZE = 100
    MAX_WORKERS = os.cpu_count()
    MAX_RETRIES = 3

    def __init__(
        self,
        api_key: str = None,
        api_base_url: str = API_BASE_URL,
        timeout: int = TIMEOUT_SECS,
        max_retries: int = MAX_RETRIES,
        max_workers: int = MAX_WORKERS,
        project: Optional[str] = None,
    ) -> None:
        """
        Args:
            api_key (str, optional): Refuel API Key. Defaults to None.
            api_base_url (str, optional): Base URL of the Refuel API endpoints. Defaults to API_BASE_URL.
            timeout (int, optional): Timeout (secs) for a given API call. Defaults to TIMEOUT_SECS.
            max_retries (int, optional): Max num retries. Defaults to MAX_RETRIES.
            max_workers (int, optional): Max number of concurrent tasks in the ThreadPoolExecutor
            project (str, optional): Name or ID of the Project you plan to use.

        """
        # initialize variables
        self._api_key = api_key or os.environ.get(self.API_KEY_ENV_VARIABLE)
        self._api_base_url = api_base_url
        self._timeout = timeout
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._api_key}",
        }
        # initialize request session
        adapter_kwargs = {"max_retries": max_retries}
        self._session = FuturesSession(
            max_workers=max_workers,
            adapter_kwargs=adapter_kwargs,
        )
        self.catalog_applications = self.get_catalog_applications()
        if project:
            self.set_project(project)
        else:
            self._project_id = None

    def set_project(self, project: str) -> None:
        """
        Set the project to be used for subsequent API calls.

        Args:
            project (str): Name or ID of the Project you plan to use.

        """
        self._project_id = self._get_project_id(project)

    def _async_get(
        self,
        url: str,
        params: Dict = None,
        headers: Dict = None,
    ) -> pyfutures.Future:
        return self._session.get(
            url,
            headers=headers,
            params=params,
            timeout=self._timeout,
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        before_sleep=before_sleep_log(logger, "WARNING"),
        retry=retry_if_exception_type(RetryableRefuelException),
    )
    def _get(self, url: str, params: Dict = None, headers: Dict = None) -> Dict:
        response = self._session.get(
            url,
            headers=headers,
            params=params,
            timeout=self._timeout,
        ).result()
        try:
            if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
                raise RetryableRefuelException(response.status_code, response.text)
            response.raise_for_status()
        except Exception as err:
            raise RefuelException(response.status_code, response.text) from err

        if response.status_code == HTTPStatus.OK:
            return response.json()
        return response

    def _async_post(
        self,
        url: str,
        data: str = None,
        params: Dict = None,
        json: Dict = None,
        files: List = None,
        headers: Dict = None,
    ) -> pyfutures.Future:
        return self._session.post(
            url,
            headers=headers,
            timeout=self._timeout,
            data=data,
            params=params,
            json=json,
            files=files,
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        before_sleep=before_sleep_log(logger, "WARNING"),
        retry=retry_if_exception_type(RetryableRefuelException),
    )
    def _post(
        self,
        url: str,
        data: str = None,
        params: Dict = None,
        json: Dict = None,
        files: List = None,
        headers: Dict = None,
    ) -> Dict:
        response = self._session.post(
            url,
            headers=headers,
            timeout=self._timeout,
            data=data,
            params=params,
            json=json,
            files=files,
        ).result()
        try:
            if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
                raise RetryableRefuelException(response.status_code, response.text)
            response.raise_for_status()
        except Exception as err:
            raise RefuelException(response.status_code, response.text) from err

        if response.status_code in [
            HTTPStatus.OK,
            HTTPStatus.CREATED,
            HTTPStatus.ACCEPTED,
        ]:
            return response.json()
        return response

    def _async_patch(
        self,
        url: str,
        data: str = None,
        params: Dict = None,
        json: Dict = None,
        headers: Dict = None,
    ) -> pyfutures.Future:
        return self._session.patch(
            url,
            data=data,
            params=params,
            json=json,
            headers=headers,
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        before_sleep=before_sleep_log(logger, "WARNING"),
        retry=retry_if_exception_type(RetryableRefuelException),
    )
    def _patch(
        self,
        url: str,
        data: str = None,
        params: Dict = None,
        json: Dict = None,
        headers: Dict = None,
    ) -> Dict:
        response = self._session.patch(
            url,
            data=data,
            params=params,
            json=json,
            headers=headers,
        ).result()
        try:
            if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
                raise RetryableRefuelException(response.status_code, response.text)
            response.raise_for_status()
        except Exception as err:
            raise RefuelException(response.status_code, response.text) from err

        if response.status_code == HTTPStatus.OK:
            return response.json()
        return response

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        before_sleep=before_sleep_log(logger, "WARNING"),
        retry=retry_if_exception_type(RetryableRefuelException),
    )
    def _delete(
        self,
        url: str,
        params: Dict = None,
        headers: Dict = None,
    ) -> Dict:
        response = self._session.delete(url, headers=headers, params=params).result()
        try:
            if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
                raise RetryableRefuelException(response.status_code, response.text)
            response.raise_for_status()
        except Exception as err:
            raise RefuelException(response.status_code, response.text) from err

        if response.status_code == HTTPStatus.OK:
            return response.json()
        return response

    def _item_count_helper(self, url: str, params: Dict = None) -> int:
        # construct parallel requests
        request_params = copy.deepcopy(params)
        request_params["offset"] = 0
        request_params["max_items"] = 0

        response = self._get(url=url, params=request_params, headers=self._headers)

        dataset_size = response.get("data", {}).get("total_count")
        return dataset_size or self.DEFAULT_MAX_QUERY_ITEMS

    def _label_parse_helper(self, labels: List[Dict], task_config: Dict) -> Dict:
        task_name = task_config["task_name"]
        subtask_id_to_name_and_type = {}
        for subtasks in task_config["subtasks"]:
            subtask_type = subtasks.get("type")
            subtask_name = subtasks.get("name")
            subtask_id = subtasks.get("id")
            if subtask_id and subtask_name:
                subtask_id_to_name_and_type[subtask_id] = (subtask_name, subtask_type)

        parsed_output = {}
        for label in labels:
            # Each label is a dictionary containing the labels for a subtask (output field)
            subtask_id = label.get("id", "")
            subtask_name, subtask_type = subtask_id_to_name_and_type.get(subtask_id)
            if not subtask_name:
                continue
            parsed_output[f"{task_name}_{subtask_name}_llm_label"] = label.get(
                "llm_label",
                None,
            )
            parsed_output[f"{task_name}_{subtask_name}_confidence"] = label.get(
                "confidence",
                None,
            )
            if subtask_type == TaskType.MULTILABEL_CLASSIFICATION:
                parsed_output[
                    f"{task_name}_{subtask_name}_multilabel_confidence"
                ] = label.get("multilabel_confidence", None)
            parsed_output[f"{task_name}_{subtask_name}_label"] = label.get(
                "label",
                None,
            )
        return parsed_output

    def _query_helper(
        self,
        url: str,
        params: Optional[Dict] = None,
        verbose: Optional[bool] = False,
        task_dict: Optional[Dict] = None,
    ) -> pd.DataFrame:
        dataset_size = self._item_count_helper(url, params)
        max_items = min(
            params.get("max_items", self.DEFAULT_MAX_QUERY_ITEMS),
            dataset_size,
        )
        offset = params.get("offset", 0)

        # construct parallel requests
        logger.info(f"Started fetching data. Will fetch {max_items} items ...")
        futures = []
        offset_starts = list(
            range(offset, offset + max_items, RefuelClient.QUERY_STEP_SIZE),
        )
        items_remaining = max_items

        for batch_num, offset_start in enumerate(offset_starts):
            num_to_fetch = min(items_remaining, RefuelClient.QUERY_STEP_SIZE)
            request_params = copy.deepcopy(params)
            request_params["offset"] = offset_start
            request_params["max_items"] = num_to_fetch
            future_obj = self._async_get(
                url=url,
                params=request_params,
                headers=self._headers,
            )
            future_obj.batch_num = batch_num
            futures.append(future_obj)
            items_remaining -= num_to_fetch

        # parse response from each request
        batch_idx_to_items = {}
        num_fetched = 0
        for future in as_completed(futures):
            response = future.result()
            if response.status_code != 200:
                logger.error(
                    "Request failed with status code: {} received with response: {}",
                    response.status_code,
                    response.text,
                )
            else:
                json_response = response.json()
                result = json_response.get("data", [])
                items = result.get("items", [])
                batch_idx_to_items[future.batch_num] = items
                num_fetched += len(items)
                if verbose:
                    logger.info(f"Fetched {num_fetched} items so far.")

        sorted_by_batch_idx = [item[1] for item in sorted(batch_idx_to_items.items())]
        items = [item for sublist in sorted_by_batch_idx for item in sublist]
        if task_dict:
            final_items = []
            for item in items:
                dataset_cols = item["fields"]
                label_cols = self._label_parse_helper(item["labels"], task_dict)
                final_item = {**dataset_cols, **label_cols}
                final_items.append(final_item)
            items = final_items
        logger.info(f"Completed fetching data. {len(items)} items were fetched.")
        return pd.DataFrame.from_records(items)

    def _get_dataset_id(self, dataset: str) -> str:
        if is_valid_uuid(dataset):
            return dataset
        for ds in self.get_datasets():
            if ds.get("dataset_name") == dataset:
                return ds.get("id")
        raise RefuelException(
            HTTPStatus.NOT_FOUND,
            f"No dataset with name={dataset} found.",
        )

    def _get_project_id(self, project: str) -> str:
        if is_valid_uuid(project):
            return project
        for p in self.get_projects():
            if p.get("project_name") == project:
                return p.get("id")

        raise RefuelException(
            HTTPStatus.NOT_FOUND,
            f"No project with name={project} found.",
        )

    def _get_task_id(self, task: str) -> str:
        if is_valid_uuid(task):
            return task
        for t in self.get_tasks():
            if t.get("task_name") == task:
                return t.get("id")
        raise RefuelException(HTTPStatus.NOT_FOUND, f"No task with name={task} found.")

    def _get_catalog_app_id(self, catalog_app: str) -> str:
        if is_valid_uuid(catalog_app):
            return catalog_app
        for app in self.get_catalog_apps():
            if app.get("app_name") == catalog_app:
                return app.get("id")
        raise RefuelException(
            HTTPStatus.NOT_FOUND,
            f"No catalog app with name={catalog_app} found.",
        )

    def _get_application_id(self, application: str) -> str:
        if (
            is_valid_uuid(application)
            or application in self.catalog_applications.values()
        ):
            return application
        if application in self.catalog_applications:
            return self.catalog_applications[application]
        for app in self.get_applications():
            if app.get("name") == application:
                return app.get("id")
        raise RefuelException(
            HTTPStatus.NOT_FOUND,
            f"No application with name={application} found.",
        )

    # Datasets
    @ensure_project
    def get_datasets(self) -> List:
        response = self._get(
            url=self._api_base_url + "/datasets",
            params={"project_id": self._project_id},
            headers=self._headers,
        )
        datasets = response.get("data", [])
        return list(
            map(
                lambda ds: {
                    "id": ds.get("id"),
                    "dataset_name": ds.get("dataset_name"),
                    "created_at": ds.get("created_at"),
                    "status": ds.get("ingest_status"),
                    "dataset_schema": ds.get("dataset_schema", {}).get(
                        "properties",
                        {},
                    ),
                    "source": ds.get("source"),
                },
                datasets,
            ),
        )

    @ensure_project
    def get_dataset(self, dataset: str) -> Dict:
        dataset_id = self._get_dataset_id(dataset)
        if not dataset_id:
            raise RefuelException(
                HTTPStatus.NOT_FOUND,
                f"Dataset with name={dataset} not found.",
            )

        response = self._get(
            url=self._api_base_url + f"/datasets/{dataset_id}",
            headers=self._headers,
        )

        ds = response.get("data", {})
        return {
            "id": ds.get("id"),
            "dataset_name": ds.get("name"),
            "created_at": ds.get("created_at"),
            "status": ds.get("ingest_status"),
            "dataset_schema": ds.get("schema", {}).get("properties", {}),
            "source": ds.get("source"),
        }

    def wait_for_dataset_upload(
        self,
        dataset: str,
        wait_time: int = 30,
        timeout: int = 15 * 60,
    ) -> Dict:
        """
        Waits for a dataset to finish uploading. Returns the dataset object if successful, None otherwise.

        Args:
            dataset (str): Name or ID of the dataset
            wait_time (int, optional): How often to check the dataset status (in seconds). Defaults to 30.
            timeout (int, optional): How long to wait for the dataset to finish uploading (in seconds). Defaults to 15*60.

        Returns:
            Dict: Dataset object

        """
        dataset_id = self._get_dataset_id(dataset)
        sleep(wait_time)
        start_time = datetime.now()
        while True:
            dataset = self.get_dataset(dataset_id)
            if dataset["status"] == "success":
                return dataset
            if dataset["status"] == "failed":
                raise RefuelException(
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                    f"Dataset ingestion failed. {CONTACT_SUPPORT_MESSAGE}",
                )
            if (datetime.now() - start_time).seconds > timeout:
                raise RefuelException(
                    HTTPStatus.REQUEST_TIMEOUT,
                    f"Dataset ingestion is taking longer than expected. {CONTACT_SUPPORT_MESSAGE}",
                )
            logger.info(
                f"Dataset status is {dataset['status']}. Waiting {wait_time} seconds before checking again.",
            )
            sleep(wait_time)

    @ensure_project
    def upload_dataset(
        self,
        file_path: str,
        dataset_name: str,
        source: str = "file",
        wait_for_completion: bool = False,
    ) -> Dict:
        response = {}
        if source == "file":
            with open(file_path, "rb") as f:
                response = self._post(
                    url=self._api_base_url + f"/projects/{self._project_id}/datasets",
                    headers={
                        "Authorization": f"Bearer {self._api_key}",
                    },
                    data={
                        "name": dataset_name,
                        "source": source,
                    },
                    files={"file": f},
                )
        elif source == "uri":
            response = self._post(
                url=self._api_base_url + f"/projects/{self._project_id}/datasets",
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                },
                data={
                    "name": dataset_name,
                    "source": source,
                    "source_path": file_path,
                },
            )
        else:
            raise RefuelException(
                HTTPStatus.BAD_REQUEST,
                "Invalid source. Must be one of ['local', 'uri']",
            )
        dataset_response = response.get("data", {})
        dataset_id = dataset_response.get("id")
        logger.info("Ingesting dataset into the platform. This may take a few minutes.")

        if wait_for_completion:
            dataset = self.wait_for_dataset_upload(dataset_id)
            return dataset

        return {
            "id": dataset_response.get("id"),
            "dataset_name": dataset_response.get("name"),
            "status": dataset_response.get("ingest_status"),
            "dataset_schema": dataset_response.get("schema", {}).get("properties", {}),
        }

    @ensure_project
    def download_dataset(
        self,
        email_address: str,
        dataset: str,
        task: Optional[str] = None,
    ) -> None:
        # Get dataset ID
        dataset_id = self._get_dataset_id(dataset)

        params = {"dataset_id": dataset_id, "email_address": email_address}

        # Get task ID if specified
        if task:
            task_id = self._get_task_id(task)
            params["task_id"] = task_id
            params["include_labels"] = True

        path = self._api_base_url + f"/datasets/{dataset_id}/exports"
        response = self._post(
            url=path,
            params=params,
            headers=self._headers,
        )
        logger.info(
            "Dataset will be downloaded shortly. A link will also be sent to your email address.",
        )
        export_id = response.get("data", {}).get("export_id")
        while True:
            export_status = self._session.get(
                url=f"{path}/{export_id}",
                headers=self._headers,
                timeout=self._timeout,
            ).result()

            if export_status.status_code == HTTPStatus.OK:
                dataset_url = export_status.json().get("data", {})
                # download dataset file
                response = self._session.get(
                    url=dataset_url,
                    allow_redirects=True,
                ).result()
                if response.status_code != HTTPStatus.OK:
                    logger.error("Failed to download dataset")
                    break
                file_name = self.get_dataset(dataset)["dataset_name"] + ".csv"
                with open(file_name, "wb") as f:
                    f.write(response.content)

                logger.info(f"Dataset has been downloaded to {file_name}")
                break
            if export_status.status_code == HTTPStatus.NOT_FOUND:
                sleep(30)
            else:
                logger.error("Failed to download dataset")
                break

    def delete_dataset(self, dataset: str) -> None:
        dataset_id = self._get_dataset_id(dataset)
        response = self._delete(
            url=self._api_base_url + f"/datasets/{dataset_id}",
            headers=self._headers,
        )
        logger.info("Dataset was successfully deleted.")

    @ensure_project
    def add_items(
        self,
        dataset: str,
        items: List[Dict],
    ):
        dataset_id = self._get_dataset_id(dataset)
        response = self._post(
            url=self._api_base_url + f"/datasets/{dataset_id}/items",
            json=items,
            headers=self._headers,
        )
        return response.get("data", {})

    @ensure_project
    def get_items(
        self,
        dataset: str,
        offset: int = 0,
        max_items: int = 20,
        filters: List[Dict] = [],
        order_by: List[Dict] = [],
        task: Optional[str] = None,
    ) -> pd.DataFrame:
        dataset_id = self._get_dataset_id(dataset)
        task_dict = self.get_task(task) if task else None
        dataset_dict = self.get_dataset(dataset)
        params = {
            "dataset_id": dataset_id,
            "offset": offset,
            "max_items": max_items,
            "filters": format_filters(filters, dataset_dict, task_dict),
            "order_bys": format_order_by(order_by, task_dict),
            "expand": "true",
        }

        # Get task details if specified
        if task:
            task_id = task_dict.get("id")
            params["task_id"] = task_id
            return self._query_helper(
                self._api_base_url + f"/tasks/{task_id}/datasets/{dataset_id}",
                params=params,
                task_dict=task_dict,
            )
        return self._query_helper(
            self._api_base_url + f"/datasets/{dataset_id}",
            params=params,
        )

    # Projects
    def get_projects(self) -> List:
        response = self._get(
            url=self._api_base_url + "/projects",
            headers=self._headers,
        )
        return response.get("data", [])

    def get_project(self, project: str) -> Dict:
        project_id = self._get_project_id(project)
        if not project_id:
            logger.error("Must provide a valid project name or ID to get project")
            return {}
        response = self._get(
            url=self._api_base_url + f"/projects/{project_id}",
            headers=self._headers,
        )
        return response.get("data", {})

    def create_project(self, project: str, description: str) -> Dict:
        response = self._post(
            url=self._api_base_url + "/projects",
            params={"project_name": project, "description": description},
            headers=self._headers,
        )
        return response.get("data", {})

    # Tasks
    @ensure_project
    def get_tasks(self) -> List:
        response = self._get(
            url=self._api_base_url + f"/projects/{self._project_id}/tasks",
            params={"project_id": self._project_id},
            headers=self._headers,
        )

        tasks = response.get("data", [])
        return list(
            map(
                lambda task: {
                    "id": task.get("id"),
                    "task_name": task.get("task_name"),
                    "created_at": task.get("created_at"),
                    "status": task.get("status"),
                },
                tasks,
            ),
        )

    @ensure_project
    def get_catalog_apps(self) -> List:
        response = self._get(
            url=self._api_base_url + "/app_catalog",
            headers=self._headers,
        )

        apps = response.get("data", [])
        return list(
            map(
                lambda app: {
                    "id": app.get("id"),
                    "app_name": app.get("app_name"),
                    "description": app.get("description"),
                },
                apps,
            ),
        )

    @ensure_project
    def get_task(self, task: str) -> Dict:
        task_id = self._get_task_id(task)
        response = self._get(
            url=self._api_base_url + f"/tasks/{task_id}",
            headers=self._headers,
        )
        return response.get("data", {})

    def _validate_task_config(self, dataset_obj: Dict, fields: List[Dict]) -> bool:
        if not dataset_obj:
            logger.error("Cannot create task, must provide a valid dataset name or ID")
            return False
        dataset_schema = dataset_obj.get("dataset_schema", {})
        schema_columns = dataset_schema.keys()
        field_names = [field.get("name") for field in fields]
        if any(
            [
                not all(key in field for key in ["name", "type", "input_columns"])
                for field in fields
            ],
        ):
            logger.error(
                "Cannot create task, fields must have name, type and input_columns",
            )
            return False

        if len(field_names) != len(set(field_names)):
            logger.error("Cannot create task, field names must be unique")
            return False

        if any(field_name in schema_columns for field_name in field_names):
            logger.error(
                "Cannot create task, field names must be different from dataset column names",
            )
            return False

        for field in fields:
            input_columns = field.get("input_columns", [])
            if not all(
                (col in schema_columns or col in field_names)
                and col != field.get("name")
                for col in input_columns
            ):
                logger.error(
                    "Cannot create task, field input columns must be present in dataset schema columns or one of the other field names",
                )
                return False

        return True

    def _task_chain(self, fields: List[Dict]) -> List:
        subtasks = []
        for field in fields:
            attribute_name = field.get("name")
            attribute_guidelines = field.get("guidelines")
            input_columns = field.get("input_columns")
            task_type = field.get("type")
            default_value = field.get("fallback_value", "-")
            ground_truth_column = field.get("ground_truth_column")
            subtask = {
                "name": attribute_name,
                "type": task_type,
                "input_columns": input_columns,
                "guidelines": attribute_guidelines,
                "default_value": default_value,
                "label_column": ground_truth_column,
            }
            if task_type in [
                TaskType.CLASSIFICATION,
                TaskType.MULTILABEL_CLASSIFICATION,
            ]:
                labels = field.get("labels")
                subtask["labels"] = labels

            subtasks.append(subtask)
        return subtasks

    @ensure_project
    def create_task(
        self,
        task: str,
        dataset: str,
        context: str,
        fields: List[Dict],
        model: Optional[str] = None,
    ) -> Dict:
        # validate dataset
        dataset_obj = self.get_dataset(dataset)
        if not self._validate_task_config(dataset_obj, fields):
            return {}
        enrichments = list(filter(lambda x: x.get("type") in ENRICHMENT_TYPES, fields))
        fields = list(filter(lambda x: x.get("type") in TASK_TYPES, fields))

        subtasks = self._task_chain(fields)
        if model is not None and model not in VALID_LLM_MODELS:
            logger.error(
                f"Invalid model name: {model}. List of valid model names: {list(VALID_LLM_MODELS.keys())!s}",
            )
            return {}
        if model:
            model = VALID_LLM_MODELS[model]
        task_settings = {
            "context": context,
            "subtasks": subtasks,
            "dataset_id": dataset_obj.get("id"),
            "model": model,
            "task_type": TaskType.TASK_CHAIN,
        }
        if enrichments:
            task_settings["transforms"] = enrichments
        params = {"task_name": task}
        response = self._post(
            url=self._api_base_url + f"/projects/{self._project_id}/tasks",
            params=params,
            json=task_settings,
            headers=self._headers,
        )

        return response.get("data", {})

    @ensure_project
    def get_task_run(
        self,
        task: str,
        dataset: str,
    ) -> Dict:
        task_id = self._get_task_id(task)
        dataset_id = self._get_dataset_id(dataset)
        params = {"task_id": task_id, "dataset_id": dataset_id}
        task_run_response = self._get(
            url=self._api_base_url + f"/tasks/{task_id}/runs/{dataset_id}",
            params=params,
            headers=self._headers,
        )
        task_run_response = task_run_response.get("data", {})

        task_run_metrics_response = self._get(
            url=self._api_base_url + f"/tasks/{task_id}/runs/{dataset_id}/metrics",
            params=params,
            headers=self._headers,
        )
        task_run_metrics_response = task_run_metrics_response.get("data", {})
        task_run_metrics = task_run_metrics_response.get("task", [])
        task_run_response["metrics"] = task_run_metrics

        return task_run_response

    def wait_for_task_completion(
        self,
        task: str,
        dataset: str,
        wait_time: int = 30,
        timeout: int = 24 * 60 * 60,  # 1 day
    ) -> Dict:
        """
        Waits for a task to finish executing. Returns the task run object if successful, None otherwise.

        Args:
            task (str): Name or ID of the task
            dataset (str): Name or ID of the dataset
            wait_time (int, optional): How often to check the task run status (in seconds). Defaults to 30.
            timeout (int, optional): How long to wait for the task to finish execution (in seconds). Defaults to 1 day.

        Returns:
            Dict: Task Run object

        """
        sleep(wait_time)
        start_time = datetime.now()
        while True:
            task_run = self.get_task_run(task, dataset)
            if task_run["status"] in ["completed", "paused"]:
                return task_run
            if task_run["status"] == "failed":
                raise RefuelException(
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                    f"Task Run failed. {CONTACT_SUPPORT_MESSAGE}",
                )
            if task_run["status"] == "cancelled":
                raise RefuelException(
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                    f"Task Run has been cancelled. {CONTACT_SUPPORT_MESSAGE}",
                )
            if (datetime.now() - start_time).seconds > timeout:
                raise RefuelException(
                    HTTPStatus.REQUEST_TIMEOUT,
                    f"Task execution is taking longer than expected. {CONTACT_SUPPORT_MESSAGE}",
                )
            logger.info(
                f"Task is in {task_run['status']} state. Waiting {wait_time} seconds before checking again.",
            )
            sleep(wait_time)

    @ensure_project
    def start_task_run(
        self,
        task: str,
        dataset: str,
        num_items: Optional[int] = None,
        wait_for_completion: bool = False,
    ) -> Dict:
        task_id = self._get_task_id(task)
        dataset_id = self._get_dataset_id(dataset)
        params = {
            "task_id": task_id,
            "dataset_id": dataset_id,
        }
        if num_items:
            params["num_items"] = num_items
        logger.info(
            "The labeling task is being run on the dataset. You can monitor progress with get_task_run(task, dataset)",
        )
        response = self._post(
            url=self._api_base_url + f"/tasks/{task_id}/runs",
            params=params,
            headers=self._headers,
        )

        if wait_for_completion:
            response = self.wait_for_task_completion(task_id, dataset_id)
            return response

        return response

    @ensure_project
    def cancel_task_run(
        self,
        task: str,
        dataset: str,
    ) -> Dict:
        task_id = self._get_task_id(task)
        dataset_id = self._get_dataset_id(dataset)
        params = {"task_id": task_id, "dataset_id": dataset_id, "cancel_run": True}
        response = self._post(
            url=self._api_base_url + f"/tasks/{task_id}/runs",
            params=params,
            headers=self._headers,
        )
        return response

    @lru_cache
    @ensure_project
    def get_application(self, application: str) -> Dict:
        application_id = self._get_application_id(application)
        url = self._api_base_url + f"/applications/{application_id}"
        response = self._get(url=url, headers=self._headers)
        return response.get("data", {})

    @ensure_project
    def get_applications(self) -> List:
        response = self._get(
            url=self._api_base_url + f"/projects/{self._project_id}/applications",
            headers=self._headers,
        )
        applications = response.get("data", [])
        return list(
            map(
                lambda app: {
                    "id": app.get("id"),
                    "name": app.get("name"),
                    "created_at": app.get("created_at"),
                    "status": app.get("status"),
                },
                applications,
            ),
        )

    def get_catalog_applications(self) -> dict:
        response = self._get(
            url=self._api_base_url + f"/projects/{APP_CATALOG_PROJECT_ID}/applications",
            headers=self._headers,
        )
        applications = response.get("data", [])
        return {app.get("name"): app.get("id") for app in applications}

    @ensure_project
    def deploy_task(self, task: str):
        task_id = self._get_task_id(task)
        url = self._api_base_url + f"/projects/{self._project_id}/applications"
        response = self._post(
            url=url,
            params={"task_id": task_id, "application_name": task},
            headers=self._headers,
        )
        application_data = response.get("data", {})
        return {
            "id": application_data.get("id"),
            "name": application_data.get("name"),
            "created_at": application_data.get("created_at"),
            "status": application_data.get("status"),
        }

    @ensure_project
    def import_app(self, catalog_app: str) -> Dict:
        url = self._api_base_url + f"/projects/{self._project_id}/applications"
        catalog_app_id = self._get_catalog_app_id(catalog_app)
        params = {"catalog_id": catalog_app_id, "application_name": catalog_app}
        response = self._post(
            url=url,
            params=params,
            headers=self._headers,
        )
        application_data = response.get("data", {})
        return {
            "id": application_data.get("id"),
            "name": application_data.get("name"),
            "created_at": application_data.get("created_at"),
            "status": application_data.get("status"),
        }

    @ensure_project
    def label(
        self,
        application: str,
        inputs: List[Dict],
        explain: bool = False,
        explain_fields: List[str] = None,
        telemetry: bool = False,
        model_id: Optional[str] = None,
    ):
        application_id = self._get_application_id(application)
        url = self._api_base_url + f"/applications/{application_id}/label"
        futures = []
        idx_to_result = {}
        explain_fields_serialized = ";".join(explain_fields) if explain_fields else None
        if model_id and model_id in VALID_LLM_MODELS.keys():
            model_id = VALID_LLM_MODELS[model_id]

        try:
            for i, input in enumerate(inputs):
                future_obj = self._async_post(
                    url=url,
                    params={
                        "application_id": application_id,
                        "explain": explain,
                        "telemetry": telemetry,
                        "explain_fields": explain_fields_serialized,
                        "model_id": model_id,
                    },
                    json=[input],
                    headers=self._headers,
                )
                future_obj.index = i
                future_obj.retries = 0
                future_obj.input = input
                futures.append(future_obj)
            while futures:
                new_futures = []
                for future in as_completed(futures):
                    response = future.result()
                    if response.status_code != 200:
                        logger.error(
                            "Request failed with status code: {} received with response: {}. Retrying...",
                            response.status_code,
                            response.text,
                        )
                        if future.retries == self.MAX_RETRIES:
                            idx_to_result[future.index] = {
                                "refuel_output": [
                                    {
                                        "refuel_uuid": None,
                                        "refuel_fields": [],
                                        "refuel_api_timestamp": datetime.now(
                                            timezone.utc,
                                        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
                                    },
                                ],
                            }
                        else:
                            new_future = self._async_post(
                                url=url,
                                params={
                                    "application_id": application_id,
                                    "explain": explain,
                                    "telemetry": telemetry,
                                    "explain_fields": explain_fields_serialized,
                                },
                                json=[future.input],
                                headers=self._headers,
                            )
                            new_future.retries = future.retries + 1
                            new_future.index = future.index
                            new_future.input = future.input
                            new_futures.append(new_future)
                    else:
                        result = response.json().get("data", [])
                        idx_to_result[future.index] = result
                futures = new_futures
        except Exception:
            logger.error(
                "Error while labeling! Returning only successfully labeled inputs.",
            )

        full_labels = []
        for i in range(len(inputs)):
            full_labels += idx_to_result.get(i, {}).get(
                "refuel_output",
                [
                    {
                        "refuel_uuid": None,
                        "refuel_fields": [],
                        "refuel_api_timestamp": datetime.now(timezone.utc).strftime(
                            "%Y-%m-%dT%H:%M:%SZ",
                        ),
                    },
                ],
            )

        return {
            "application_id": application_id,
            "application_name": application,
            "refuel_output": full_labels,
        }

    @ensure_project
    def alabel(
        self,
        application: str,
        inputs: List[Dict],
        explain: bool = False,
        explain_fields: List[str] = None,
        telemetry: bool = False,
        model_id: Optional[str] = None,
    ):
        """
        Asynchronously labels a list of inputs using the specified application.

        Args:
            application (str): Name or ID of the application
            inputs (List[Dict]): List of inputs to be labeled
            explain (bool, optional): Whether to return explanations for the labels. Defaults to False.
            explain_fields (List[str], optional): List of fields to explain. Defaults to None.
            telemetry (bool, optional): Whether to collect telemetry data. Defaults to False.

        Returns:
            Dict: A dictionary containing the application ID, application name, and the output labels

        """
        application_id = self._get_application_id(application)
        url = self._api_base_url + f"/applications/{application_id}/label"
        explain_fields_serialized = ";".join(explain_fields) if explain_fields else None
        if model_id and model_id in VALID_LLM_MODELS.keys():
            model_id = VALID_LLM_MODELS[model_id]

        result = self._post(
            url=url,
            params={
                "application_id": application_id,
                "explain": explain,
                "telemetry": telemetry,
                "explain_fields": explain_fields_serialized,
                "is_async": True,
                "model_id": model_id,
            },
            json=inputs,
            headers=self._headers,
        )
        return result.get("data", {})

    @ensure_project
    def get_labeled_item(
        self,
        application: str,
        refuel_uuid: str,
    ) -> pd.DataFrame:
        """
        Fetches the labeled item with the specified refuel_uuid.

        Args:
            application (str): Name or ID of the application
            refuel_uuid (str): UUID of the labeled item
        Returns:
            A dictionary containing the application ID, application name, and the output labels

        """
        application_id = self._get_application_id(application)
        response = self._get(
            self._api_base_url + f"/applications/{application_id}/items/{refuel_uuid}",
            headers=self._headers,
        )
        return response.get("data", {})

    @ensure_project
    def feedback(
        self,
        application: str,
        refuel_uuid: str,
        label: Dict,
    ):
        application_dict = self.get_application(application)
        application_id = application_dict.get("id")
        subtasks = application_dict.get("subtasks")
        for subtask, subtask_label in label.items():
            subtask_id = None
            for subtask_dict in subtasks:
                if subtask_dict.get("name") == subtask:
                    subtask_id = subtask_dict.get("id")
            if not subtask_id:
                logger.error(
                    f"Subtask {subtask} not found for application {application}",
                )
                raise RefuelException(
                    HTTPStatus.NOT_FOUND,
                    f"No subtask with name={subtask} found.",
                )
            url = (
                self._api_base_url
                + f"/applications/{application_id}/items/{refuel_uuid}/label"
            )
            self._post(
                url=url,
                json={subtask_id: {"label": subtask_label}},
                headers=self._headers,
            )
        logger.info("Feedback was successfully received.")

    @ensure_project
    def finetune_model(
        self,
        task_id: str,
        model: str,
        hyperparameters: Optional[Dict] = {"num_epochs": 1},
        datasets: Optional[List] = None,
    ):
        finetuning_params = {
            "project_id": self._project_id,
            "task_id": task_id,
            "max_training_rows": None,
            "lora": True,
            "base_model": model,
            "augmented_finetuning_model": False,
            "hyperparameters": hyperparameters,
            "datasets": datasets,
        }
        return self._post(
            url=self._api_base_url + f"/projects/{self._project_id}/finetuned_models",
            json=finetuning_params,
            headers=self._headers,
        )

    @ensure_project
    def get_finetuned_models(self, task_id: Optional[str] = None):
        url = self._api_base_url + f"/projects/{self._project_id}/finetuned_models"
        return self._get(url=url, params={"task_id": task_id}, headers=self._headers)

    @ensure_project
    def cancel_finetuning(self, model_id: str):
        url = self._api_base_url + f"/finetuned_models/{model_id}"
        return self._patch(
            url=url,
            json={
                "model_id": model_id,
                "finetuning_run_status": "INTERRUPTED",
            },
            headers=self._headers,
        )

    def send_webhook_event(
        self,
        payload: Dict,
    ):
        url = self._api_base_url + "/webhook/events"
        response = self._post(
            url=url,
            json=payload,
            headers=self._headers,
        )
        return response
