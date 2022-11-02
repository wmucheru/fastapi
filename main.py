from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version

app = FastAPI(title="Test App")


@app.get("/")
@version(1)
async def root():
    return {
        "message": "Hello world"
    }

app = VersionedFastAPI(app,
                       version_format='{major}',
                       prefix_format='/v{major}')
