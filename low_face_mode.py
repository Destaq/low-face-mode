# dim the computer screen when not looking at it with opencv

from cv2 import cv2
import osascript
import argparse
from custom_recognition.recognize_faces_video import get_name



def dim():
    script = """
    tell application "System Events"
        repeat 32 times
            key code 145
            delay 0.02
        end repeat
    end tell
    """
    osascript.osascript(script)


def brighten():
    script = """
    tell application "System Events"
        repeat 32 times
            key code 144
            delay 0.02
        end repeat
    end tell
    """
    osascript.osascript(script)


face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

capture = cv2.VideoCapture(0)

face_counter = []
frames = 0
dimmed = False

while True:
    _, img = capture.read()
    frames += 1
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    face_counter.append(len(faces))

    users, verified_users, rec = get_name(img)

    if frames > 20:

        if dimmed == False:
            if 1 not in face_counter[frames - 20 : frames] or ((bool(set(users) & set(verified_users)) == False) and rec == True):
                dim()
                dimmed = True

        if dimmed == True:
            if rec == True:
                if set(users) & set(verified_users):
                    if 1 in face_counter[frames - 20 : frames]:
                        brighten()
                        dimmed = False
            else:
                if 1 in face_counter[frames - 20 : frames]:
                        brighten()
                        dimmed = False

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Low Face Mode On", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27 or k == 113:
        break

capture.release()
cv2.destroyAllWindows()
