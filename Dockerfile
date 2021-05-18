FROM python:3.8.5
WORKDIR /Tubra_Docker
env PYTHONDONTWRITEBYTECODE 1
env PYTHONUNBUFFERED 1
RUN apt update && apt -y install netcat gcc postgres && apt clean
RUN apt install -y binutils libproj-dev gdal-bin python3-gdal python-gdal
RUN pip install --upgrade pip
COPY ./requirements.txt /Tubra_Docker/requirements.txt
RUN pip install -r requirements.txt 
COPY . /Tubra_Docker

