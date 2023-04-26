FROM python:3.11.3-slim-buster as fastapi-backend

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./api ./app
RUN ls

RUN apt-get update
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000