import PIL
import cv2
from PIL.Image import Image
import datetime as dt

class Camera():
    def __init__(self, video):
        self.cam = video
        self.width, self.height = (1400, 1400)
        self.cam.set(3, self.width)
        self.cam.set(4, self.height)
        self.y = self.height / 2
        self.x = self.width / 2
        self.zoom = 1

    def stream(self):
        while True:
            success, image = self.cam.read()

            image = self.zoom_in(image)
            ret, jpeg = cv2.imencode('.jpg', image)

            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def zoom_in(self, img):
        rot_mat = cv2.getRotationMatrix2D((self.x, self.y), 0, self.zoom)
        result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

        return result
    # def zoom_in(self, img, coord=None):
    #     """
    #     Simple image zooming without boundary checking.
    #     Centered at "coord", if given, else the image center.
    #
    #     img: numpy.ndarray of shape (h,w,:)
    #     zoom: float
    #     coord: (float, float)
    #     """
    #     # Translate to zoomed coordinates
    #     h, w, _ = [self.zoom * i for i in img.shape]
    #
    #     if coord is None:
    #         cx, cy = w / 2, h / 2
    #     else:
    #         cx, cy = [self.zoom * c for c in coord]
    #
    #     img = cv2.resize(img, (0, 0), fx=self.zoom, fy=self.zoom)
    #     img = img[int(round(cy - h / self.zoom * .5)): int(round(cy + h / self.zoom * .5)),
    #           int(round(cx - w / self.zoom * .5)): int(round(cx + w / self.zoom * .5)),:]
    #
    #     return img

    def capture(self, path):
        ret, frame = self.cam.read()
        ts = dt.datetime.now()

        out = cv2.imwrite(path, frame)

        return out


