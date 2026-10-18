"""
FastAPI 后端服务
农作物病虫害识别系统 API
"""
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import jwt
import datetime

app = FastAPI(title="农作物病虫害识别 API", version="1.0.0")
SECRET_KEY = "crop_disease_secret_key_2024"


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(req: LoginRequest):
    token = jwt.encode(
        {"sub": req.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
        SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    return {"filename": file.filename, "disease": "Tomato___Early_blight", "confidence": 0.94}


@app.get("/records")
def get_records():
    return {"records": []}


@app.get("/knowledge")
def get_knowledge():
    return {"knowledge": []}


@app.get("/health")
def health_check():
    return {"status": "ok"}
