FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY requirements/test-requirements.txt /test-requirements.txt

COPY requirements/requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

RUN pip install --no-cache-dir -r /test-requirements.txt

COPY src /src/

WORKDIR /src

ENV DJANGO_SETTINGS_MODULE=config.settings
