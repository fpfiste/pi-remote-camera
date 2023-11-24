# syntax=docker/dockerfile:1


FROM balenalib/raspberry-pi-debian:latest


WORKDIR /files
RUN apt-get update 
RUN apt-get upgrade


RUN apt-get install libcamera-dev libcamera-apps-lite v4l-utils
RUN apt-get install python3 python3-pip python3-opencv python3-picamera2




COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY start.sh ./

RUN chmod +x start.sh

RUN usermod -a -G video root

ENV UDEV=on

CMD ["sh","./start.sh"]
