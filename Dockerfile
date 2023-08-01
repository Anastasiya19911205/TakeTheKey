FROM python:3.11

RUN mkdir TakeTheKey

WORKDIR TakeTheKey

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN cd TakeTheKey

#
#
# FROM python:3.10-alpine
# # RUN mkdir TakeTheKey
# #
# COPY requirements.txt
# RUN pip install -r requirements.txt
# COPY . .
# WORKDIR TakeTheKey
# CMD ['python','manage.py', 'runserver']