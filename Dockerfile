FROM python:3.7-slim-stretch

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
RUN pip3 install --upgrade pip setuptools; \pip3 install -r /requirements.txt;

COPY api /app/api

WORKDIR /app

# bond.py will run when container starts up on the device
CMD ["gunicorn", "-b", "0.0.0.0:80", "api.server:rest"]