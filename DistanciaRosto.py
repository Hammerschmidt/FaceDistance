# import the necessary packages
import cv2
import math
import sys

dist = 0.0
fonte = cv2.FONT_HERSHEY_SIMPLEX

#video_capture = cap
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame

    #image = huge_frame
    ret, image = video_capture.read()
    # load the input image and convert it to grayscale
    #image = cv2.imread(args["image"])

    # Create the greyscale and detect faces
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
	minNeighbors=5)

    # loop over the face and draw a rectangle surrounding each
    for (i, (x, y, w, h)) in enumerate(rects):
	    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	    cv2.putText(image, "Rosto #{}".format(i + 1), (x, y - 10),
		fonte, 0.55, (0, 0, 255), 2)
            distance = ((2 * 3.14 * 180)/(w + h * 360) * 1000 + 3) * 2.54
            distance = math.floor(distance)

    # show the faces
    cv2.putText(image,'Distancia = ' + str(dist), (5,100), fonte, 0.55, (0, 0, 255), 2)
    cv2.imshow("Distância", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


