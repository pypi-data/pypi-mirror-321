import json
import uuid
from collections.abc import Callable
from datetime import datetime
from http.server import BaseHTTPRequestHandler
from typing import Any


class SDKRunner:
    fetch_status: Callable[[], dict]

    def __init__(self, status_func: Callable[[], dict]) -> None:
        self.fetch_status = status_func
        pass

    def validate(self, response: dict) -> None:
        if response.get("status", None) not in ["ONLINE", "SOME_ERRORS", "OFFLINE"]:
            raise ValueError("status field must should exist and be one of ONLINE, SOME_ERRORS, OFFLINE")
        try:
            datetime.fromisoformat(response["created_at"])
        except ValueError:
            raise ValueError("created_at field should exist and must be a valid ISO 8601 datetime")

        try:
            uuid.UUID(response["project_uuid"])

        except ValueError:
            raise ValueError("project_uuid field should exist and must be a valid UUID")

        return

    def get_status(self) -> str:
        """
        Runs a callable that must return a dict
        """
        status = self.fetch_status()
        self.validate(status)
        return json.dumps(status)

    def validate_output(self) -> None:
        pass


class SJSDK(BaseHTTPRequestHandler):
    """
    Simple Request handler that serves the status of the process
    """

    def __init__(self, request: Any, client_address: Any, server: Any, callable: Callable[[], dict]) -> None:
        self.runner = SDKRunner(callable)
        super().__init__(request, client_address, server)

    def do_GET(self) -> None:
        if self.path != "/status":
            self._handle_bad_request()

        response = self.runner.get_status()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

    def _handle_bad_request(self) -> None:
        response = json.dumps({"errorCode": "PathNotAvailable", "message": "path does not exist."})
        self.send_response(400, "Bad Request")
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))
