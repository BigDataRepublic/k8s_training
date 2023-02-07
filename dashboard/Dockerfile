### Install dependencies and export to requirements.txt file
FROM python:3.11-slim-bullseye as build

ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN pip install streamlit psycopg2-binary

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
