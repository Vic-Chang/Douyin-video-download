FROM python:3.10-alpine

ENV TZ=Asia/Taipei

WORKDIR /

COPY . /

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]