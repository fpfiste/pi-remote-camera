# syntax=docker/dockerfile:1

<<<<<<< HEAD
FROM balenalib/raspberry-pi-debian:latest
=======
FROM python:3.11-slim-bullseye
RUN apt-get install -y git
RUN git clone https://git.libcamera.org/libcamera/libcamera.git
RUN cd libcamera
RUN meson setup build
RUN ninja -C build install

>>>>>>> 7257167 (add app)

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