FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./app /app
COPY ./pyproject.toml /app/pyproject.toml
WORKDIR /app
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
