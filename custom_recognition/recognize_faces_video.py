"""
Program made and modified from tutorial on https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
Adiran Rosebrock kindly provided this tutorial on custom face recognition, which I used and adapated for low-face-mode.
Please do not reproduce commercially without permission from the author.
"""

# import the necessary packages
import face_recognition
import argparse
import pickle
import time
import cv2
import imutils
from custom_recognition.build_face_dataset import create_videos
from custom_recognition.encode_faces import encode_images


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument(
    "-r", "--recognition", type=str, default = "True", help="whether custom recognition is True/False"
)

ap.add_argument(
    "-d",
    "--database",
    type=bool,
    default=False,
    help="create facial database; True/False",
)

ap.add_argument(
    "-y",
    "--yourname",
    type = str,
    default = 'none',
    help = "name used for creating custom face database, MUST be same as in --users"
)

ap.add_argument(
    "-u",
    "--users",
    type=list,
    nargs="+",
    help="list of verified users to brighten screen",
)

args = vars(ap.parse_args())

if args["database"] == True and args["recognition"] == True:
    create_videos(args["yourname"])
    encode_images()

# load the known faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open("custom_recognition/encodings.pickle", "rb").read())
# initialize the video stream and pointer to output video file, then
# allow the camera sensor to warm up
print("[INFO] starting video stream...")
time.sleep(2.0)

verified_users = []
for i in range(len(args["users"])):
    verified_users.append("".join(args["users"][i]))

# loop over frames from the video file stream
def get_name(frame):
    # grab the frame from the threaded video stream

    # convert the input frame from BGR to RGB then resize it to have
    # a width of 750px (to speedup processing)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])
    # detect the (x, y)-coordinates of the bounding boxes
    # corresponding to each face in the input frame, then compute
    # the facial embeddings for each face
    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    name = "Unknown"
    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            # determine the recognized face with the largest number
            # of votes (note: in the event of an unlikely tie Python
            # will select first entry in the dictionary)
            name = max(counts, key=counts.get)
        # update the list of names
        names.append(name)

    # check to see if we are supposed to display the output frame to
    # the screen
    result = args["recognition"]
    if result == "True" or result == "true" or result == 'y' or result == 'on':
        result = True
    elif result == "False" or result == "false" or result == "n" or result == "off":
        result = False
    return names, verified_users, result
