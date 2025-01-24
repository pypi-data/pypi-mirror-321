import logging

from threaded_handler import SanLogSDK

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

base_url = "localhost"
project_uuid = "e9b136ee-ffcb-4cdd-bea0-cc560796a01c"
logger.addHandler(SanLogSDK(base_url, project_uuid, 8000))

try:
    result = 1 + "a"  # type: ignore
except Exception as e:
    logger.error(e)
