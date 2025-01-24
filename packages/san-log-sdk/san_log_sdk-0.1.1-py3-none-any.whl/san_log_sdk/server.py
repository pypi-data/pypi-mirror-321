import sys
from collections.abc import Callable
from http.server import HTTPServer

from sj_sdk import SJSDK


def run(callable: Callable[[], dict], host: str = "0.0.0.0", port: int = 8001) -> None:
    """
    Simple HTTP Server that serves the status of the script.
    It serves as a simple process that mantains the container alive.
    \nNote that the callable must return a dict with the following keys, as they are validated:
    - status (str): Status of the script
    - created_at (str): ISO 8601 datetime
    - project_uuid (str): UUID

    Args:
    -----
        - host (str): Host to run the server on. Default is 0.0.0.0
        - port (int): Port number to run the server on. Default is 8001
        - callable (Callable): Callable that returns the status of the script
    """
    with HTTPServer((host, port), lambda *args: SJSDK(*args, callable)) as httpd:
        sys.stdout.write(f"Serving at http://{host}:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nReceived signal: Ctrl+C, Shutting down...")
            httpd.shutdown()
            httpd.server_close()
            sys.exit(0)
