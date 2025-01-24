import os
import time
import requests
from fastapi import Request, Response


async def metrics_middleware(request: Request, call_next):
    url = os.getenv("MONITORING_URL")
    service_name = os.getenv("SERVICE_NAME")
    if url is None or service_name is None:
        return
    start_time = time.perf_counter()
    response: Response = await call_next(request)
    process_time = time.perf_counter() - start_time
    data = {
        "service_name": service_name,
        "endpoint": str(request.url.path),
        "method": str(request.method),
        "status": response.status_code,
        "duration": process_time
    }
    _ = requests.post(f"{url}/metrics", data=data)
    return response

