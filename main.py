import cv2 as cv
import HandTracker


capture = cv.VideoCapture(0)
handTracker = HandTracker.HandTracker()

while True:
    success, img = capture.read()
    img = cv.flip(img,1)
    img = handTracker.detect(img)
    positions = handTracker.find_postion(img)
    if len(positions) > 0:
        print (positions[8])
    cv.imshow("Camera", img)
    cv.waitKey(1)

    if cv.getWindowProperty("Camera", cv.WND_PROP_VISIBLE) < 1:
        break
capture.release()
cv.destroyAllWindows()