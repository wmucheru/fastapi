from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
@app.get("/")
async def root():
    return {
        "message": "Hello world"
    }
