FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000

RUN mkdir /web

WORKDIR /web

COPY ../poetry.lock ../pyproject.toml /web/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

ADD . ./

CMD poetry run alembic upgrade head && \
    ["python", "main.py"]