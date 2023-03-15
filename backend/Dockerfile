FROM python:3.10
RUN mkdir backend
COPY ./requirements.txt /backend/
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev ffmpeg
RUN pip install -r /backend/requirements.txt
WORKDIR /backend/scripts/