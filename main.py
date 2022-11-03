from fastapi import FastAPI

app = FastAPI(title="Test App")
v1 = FastAPI()


@app.get("/")
@v1.get("/")
async def root():
    return {
        "message": "Hello world"
    }

app.mount("/api/v1", v1)
