FROM python:3.9-slim

RUN apt-get update && apt-get -y install build-essential

RUN apt-get install -y sudo
RUN echo "appuser ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/appuser && chmod 0440 /etc/sudoers.d/appuser

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN /usr/local/bin/pip install --no-cache-dir \
    wheel \
    gunicorn \
    orjson \
    ujson \
    uvicorn[standard]

ONBUILD COPY requirements.txt /app/requirements.txt
ONBUILD RUN /usr/local/bin/pip install --no-cache-dir -r requirements.txt
ONBUILD COPY . /app

EXPOSE 8080
WORKDIR /app