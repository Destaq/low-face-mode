"""
Program made and modified from tutorial on https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
Adiran Rosebrock kindly provided this tutorial on custom face recognition, which I used and adapated for low-face-mode.
Please do not reproduce commercially without permission from the author.
"""

from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os

def create_videos(name):

    detector = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

    parent_directory = os.getcwd()
    new_directory = "custom_recognition/dataset/" + str(name)
    path = os.path.join(parent_directory, new_directory)
    os.mkdir(path)


    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()

    time.sleep(2.0)
    total = 0

    while True:

        frame = vs.read()
        orig = frame.copy()
        frame = imutils.resize(frame, width=400)

        rects = detector.detectMultiScale(
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("k"):
            p = os.path.sep.join(["custom_recognition/dataset/" + str(name), "{}.png".format(str(total).zfill(5))])

            cv2.imwrite(p, orig)
            total += 1

        elif key == ord("q"):
            break

    print("[INFO] {} faces stored.".format(total))
    print("[INFO] cleaning up...")

    cv2.destroyAllWindows()
    vs.stop()
