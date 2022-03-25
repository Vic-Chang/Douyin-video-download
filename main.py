import json
import re
import requests
from fastapi import FastAPI
from urllib.parse import urlparse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def get_video_url(p_str: str):
    req = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
    }
    regular_patten = r'(?:https:)//.*(?=/)'
    input_url = re.search(regular_patten, p_str).group()
    response = req.get(input_url, headers=headers)

    redirect_url = urlparse(response.url).path.rstrip('/')
    uid = redirect_url.rsplit('/', 1)[1]
    douyin_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={uid}'
    video_info = req.get(douyin_url, timeout=5, headers=headers)

    video_info_obj = json.loads(video_info.text)
    video_url = video_info_obj['item_list'][0]['video']['play_addr']['url_list'][0]
    video_url = video_url.replace('playwm', 'play')

    return {"result": f"{video_url}"}
