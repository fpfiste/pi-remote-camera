import cv2
from flask import Flask, Response, render_template, jsonify, request
from cam import Camera

app = Flask(__name__)

video = cv2.VideoCapture(0)
cam = Camera(video)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
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

@app.route('/mv_left', methods=['POST'])
def mv_left():
    if cam.zoom > 1:
        cam.x -= 1
    data = {'zoom':cam.zoom}
    return  jsonify(data)

@app.route('/mv_right', methods=['POST'])
def mv_right():
    if cam.zoom < cam.width:
        cam.x += 1
    data = {'zoom':cam.zoom}
    return  jsonify(data)


@app.route('/capture', methods=['POST'])
def capture():
    cam.capture()
    return render_template('index.html')





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7007, threaded=True)