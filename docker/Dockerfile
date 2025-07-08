FROM python:3.11-slim

WORKDIR /code

COPY uv.lock pyproject.toml /code/
RUN pip install uv && uv sync

COPY . /code

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]