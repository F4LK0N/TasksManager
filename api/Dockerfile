FROM python:3.11-slim as base

WORKDIR /app

COPY ./src/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ /app/

EXPOSE 8000

CMD ["python", "app.py", "runserver", "0.0.0.0:8000"]
