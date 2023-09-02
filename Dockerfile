FROM python:3.11.1-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install python-dotenv
RUN python -m pip install psycopg2-binary
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY . .