from fastapi import FastAPI
import uvicorn
from app.api.endpoints import router

app = FastAPI(title = "AI Email Classifier")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)