import datetime
import logging
from queue import Queue
from threading import Thread

from client import SanLogHttpClient


class SanLogSDK(logging.Handler):
    """
    Handler that makes uses of HttpClient to send logs to the server
    """

    client: SanLogHttpClient
    log_queue: Queue
    project_uuid: str
    worker_thread: Thread

    def __init__(self, base_url: str, project_uuid: str, port: int) -> None:
        super().__init__()
        self.client = SanLogHttpClient(base_url, port)
        self.project_uuid = project_uuid
        self.log_queue = Queue()
        self.worker_thread = Thread(target=self._process_logs, daemon=True)
        self.worker_thread.start()

    def _format_log_data(self, record: logging.LogRecord) -> dict:
        """Formats the data to be sent"""
        return {
            "project_uuid": self.project_uuid,
            "type": record.levelname,
            "log": record.getMessage(),
            "created_at": datetime.datetime.fromtimestamp(record.created).isoformat(),
        }

    def emit(self, record: logging.LogRecord) -> None:
        """Emits the log to the queue"""
        entry = self._format_log_data(record)
        self.log_queue.put(entry)

    def _process_logs(self) -> None:
        """Processes the logs from the queue"""
        while True:
            try:
                entry = self.log_queue.get()
                if entry is None:
                    break
                else:
                    self.client.post_entry(entry)

            except Exception as e:
                print(f"Error logging in threaded handler: {e}")
            finally:
                self.log_queue.task_done()

    def close(self) -> None:
        self.log_queue.put(None)
        self.worker_thread.join()
        super().close()
