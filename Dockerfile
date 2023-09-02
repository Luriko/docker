FROM python:3.11.1-slim

COPY requirements.txt .

RUN python -m pip install python-dotenv
RUN python -m pip install psycopg2-binary
RUN pip install -r /requirements.txt


COPY . .