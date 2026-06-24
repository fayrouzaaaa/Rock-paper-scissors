import cv2 as cv
import mediapipe as mp
import HandTracker as ht

class PositionDetector:
    def __init__(self, hand_tracker, img):
        self.tip_landmarks = [8,12,16,20]
        self.hand_tracker = hand_tracker
        self.img = img

    def finger_positions(self):
        fingers = []
        positions = self.hand_tracker.find_position(self.img)
        if len(positions) > 0:
            for landmark in self.tip_landmarks:
                if positions[landmark][2] < positions[landmark-2][2]:
                    fingers.append(True)
                else:
                    fingers.append(False)
        return fingers

    def hand_position(self):
        result = 'i'
        fingers = self.finger_positions()
        if len(fingers) > 0:
            if fingers[0] and fingers[1] and fingers[2] and fingers[3]:
                result = 'p'
            elif fingers[0] and fingers[1] and not(fingers[2]) and not(fingers[3]):
                result = 's'
            elif not(fingers[0]) and not(fingers[1]) and not(fingers[2]) and not(fingers[3]):
                result = 'r'
        return result
