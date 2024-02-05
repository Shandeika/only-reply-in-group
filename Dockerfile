# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.10.9
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

COPY . .

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["python", "main.py"]