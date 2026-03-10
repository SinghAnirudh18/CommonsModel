import logging
from fastapi import FastAPI, Request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/query")
async def handle_query(request: Request):
    body = await request.json()
    logger.info(f"Received query: {body}")
    return {"status": "ok", "received": body}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
