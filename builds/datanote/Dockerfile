ARG PYTHON_RELEASE=3.8.1
FROM python:${PYTHON_RELEASE}-buster
# https://hub.docker.com/r/eipdev/alpine-jupyter-notebook/dockerfile

# RUN apt-get update && apt-get install -y \
#     build-essential

WORKDIR /tmp
ADD requirements.txt requirements.txt
RUN pip3 install --upgrade -r requirements.txt
RUN jupyter contrib nbextension install --user
