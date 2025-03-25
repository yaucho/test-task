FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional

WORKDIR /test-task-app

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip && pip install poetry && poetry install --no-root

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "/test-task-app/entrypoint.sh"]