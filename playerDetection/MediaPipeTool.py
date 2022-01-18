import mediapipe as mp
from math import *
import cv2
import numpy as np

class MediaPipeTool :
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.leftHand = ()
        self.rightHand = ()
        self.isFistClosed = 0

    def initHandCapture(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

    def hand_detection(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            image.flags.writeable = False

            resultsHand = self.hands.process(image)

            image_height, image_width, _ = image.shape

            result = []
            self.leftHand = ()
            self.rightHand = ()
            if resultsHand.multi_hand_landmarks:
                for num, hand in enumerate(resultsHand.multi_hand_landmarks):

                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width * 1920 / 800
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height * 1080 / 600

                    numberOfFingersClosed = 0

                    if hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.WRIST].y:
                        numberOfFingersClosed += 1
                    if hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.WRIST].y:
                        numberOfFingersClosed += 1
                    if hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.WRIST].y:
                        numberOfFingersClosed += 1
                    if hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y <= \
                            hand.landmark[self.mp_hands.HandLandmark.WRIST].y:
                        numberOfFingersClosed += 1

                    if numberOfFingersClosed >= 3:
                        self.isFistClosed = 1
                    else:
                        self.isFistClosed = 0

                    if resultsHand.multi_handedness[num].classification[0].label == "Right":
                        self.rightHand = (hand_x, hand_y)
                    if resultsHand.multi_handedness[num].classification[0].label == "Left":
                        self.leftHand = (hand_x, hand_y)
                    result.append((hand_x, hand_y))
            return result

    def closeCamera(self):
        self.cap.release()