FROM python:3.9.16-slim
RUN apt-get update && apt-get install -y \
    software-properties-common \
    gnupg \
    curl \
    wget \
    nano \
    dos2unix

RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc \
    --create-dirs -o /usr/local/bin/mc &&  \
    chmod +x /usr/local/bin/mc 

RUN pip install pandas duckdb minio boto3 pymongo cassandra-driver requests 


WORKDIR /app

COPY  app/ .