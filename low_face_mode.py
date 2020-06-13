# dim the computer screen when not looking at it with opencv

from cv2 import cv2
import osascript


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
eye_cascade = cv2.CascadeClassifier("data/haarcascade_eye.xml")

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

    if frames > 240:
        if dimmed == False:
            if 1 not in face_counter[frames - 20 : frames]:
                dim()
                dimmed = True

        if dimmed == True:
            if 1 in face_counter[frames - 20 : frames]:
                brighten()
                dimmed = False

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow("Low Face Mode On", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
