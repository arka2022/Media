from fastapi import FastAPI, HTTPException
from flask import jsonify
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.thumbnailCreation.engine import thumbnail_using_adaptive, thumbnail_using_threshold, thumbnail_using_content
from app.thumbnailCreation.functions import downloadVideoFromS3, adaptiveScreenDetection, getFPS, createJson

app=FastAPI()



class Payload(BaseModel):
    file_name:str
    file_path:str

@app.get("/")
async def fn_call():
    return JSONResponse({'message': 'Hello from Thumbnail'})

@app.post("/create/thumbnails_using_adaptive")
async def fn_call(payload:Payload):
    if not payload:
        raise HTTPException(status_code=404, detail="payload is required")
    video_name = payload.file_name
    video_s3_path=payload.file_path
    return thumbnail_using_adaptive(video_name,video_s3_path)

@app.post("/create/thumbnails_using_threshold")
async def fn_call(payload:Payload):
    if not payload:
        raise HTTPException(status_code=404, detail="payload is required")
    video_name = payload.file_name
    video_s3_path=payload.file_path
    return thumbnail_using_threshold(video_name,video_s3_path)

@app.post("/create/thumbnails_using_content")
async def fn_call(payload:Payload):
    if not payload:
        raise HTTPException(status_code=404, detail="payload is required")
    video_name = payload.file_name
    video_s3_path=payload.file_path
    return thumbnail_using_content(video_name,video_s3_path)




#  uvicorn {file_name}:app --reload
#  uvicorn thumbnailCreation_with_AdaptiveSceneDetection:app --reload
