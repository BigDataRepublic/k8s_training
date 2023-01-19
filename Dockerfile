### Install dependencies and export to requirements.txt file
FROM python:3.8.14-slim as build

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && \
    poetry export -f requirements.txt -o requirements.txt

### Install dependencies from requirements.txt
FROM python:3.8.14-slim as final

WORKDIR /app

COPY --from=build /app/requirements.txt .

RUN pip install -r requirements.txt

COPY data data
COPY artifacts artifacts
COPY api api

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
