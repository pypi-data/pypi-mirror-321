# install
```
pip install hfl-metrics
```

# import 
`from metrics import metrics_middleware`

# use
```python
from metrics import metrics_middleware
from fastapi import FastAPI, Request

app = FastAPI()
@app.middleware("http")
async def add_metrics(request: Request, call_next):
    return metrics_middleware(request, call_next)
```