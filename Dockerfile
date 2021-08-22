FROM python:3.9.5

WORKDIR /code

RUN mkdir -p requirements

COPY movies_admin/requirements/*.txt requirements/

RUN pip install -r requirements/production.txt

COPY ./movies_admin .
