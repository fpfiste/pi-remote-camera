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
    if cam.x > 50:
        cam.x -= 50
    data = {'zoom':cam.x}
    return  jsonify(data)

@app.route('/mv_right', methods=['POST'])
def mv_right():
    if cam.x < (cam.width - 50):
        cam.x += 50
    data = {'zoom':cam.x}
    return  jsonify(data)


@app.route('/mv_up', methods=['POST'])
def mv_up():
    if cam.y > 50:
        cam.y -= 50
    data = {'zoom':cam.y}
    return  jsonify(data)

@app.route('/mv_down', methods=['POST'])
def mv_down():
    if cam.y < (cam.height-50):
        cam.y += 50
    data = {'zoom':cam.y}
    return  jsonify(data)

@app.route('/capture', methods=['POST'])
def capture():
    cam.capture()
    return render_template('index.html')





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7007, threaded=True)