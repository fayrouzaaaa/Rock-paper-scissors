import cv2 as cv
import HandTracker as ht
import PositionDetector as pd


capture = cv.VideoCapture(0)
hand_tracker = ht.HandTracker()

while True:
    success, img = capture.read()
    img = cv.flip(img,1)
    img = hand_tracker.detect(img)
    positions = hand_tracker.find_position(img)
    position_detector = pd.PositionDetector(hand_tracker, img)
    print (position_detector.hand_position())
    cv.imshow("Camera", img)
    cv.waitKey(1)

    if cv.getWindowProperty("Camera", cv.WND_PROP_VISIBLE) < 1:
        break
capture.release()
cv.destroyAllWindows()