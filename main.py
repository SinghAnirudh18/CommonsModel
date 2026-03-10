from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/query")
async def handle_query(request: Request):
    body = await request.json()
    print("Received query:", body)
    return {"status": "ok", "received": body}
