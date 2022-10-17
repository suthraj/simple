# FILE: Dockerfile
# AUTHOR: Sutharsan Rajaratnam
# PROJECT: The Dockerfile for the Django reference/template project: 'ref_simple' 
# PURPOSE: Build Debian image with specified Python version.

# syntax=docker/dockerfile:1
FROM python:3.9.10-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set the initial image "default" directory.
WORKDIR /project
# Copy file from host machine to image.
COPY requirements.txt /project/
#* Enable venv and install Python packages.
#** Activate Python virtual environment to install Django & other dependencies in isolation (non-global) via pip..
ENV VIRTUAL_ENV=/py_venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#** Using the file 'requirements.txt', install the listed packages via pip.
RUN pip install -r requirements.txt
# Switch "default" directory to the 'django' sub directory.
WORKDIR /project/django

