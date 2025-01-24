import http.client
import json


class SanLogHttpClient:
    """
    Client that sends logs to the server in specific format.
    """

    headers = {"Content-Type": "application/json"}

    def __init__(self, base_url: str, port: int = 8000) -> None:
        self.base_url = base_url
        self.port = port

    def post_entry(self, data: dict) -> None:
        if data is None or data == {}:
            raise Exception("Post data cannot be empty.")

        body = json.dumps(data).encode("utf-8")

        conn = http.client.HTTPConnection(f"{self.base_url}", self.port)
        conn.request("POST", "/logPanel/log/", body, self.headers)
        print(conn.getresponse().read())
