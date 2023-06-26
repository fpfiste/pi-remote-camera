import os

import cv2
from flask import Flask, Response, render_template, jsonify, request, make_response
from cam import Camera
import datetime as dt


app = Flask(__name__)

cam = Camera()

parent_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(parent_path, 'images')

if not os.path.exists(image_path):
    os.mkdir(image_path)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed/', methods=['GET'])
def video_feed():
    print('here')
    frame = cam.stream()
  
    return Response(cam.stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/zoom_in', methods=['POST'])
def zoom_in():
    if cam.zoom < 10:
        cam.zoom += 0.1
    data = {'zoom': cam.zoom}
    return  jsonify(data)


@app.route('/zoom_out', methods=['POST'])
def zoom_out():
    if cam.zoom > 1:
        cam.zoom -= 0.1
    data = {'zoom':cam.zoom}
    return  jsonify(data)

@app.route('/capture', methods=['POST'])
def capture():


    path = os.path.join(image_path, str(dt.datetime.now()) + '.jpg')
    cam.capture(path)
    return  jsonify({'data': path})




if __name__ == '__main__':





    app.run(host='0.0.0.0', port=7007, threaded=True)