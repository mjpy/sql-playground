FROM python:3.9-slim

RUN pip install requests

RUN mkdir /app
COPY init-metabase.py /app/

CMD [ "python3", "/app/init-metabase.py"]
