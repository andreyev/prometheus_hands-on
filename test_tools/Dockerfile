# syntax=docker/dockerfile:1
FROM python:alpine3.16
# Base image
# https://hub.docker.com/_/python
# Source: https://docs.docker.com/language/python/build-images/
# Elegantly activating a virtualenv in a Dockerfile: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

# Informations about image
LABEL maintainer="André Déo" \
      author="André Déo" \
      email="andredeo@gmail.com" \
      description="Docker image to provide a simple Flask Web Server that displays the Header and Body of requests" \
      licence="GNU GPL v2"

# Running pip in virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Workdir
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt requirements.txt

# Install Requirements
RUN pip3 install -r requirements.txt

# Copy App Files
COPY main.py main.py

# Clear cache of packages in Alpine Linux
# Source: https://wiki.alpinelinux.org/wiki/Local_APK_cache
# https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management
RUN rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

# Entrypoint
CMD [ "python3", "-u", "main.py" ]