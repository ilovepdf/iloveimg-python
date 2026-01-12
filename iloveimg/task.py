"""Module for handling file tasks using the iLoveIMG API."""

import os
import re
from typing import Any, Callable, Dict, Generic, List, Optional, Type, TypeVar, cast
from urllib.parse import unquote

from .abstract_task_element import AbstractTaskElement
from .exceptions import PathException, StartException, UploadException
from .file import File
from .iloveimg_api import Iloveimg

IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp"]

MAX_SIZE_MB = 100  # File size limit (100 MB)


T_FILE = TypeVar("T_FILE", bound=File)  # pylint: disable=invalid-name


T = TypeVar("T")


class FileManager:
    """Manages file operations including validation and upload processing.

    This class encapsulates file extension validation, size checking, and
    processing of upload responses from the API.
    """

    def __init__(self, cls_file: Type[File] = File):
        """Initialize FileManager.

        Args:
            cls_file (Type[File]): The File class to use for file objects.
        """
        self.cls_file = cls_file

    def validate_extension(
        self,
        file_path: str,
        extension_list: Optional[List[str]] = None,
    ) -> None:
        """Validate that the file extension is allowed.

        Args:
            file_path (str): Path to the file.
            extension_list (Optional[List[str]]): List of allowed extensions.

        Raises:
            ValueError: If the file extension is not allowed.
        """
        if extension_list is None:
            extension_list = IMAGE_EXTENSIONS

        extension_list_format = self.get_extension_format(extension_list)
        if not any(file_path.lower().endswith(ext) for ext in extension_list_format):
            msg = (
                f"Only image files are supported " f"{' '.join(extension_list_format)}"
            )
            raise ValueError(msg)

    def validate_file_exists(self, file_path: str) -> None:
        """Validate that a file exists and is within size limits.

        Args:
            file_path (str): Path to the file.

        Raises:
            ValueError: If file does not exist or exceeds size limit.
        """
        if not os.path.exists(file_path):
            raise ValueError(f"File {file_path} does not exist")

        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > MAX_SIZE_MB:
            raise ValueError(
                f"File {file_path} exceeds the maximum allowed size "
                f"({MAX_SIZE_MB} MB)"
            )

    @staticmethod
    def get_extension_list() -> List[str]:
        """Get the list of allowed image file extensions.

        Returns:
            List[str]: List of allowed extensions.
        """
        return IMAGE_EXTENSIONS

    @staticmethod
    def get_extension_format(
        extension_list: Optional[List[str]] = None,
    ) -> tuple:
        """Get extensions in dot format (e.g., '.jpg').

        Args:
            extension_list (Optional[List[str]]): List of extensions to
                format.

        Returns:
            tuple: Tuple of formatted extensions.
        """
        ext_list = extension_list or IMAGE_EXTENSIONS
        return tuple(f".{ext}" for ext in ext_list)

    def process_upload_response(self, response: Any, file_path: str) -> File:
        """Process the API response after uploading a file.

        Args:
            response: The API response object.
            file_path (str): Path to the uploaded file.

        Returns:
            File: The File object created from the response.

        Raises:
            UploadException: If the response is invalid.
        """
        try:
            response_body = response.json()
        except Exception as exc:
            raise UploadException("Upload response error") from exc

        filename = os.path.basename(file_path) or self.cls_file.get_temp_filename()
        file = self.cls_file(response_body["server_filename"], filename)
        return file


class DownloadManager:
    """Manages file download operations including path validation and
    response processing.

    This class handles download path validation, file content storage,
    and metadata extraction from download responses.
    """

    def __init__(self):
        """Initialize DownloadManager."""
        self.output_file: Optional[bytes] = None
        self.output_filename: Optional[str] = None
        self.output_file_name: Optional[str] = None
        self.output_file_type: Optional[str] = None

    def validate_download_path(self, path: Optional[str]) -> None:
        """Validate the download destination path.

        Args:
            path (Optional[str]): The destination path.

        Raises:
            PathException: If the path is invalid.
        """
        if path is None:
            return

        if not os.path.isdir(path):
            if os.path.splitext(path)[1]:
                raise PathException(
                    "Invalid download path. Use method set_output_filename() "
                    "to set the output file name."
                )
            raise PathException(
                "Invalid download path. Set a valid folder path "
                "to download the file."
            )

    def save_file(self, path: Optional[str], filename: Optional[str]) -> None:
        """Save downloaded file to disk.

        Args:
            path (Optional[str]): Destination folder path.
            filename (Optional[str]): Filename to use.

        Raises:
            ValueError: If output file data is None.
        """
        if self.output_file is None:
            raise ValueError("Data to write cannot be None")

        destination = os.path.join(path or ".", filename or "")
        with open(destination, "wb") as file_dest:
            file_dest.write(self.output_file)

    def process_download_response(self, response: Any) -> None:
        """Process download response and extract metadata.

        Args:
            response: The API response object.
        """
        self.output_file = response.content
        content_disposition = response.headers.get("Content-Disposition", "")

        filename = None

        # Try UTF-8 encoded filename first
        match = re.search(r"filename\*=utf-8\'\'([^\s]+)", content_disposition)
        if match:
            filename = unquote(match.group(1).replace('"', ""))
        else:
            # Try regular filename
            match = re.search(r'filename="([^"]+)"', content_disposition)
            if match:
                filename = match.group(1)

        self.output_file_name = filename or "output_unknown_filename.unknown"
        self.output_file_type = (
            os.path.splitext(self.output_file_name)[1][1:]
            if self.output_file_name
            else None
        )


class PayloadBuilder:
    """Builds and validates request payloads for tasks.

    This class encapsulates payload construction and validation logic
    for API requests.
    """

    def __init__(self, to_payload_func: Callable[[], Dict[str, Any]]) -> None:
        """Initialize PayloadBuilder.

        Args:
            to_payload_func (Callable[[], Dict[str, Any]]): Function that returns the
                payload dictionary.
        """
        self._to_payload = to_payload_func

    def build_body(self, version: str) -> Dict[str, Any]:
        """Build the request body for API operations.

        Args:
            version (str): The library version.

        Returns:
            Dict[str, Any]: The request body dictionary.

        Raises:
            ValueError: If body is invalid.
        """
        data = self._to_payload()

        # Remove server config keys
        for key in ["timeout_large", "timeout", "time_delay"]:
            data.pop(key, None)

        body = {"data": data, "params": {"v": version}}
        self.validate_body(body)
        return body

    @staticmethod
    def validate_body(body: Optional[Dict[str, Any]]) -> bool:
        """Validate the request body.

        Args:
            body (Optional[Dict[str, Any]]): The request body dictionary.

        Returns:
            bool: True if valid.

        Raises:
            ValueError: If the body is invalid.
        """
        if not body:
            raise ValueError("Invalid body")
        return True


class TaskStateManager:
    """Manages task state including validation and state updates.

    This class encapsulates task state management, including task ID
    tracking, status updates, and validation.
    """

    def __init__(self):
        """Initialize TaskStateManager."""
        self.task: Optional[str] = None
        self.status: Optional[str] = None
        self.status_message: Optional[str] = None
        self.remaining_credits: Optional[int] = None
        self.remaining_files: Optional[int] = None
        self.remaining_pages: Optional[int] = None

    def validate_task_started(self) -> None:
        """Validate that the task has been started.

        Raises:
            ValueError: If the task is not started.
        """
        if not self.task:
            raise ValueError("Current task does not exist. You must start your task")

    def set_task(self, task: str) -> None:
        """Set the task ID.

        Args:
            task (str): The task ID.
        """
        self.task = task

    def get_task_id(self) -> Optional[str]:
        """Get the task ID.

        Returns:
            Optional[str]: The task ID.
        """
        return self.task

    def set_remaining_credits(self, remaining_credits: Optional[int]) -> None:
        """Set the remaining credits.

        Args:
            remaining_credits (Optional[int]): Number of remaining credits.
        """
        self.remaining_credits = remaining_credits

    def set_remaining_files(self, remaining_files: Optional[int]) -> None:
        """Set the remaining files.

        Args:
            remaining_files (Optional[int]): Number of remaining files.
        """
        self.remaining_files = remaining_files

    def set_remaining_pages(self, remaining_pages: Optional[int]) -> None:
        """Set the remaining pages.

        Args:
            remaining_pages (Optional[int]): Number of remaining pages.
        """
        self.remaining_pages = remaining_pages

    def update_status(self, result: Dict[str, Any]) -> None:
        """Update task status from result.

        Args:
            result (Dict[str, Any]): The result dictionary from API.
        """
        self.status = result.get("status")
        self.status_message = result.get("status_message")


class Task(
    Iloveimg, Generic[T_FILE], AbstractTaskElement
):  # pylint: disable=too-many-instance-attributes,too-many-public-methods
    """
    Class for handling file tasks using the iLoveIMG API.

    This class provides core functionality for managing file-based tasks such
    as uploading, downloading, and processing images. It supports validation,
    error handling, and integration with the iLoveIMG API.

    Args:
        public_key (str, optional): API public key. If not provided,
            uses ILOVEIMG_PUBLIC_KEY env variable.
        secret_key (str, optional): API secret key. If not provided,
            uses ILOVEIMG_SECRET_KEY env variable.
        make_start (bool): Whether to start the task immediately.
            Default is False.

    Example:
        class AnyTask(Task):
            _tool = "anytool"

            _DEFAULT_PAYLOAD = {
                "attr1": "value1",
                "attr2": "value2",
            }

        @property
        def attr1(self) -> str:
            return self._get_attr("attr1")

        @attr1.setter
        def attr1(self, value: str):
            self._set_attr("attr1", value)

        # Instantiate the task
        any_tool = AnyTask(public_key, secret_key)
    """

    cls_file: Type[T_FILE] = File  # type: ignore
    _endpoint_execute = "process"
    _tool: str

    _DEFAULT_PAYLOAD = {
        "tool": None,
        "task": None,
        "files": [],
    }

    def __init__(
        self,
        public_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        make_start: bool = False,
    ) -> None:
        """
        Initialize a Task instance.

        Args:
            public_key (Optional[str]): API public key.
            secret_key (Optional[str]): API secret key.
            make_start (bool): Whether to start the task immediately.
        """
        super().__init__(public_key, secret_key)
        self.files: List[T_FILE] = []
        self.result: Optional[Dict[str, Any]] = None

        # Initialize component managers
        self._file_manager = FileManager(self.cls_file)
        self._download_manager = DownloadManager()
        self._payload_builder = PayloadBuilder(self._to_payload)
        self._state_manager = TaskStateManager()

        self.tool = self._tool

        if make_start:
            self.start()

    @property
    def tool(self) -> Optional[str]:
        """Get the tool name.

        Returns:
            Optional[str]: The current tool name. Default is None.
        """
        return self._payload["tool"]

    @tool.setter
    def tool(self, value: Optional[str]) -> None:
        """Set the tool name.

        Args:
            value (Optional[str]): The tool name.
        """
        self._payload["tool"] = value

    def start(self) -> None:
        """
        Start the task by requesting a server assignment from the API.

        Raises:
            StartException: If the tool is not set or the API response is
                invalid.
        """
        if self.tool is None:
            raise StartException("Tool must be set")

        data = {"v": self.VERSION}
        body = {"params": data}
        response = self.send_request("get", f"start/{self.tool}", body)

        try:
            response_body = response.json()
        except Exception as exc:
            raise StartException("Invalid response") from exc

        if not response_body.get("server"):
            raise StartException("no server assigned on start")

        # Update state
        self._state_manager.set_remaining_files(response_body.get("remaining_files"))
        self._state_manager.set_remaining_pages(response_body.get("remaining_pages"))
        self._state_manager.set_remaining_credits(
            response_body.get("remaining_credits")
        )

        # Set server and task
        self.set_worker_server("https://" + response_body["server"])
        self.set_task(response_body["task"])

    def set_task(self, task: str) -> None:
        """Set the current task ID.

        Args:
            task (str): The task ID.
        """
        self._state_manager.set_task(task)
        self._payload["task"] = task

    def get_task_id(self) -> Optional[str]:
        """Get the current task ID.

        Returns:
            Optional[str]: The task ID, or None if not set.
        """
        return self._state_manager.get_task_id()

    def append_file(self, file: T_FILE) -> T_FILE:
        """Append a file to the task's file list.

        Args:
            file (T_FILE): The File object to append.

        Returns:
            T_FILE: The appended File object.
        """
        self.files.append(file)
        return file

    def add_file(self, file_path: str, **kwargs: Any) -> T_FILE:
        """Add a file to the task by uploading it.

        Args:
            file_path (str): Path to the file to add.
            **kwargs: Additional parameters for file upload.

        Returns:
            T_FILE: The uploaded File object.

        Raises:
            ValueError: If the file extension is not supported or the task
                is not started.
        """
        self._file_manager.validate_extension(file_path)
        self._state_manager.validate_task_started()
        file = self.upload_file(self.get_task_id(), file_path, kwargs)
        self.append_file(file)
        return file

    def upload_file(
        self,
        task: Optional[str],
        file_path: str,
        extra_params: Optional[Dict[str, Any]] = None,
    ) -> T_FILE:
        """Upload a file to the API for the current task.

        Args:
            task (Optional[str]): The task ID.
            file_path (str): Path to the file to upload.
            extra_params (Optional[Dict[str, Any]]): Additional parameters
                for upload.

        Returns:
            T_FILE: The uploaded File object.

        Raises:
            ValueError: If the file does not exist or exceeds size limit.
        """
        self._file_manager.validate_file_exists(file_path)

        with open(file_path, "rb") as file_obj:
            files = {"file": file_obj}
            data: Dict[str, Any] = {"task": task, "v": self.VERSION}
            if extra_params:
                data.update(extra_params)
            body = {"files": files, "data": data}
            response = self.send_request("post", "upload", body)

        return cast(
            T_FILE, self._file_manager.process_upload_response(response, file_path)
        )

    def get_status(
        self,
        server: Optional[str] = None,
        task_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get the status of the current task from the API.

        Args:
            server (Optional[str]): The server URL. If not provided,
                uses the current worker server.
            task_id (Optional[str]): The task ID. If not provided,
                uses the current task ID.

        Returns:
            Dict[str, Any]: Status response from the API.

        Raises:
            ValueError: If server or task_id is not set.
        """
        server = server or self.get_worker_server()
        task_id = task_id or self.get_task_id()

        if server is None or task_id is None:
            raise ValueError("Cannot get status if no file is uploaded")

        return super().get_status(server, task_id)

    def delete(self) -> "Task":
        """Delete the current task from the API.

        Returns:
            Task: Self for chaining.

        Raises:
            ValueError: If the task is not started.
        """
        self._state_manager.validate_task_started()
        response = self.send_request("delete", f"task/{self.get_task_id()}")
        self.result = response.json()
        return self

    def download(self, path: Optional[str] = None) -> None:
        """Download the processed file from the API.

        Args:
            path (Optional[str]): Destination folder path.

        Raises:
            PathException: If the path is invalid.
            ValueError: If the file data is None.
        """
        self._state_manager.validate_task_started()
        self._download_manager.validate_download_path(path)

        # Download file data
        response = self._download_request_data(self.get_task_id())
        self._download_manager.process_download_response(response)

        # Save to disk
        dest_path = path or "."
        filename = (
            self._download_manager.output_filename
            or self._download_manager.output_file_name
        )
        self._download_manager.save_file(dest_path, filename)

    def _download_request_data(self, task: Optional[str]) -> Any:
        """Build and send the download request for the given task.

        Args:
            task (Optional[str]): The task ID.

        Returns:
            Any: The API response object.
        """
        data = {"v": self.VERSION}
        body = {"data": data}
        response = self.send_request("get", f"download/{task}", body)
        return response

    def execute(self) -> "Task":
        """Execute the current task by sending it to the API.

        Returns:
            Task: Self for chaining.

        Raises:
            ValueError: If the task is not started.
        """
        self._state_manager.validate_task_started()
        body = self._payload_builder.build_body(self.VERSION)
        endpoint = self._endpoint_execute
        response = self.send_request("post", endpoint, body)
        self.result = response.json()

        # Update status after execution
        if self.result is not None:
            self._state_manager.update_status(self.result)
        return self

    def set_output_filename(self, filename: str) -> "Task":
        """Set the output filename for the downloaded file.

        Args:
            filename (str): The output filename.

        Returns:
            Task: Self for chaining.
        """
        self._download_manager.output_filename = filename
        return self

    def _to_payload(self) -> Dict[str, Any]:
        """Update the payload with the current files list.

        Returns:
            Dict[str, Any]: The updated payload dictionary.
        """
        self._payload["files"] = self.files
        return super()._to_payload()

    @property
    def output_file(self) -> Optional[bytes]:
        """Get the downloaded file content.

        Returns:
            Optional[bytes]: The file content, or None if not downloaded.
        """
        return self._download_manager.output_file

    @property
    def output_filename(self) -> Optional[str]:
        """Get the output filename set by user.

        Returns:
            Optional[str]: The output filename.
        """
        return self._download_manager.output_filename

    @property
    def output_file_name(self) -> Optional[str]:
        """Get the output file name from response.

        Returns:
            Optional[str]: The file name extracted from response.
        """
        return self._download_manager.output_file_name

    @property
    def output_file_type(self) -> Optional[str]:
        """Get the output file type.

        Returns:
            Optional[str]: The file extension.
        """
        return self._download_manager.output_file_type

    @property
    def task(self) -> Optional[str]:
        """Get the task ID.

        Returns:
            Optional[str]: The task ID. Default is None.
        """
        return self._state_manager.task

    @task.setter
    def task(self, value: Optional[str]) -> None:
        """Set the task ID.

        Args:
            value (Optional[str]): The task ID.
        """
        self._state_manager.task = value

    @property
    def status(self) -> Optional[str]:
        """Get the task status.

        Returns:
            Optional[str]: The task status. Default is None.
        """
        return self._state_manager.status

    @property
    def status_message(self) -> Optional[str]:
        """Get the task status message.

        Returns:
            Optional[str]: The status message. Default is None.
        """
        return self._state_manager.status_message

    @property
    def remaining_files(self) -> Optional[int]:
        """Get remaining files count.

        Returns:
            Optional[int]: Number of remaining files. Default is None.
        """
        return self._state_manager.remaining_files

    @property
    def remaining_pages(self) -> Optional[int]:
        """Get remaining pages count.

        Returns:
            Optional[int]: Number of remaining pages. Default is None.
        """
        return self._state_manager.remaining_pages

    @property
    def remaining_credits(self) -> Optional[int]:
        """Get remaining credits count.

        Returns:
            Optional[int]: Number of remaining credits. Default is None.
        """
        return self._state_manager.remaining_credits

    def _validate_file_extension(
        self, file_path: str, extension_list: Optional[List[str]] = None
    ) -> None:
        """Validate file extension.

        Args:
            file_path (str): Path to the file.
            extension_list (Optional[List[str]]): List of allowed extensions.

        Raises:
            ValueError: If the file extension is not allowed.
        """
        self._file_manager.validate_extension(file_path, extension_list)

    def _validate_task_started(self) -> None:
        """Validate that task has been started.

        Raises:
            ValueError: If the task is not started.
        """
        self._state_manager.validate_task_started()

    def get_extension_list(self) -> List[str]:
        """Get the list of allowed image file extensions.

        Returns:
            List[str]: List of allowed extensions.
        """
        return self._file_manager.get_extension_list()

    def get_extension_list_format(
        self, extension_list: Optional[List[str]] = None
    ) -> tuple:
        """Get extensions in dot format.

        Args:
            extension_list (Optional[List[str]]): List of extensions to format.

        Returns:
            tuple: Tuple of formatted extensions.
        """
        return self._file_manager.get_extension_format(extension_list)

    def _set_remaining_credits(self, remaining_credits: int) -> None:
        """Set remaining credits.

        Args:
            remaining_credits (int): Number of remaining credits.
        """
        self._state_manager.set_remaining_credits(remaining_credits)

    def _set_remaining_files(self, remaining_files: int) -> None:
        """Set remaining files.

        Args:
            remaining_files (int): Number of remaining files.
        """
        self._state_manager.set_remaining_files(remaining_files)

    def _set_remaining_pages(self, remaining_pages: int) -> None:
        """Set remaining pages.

        Args:
            remaining_pages (int): Number of remaining pages.
        """
        self._state_manager.set_remaining_pages(remaining_pages)

    def validate_body(self, body: Dict[str, Any]) -> bool:
        """Validate request body.

        Args:
            body (Dict[str, Any]): The request body dictionary.

        Returns:
            bool: True if valid.

        Raises:
            ValueError: If the body is invalid.
        """
        return self._payload_builder.validate_body(body)

    def build_body(self) -> Dict[str, Any]:
        """Build request body.

        Returns:
            Dict[str, Any]: The request body dictionary.
        """
        return self._payload_builder.build_body(self.VERSION)
