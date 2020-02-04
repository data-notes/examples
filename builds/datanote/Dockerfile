ARG PYTHON_RELEASE=3.8.1
FROM python:${PYTHON_RELEASE}-buster
# https://hub.docker.com/r/eipdev/alpine-jupyter-notebook/dockerfile

# RUN apt-get update && apt-get install -y \
#     build-essential

WORKDIR /tmp
ADD requirements.txt requirements.txt
RUN pip3 install --upgrade -r requirements.txt

ENV JBLACK_REPO https://github.com/drillan/jupyter-black/archive/master.zip
RUN jupyter contrib nbextension install --user \
    && jupyter nbextension install $JBLACK_REPO --user \
    && jupyter nbextension enable jupyter-black-master/jupyter-black
ADD notebook.json /root/.jupyter/nbconfig/

RUN jupyter serverextension enable --py nbdime \
    && jupyter nbextension install --py nbdime \
    && jupyter nbextension enable --py nbdime
