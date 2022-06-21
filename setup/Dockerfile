FROM python:3.9-slim

RUN pip install requests

WORKDIR /app
COPY . /app/

CMD [ "python3", "/app/init-metabase.py"]
