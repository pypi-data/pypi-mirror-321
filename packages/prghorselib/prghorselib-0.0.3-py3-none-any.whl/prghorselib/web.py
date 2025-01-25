import sys
from fastapi import Response
from datetime import datetime

def set_headers(response) -> Response:
    response.headers['python-version'] = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    response.headers['timestamp'] = datetime.now().strftime("%H:%M:%Y %H:%M:%S")
    return response