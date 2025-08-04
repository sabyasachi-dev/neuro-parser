from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Path to Angular build
ANGULAR_DIST = os.path.join("dist", "neuro-parser", "browser")

# Serve index.html for root
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(ANGULAR_DIST, "index.html"))

# Serve all other files (JS, CSS, assets)
@app.get("/{file_path:path}")
async def serve_file(file_path: str):
    full_path = os.path.join(ANGULAR_DIST, file_path)

    if os.path.isfile(full_path):
        return FileResponse(full_path)
    else:
        # If file doesn't exist, serve index.html for Angular routing
        return FileResponse(os.path.join(ANGULAR_DIST, "index.html"))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
