import cv2 as cv
import mediapipe as mp

class HandTracker:
    def __init__(self, mode=False, max_hands=1, complexity=1,
                 detection_confidence = 0.5, tracking_confidence = 0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        self.mp_hands = mp.solutions.hands
        self.hand = self.mp_hands.Hands(self.mode, self.max_hands, self.complexity,
                                       self.detection_confidence, self.tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils


    def detect(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.result = self.hand.process(imgRGB)
        if self.result.multi_hand_landmarks:
            for landmarks in self.result.multi_hand_landmarks:
                if draw:
                     self.mp_draw.draw_landmarks(img, landmarks, self.mp_hands.HAND_CONNECTIONS)
        return img


    def find_postion(self, img, handID = 0):
        positions = []
        if self.result.multi_hand_landmarks:
            target_hand = self.result.multi_hand_landmarks[handID]
            for id, landmark in enumerate(target_hand.landmark):
                height, width, channel = img.shape
                x = int(landmark.x * width)
                y = int(landmark.y * height)
                positions.append([id, x, y])
        return positions