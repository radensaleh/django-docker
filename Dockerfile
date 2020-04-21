# download python version 3.6 from hub.docker
FROM python:3.6
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# create new directory
RUN mkdir /django-docker
# workdir
WORKDIR /django-docker
# add file requirements to folder
ADD requirements.txt /django-docker/
# install library from requirements
RUN pip install -r requirements.txt
# add all file to folder django-docker
ADD . /django-docker/
# run cmd
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]