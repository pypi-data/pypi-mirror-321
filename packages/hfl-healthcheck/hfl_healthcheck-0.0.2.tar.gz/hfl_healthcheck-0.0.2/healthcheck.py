import os
import time
import requests

def health_check_sender(minutes: int):
    url = os.getenv("MONITORING_URL")
    service_name = os.getenv("SERVICE_NAME")
    while True:
        minutes = max(minutes, 1)
        # will not ask for getenv as soon as it is defined
        url = url or os.getenv("MONITORING_URL")
        service_name = service_name or os.getenv("SERVICE_NAME")
        if url is None or service_name is None:
            time.sleep(minutes * 60)
            continue
        data = {
            "service_name": service_name,
            "status": 1,
            "period": minutes
        }
        _ = requests.post(f"{url}/healthcheck", data=data, timeout=30)
        # sleep in seconds
        time.sleep(minutes * 60)

