#!/bin/sh

udevadm control --reload

<<<<<<< HEAD
python3 -m flask run --host=0.0.0.0 --port=7007

=======
libcamera-hello --list-cameras -n -v
>>>>>>> 7257167 (add app)

sleep infinity