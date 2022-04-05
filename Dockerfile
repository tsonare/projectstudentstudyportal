FROM python:3
LABEL maintainer="studentstudyportal1910.herokuapp.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app




# FROM python:3

# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# ADD . /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# COPY . /app 


# FROM python:3.8-slim-buster

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]