from fastapi import FastAPI
import re

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def download_video(p_str: str):
    regular_patten = r'(?:https:)//.*(?=/)'
    url = re.search(regular_patten, p_str).group()
    return {"result": f"{url}"}
