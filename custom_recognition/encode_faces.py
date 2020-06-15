"""
Program taken and modified from https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
I do not make any claim over this content, which is property of Adrian Rosebrock.
Please do not reproduce commercially without permission from the author.
"""

from imutils import paths
import face_recognition
import pickle
import cv2
import os

def encode_images():
    # grab the paths to the input images in our dataset
    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images("custom_recognition/dataset"))
    # initialize the list of known encodings and known names
    knownEncodings = []
    knownNames = []

    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
        name = imagePath.split(os.path.sep)[-2]
        # load the input image and convert it from BGR (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb, model="hog")
        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)
        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and encodings
            knownEncodings.append(encoding)
            knownNames.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("custom_recognition/encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()
