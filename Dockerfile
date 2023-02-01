FROM python:3.11-slim-bullseye as build

ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.2

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-ansi --no-interaction && \
    poetry export -f requirements.txt -o requirements.txt

### Install dependencies from requirements.txt
FROM python:3.11-slim-bullseye as final

WORKDIR /app

COPY --from=build /app/requirements.txt .

RUN pip install -r requirements.txt

# make the copying of files explicit
COPY ./data data
COPY ./artifacts artifacts
COPY ./api api

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
