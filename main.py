from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from transformers import pipeline


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {"message": "this is the health endpoint"}


@app.post("/summarize")
async def summarize(transcript: str):
    # data = transcript
    json_transcript = jsonable_encoder(transcript)
    return JSONResponse(content=json_transcript)