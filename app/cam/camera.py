import cv2
import datetime as dt
from picamera2 import Picamera2

class Camera():
    def __init__(self):
        self.cam = Picamera2()
        self.width, self.height = (1920, 1080)
        self.cam.configure(self.cam.create_video_configuration({"size": (self.width, self.height), "format":'XBGR8888'}))
        self.zoom = 1

    def stream(self):
        while True:
            image = self.cam.capture_array('main')
            print(image)
            image = self.zoom_in(image)
            ret, jpeg = cv2.imencode('.jpg', image)

            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def zoom_in(self, img):
        rot_mat = cv2.getRotationMatrix2D((self.x, self.y), 0, self.zoom)
        result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

        return result

    def capture(self, path):
        frame = self.cam.capture_array()
        out = cv2.imwrite(path, frame)

        return out


