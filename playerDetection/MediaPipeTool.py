import mediapipe as mp
from math import *
import cv2
import numpy as np
from calibration.CalibrationTool import *
import ctypes

class MediaPipeTool :
    def __init__(self):

        self.calibr_util = CalibrationTool()

        #self.cap = cv2.VideoCapture(701)
        self.cap = cv2.VideoCapture(0)

        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.leftHand = ()
        self.rightHand = ()
        self.isFistClosed = 0
        self.hand_points = []


    def setUpCalibration(self):
        _,img=self.cap.read()
        return self.calibr_util.setup(img)


    def initHandCapture(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)


    def hand_detection(self):
        if self.cap.isOpened():
            ret,frame = self.cap.read()

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

                    screen = ctypes.windll.user32
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * screen.GetSystemMetrics(1)

                    self.closed_fist_detection(hand)

                    if resultsHand.multi_handedness[num].classification[0].label == "Right":
                        self.rightHand = (hand_x, hand_y)
                    if resultsHand.multi_handedness[num].classification[0].label == "Left":
                        self.leftHand = (hand_x, hand_y)
                    result.append((self.calibr_util.calibratePoint((hand_x, hand_y))))
            return result

    def complete_hand_detection(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            image.flags.writeable = False

            resultsHand = self.hands.process(image)
            screen = ctypes.windll.user32

            image_height, image_width, _ = image.shape

            result = []
            self.leftHand = ()
            self.rightHand = ()
            if resultsHand.multi_hand_landmarks:
                for num, hand in enumerate(resultsHand.multi_hand_landmarks):

                    self.closed_fist_detection(hand)

                    self.hand_points.clear()

                    screen = ctypes.windll.user32
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * screen.GetSystemMetrics(1)
                    self.hand_points.append((screen.GetSystemMetrics(0)-hand_x, hand_y))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * screen.GetSystemMetrics(1)
                    self.hand_points.append((screen.GetSystemMetrics(0)-hand_x, hand_y))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * screen.GetSystemMetrics(1)
                    self.hand_points.append((screen.GetSystemMetrics(0)-hand_x, hand_y))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * screen.GetSystemMetrics(1)
                    self.hand_points.append((screen.GetSystemMetrics(0)-hand_x, hand_y))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.WRIST].x * screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.WRIST].y * screen.GetSystemMetrics(1)
                    self.hand_points.append((screen.GetSystemMetrics(0)-hand_x, hand_y))
                    result.extend(self.hand_points)
                    print(self.hand_points[0][0])
            return result

    def closeCamera(self):
        self.cap.release()

    def closed_fist_detection(self, hand):
        numberOfFingersClosed = 0

        wrist_x = hand.landmark[self.mp_hands.HandLandmark.WRIST].x
        wrist_y = hand.landmark[self.mp_hands.HandLandmark.WRIST].y
        distanceIndexWrist = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x) ** 2)
        distanceMiddleWrist = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x) ** 2)
        distanceRingWrist = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x) ** 2)
        distancePinkyWrist = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x) ** 2)
        distanceIndexExtremities = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x) ** 2)
        distanceMiddleExtremities = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x) ** 2)
        distanceRingExtremities = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x) ** 2)
        distancePinkyExtremities = sqrt(
            (wrist_y - hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y) ** 2 +
            (wrist_x - hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x) ** 2)
        if distanceIndexExtremities < distanceIndexWrist:
            numberOfFingersClosed += 1
        if distanceMiddleExtremities < distanceMiddleWrist:
            numberOfFingersClosed += 1
        if distanceRingExtremities < distanceRingWrist:
            numberOfFingersClosed += 1
        if distancePinkyExtremities < distancePinkyWrist:
            numberOfFingersClosed += 1
        if numberOfFingersClosed >= 3:
            self.isFistClosed = 1
        else:
            self.isFistClosed = 0

    def other_closed_fist_detection(self, hand):
        numberOfFingersClosed = 0

        if hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x \
                or \
                hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x:
            numberOfFingersClosed += 1
        if hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x \
                or \
                hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x:
            numberOfFingersClosed += 1
        if hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x \
                or \
                hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x:
            numberOfFingersClosed += 1
        if hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].y \
                or \
                hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x <= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x \
                or \
                hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x >= \
                hand.landmark[self.mp_hands.HandLandmark.WRIST].x:
            numberOfFingersClosed += 1
        if numberOfFingersClosed >= 3:
            self.isFistClosed = 1
        else:
            self.isFistClosed = 0