import os

import cv2
from flask import Flask, Response, render_template, jsonify, request, make_response
from cam import Camera
import datetime as dt
import logging
from pathlib import Path

app = Flask(__name__)

cam = Camera()

parent_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(parent_path, 'static', 'images')

logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler('test.log') # creates handler for the log file
logger.addHandler(handler)

logger.info('ParentPath' + parent_path)

if not os.path.exists(image_path):
    os.mkdir(image_path)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed', methods=['GET'])
def video_feed():
    global cam
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


@app.route('/list_images', methods=['GET'])
def list_images():
    #files = os.listdir(image_path)
    files = [s for s in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, s))]
    files.sort(key=lambda s: os.path.getmtime(os.path.join(image_path, s)), reverse=True)

    files = [os.path.join('/static/images', i) for i in files]
    data = {'data':files}
    return jsonify(data)


@app.route('/delete', methods= ['POST'])
def delete():
    file = os.path.basename(request.form.get('img'))
    path = os.path.join(image_path, file)
    os.remove(path)
    return  jsonify({'img': path})
if __name__ == '__main__':





    app.run(host='0.0.0.0', port=7007, threaded=True)