# FROM python:3.10-alpine
# RUN mkdir app
# COPY . app
# WORKDIR app
# CMD ['python', 'new.py']
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