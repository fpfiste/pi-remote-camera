from flask import Flask, Response, render_template
import cv2
import datetime as dt
app = Flask(__name__)
video = cv2.VideoCapture(0)
video.set(3, 1400)
video.set(4, 1400)

@app.route('/')
def index():
    return render_template('index.html')


def gen(video):
    while True:
        success, image = video.read()

        ret, jpeg = cv2.imencode('.jpg', image)

        frame = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snap', methods=['POST'])
def snap():
    ret, frame = video.read()
    ts = dt.datetime.now()

    out = cv2.imwrite(f'../images/{str(ts)}.jpg', frame)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7007, threaded=True)