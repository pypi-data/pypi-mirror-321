
# SJSDK

Little package for containarized process to share logs and overal status.
This simple, really simple package is intended to be used as a private resource for all services to be able to centralice all log events to a main page.

### How to use it:

In your logger:
```python
import logging

from log_sdk.threaded_handler imprt SanLogSDK

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# host and port of san log page
base_url = "localhost"
project_uuid = "e9b136ee-ffcb-4cdd-bea0-cc560796a01c"
port = 8765
logger.addHandler(SanLogSDK(base_url, project_uuid, port))
```


If you need the endpoint for status in your containarized process, you need to pass a function that creates de response dict and pass it the server.run as:

```python

from log_sdk import server

from my_module import my_status_func

host = "0.0.0.0"
port = "8001"

if __name__== "__main__":
    server.run(my_status_func, host=host, port=port)
```

And this is loaded in the command of your docker-compose file like so:
```yaml
services:
  app:
    container_name: my_process_container
    build:
      context: .
      network: "host"
      
    network_mode: "host"
    working_dir: /app
    command: python /app/my_status_server.py 
```