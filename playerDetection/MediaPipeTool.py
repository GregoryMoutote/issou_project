import mediapipe as mp
from math import *
import cv2
import numpy as np
from calibration.CalibrationTool import *

class MediaPipeTool :
    def __init__(self):

        self.calibr_util = CalibrationTool()

        self.cap = cv2.VideoCapture(0)
        self.leftHand = ()
        self.rightHand = ()
        self.isFistClosed = 0


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

                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width * 1920/800

                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height * 1080/600

                    #CALIBRAGE
                    calibrated_coord = self.calibr_util.calibratePoint((hand_x,hand_y))
                    hand_x = calibrated_coord[0]
                    hand_y = calibrated_coord[1]

                    # print((hand_x,hand_y))
                    distanceIndexExtremities = sqrt(
                        (hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y -
                         hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y) ** 2 +
                        (hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x -
                         hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x) ** 2)
                    distanceMiddleExtremities = sqrt(
                        (hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y -
                         hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y) ** 2 +
                        (hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x -
                         hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x) ** 2)
                    distanceRingExtremities = sqrt(
                        (hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y -
                         hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y) ** 2 +
                        (hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x -
                         hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x) ** 2)
                    distancePinkyExtremities = sqrt(
                        (hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y -
                         hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y) ** 2 +
                        (hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x -
                         hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x) ** 2)
                    wristX = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x
                    wristY = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y
                    distanceIndexWrist = sqrt(
                        (wristY - hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y) ** 2 +
                        (wristX - hand.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x) ** 2)
                    distanceMiddleWrist = sqrt(
                        (wristY - hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y) ** 2 +
                        (wristX - hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x) ** 2)
                    distanceRingWrist = sqrt(
                        (wristY - hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y) ** 2 +
                        (wristX - hand.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x) ** 2)
                    distancePinkyWrist = sqrt(
                        (wristY - hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y) ** 2 +
                        (wristX - hand.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x) ** 2)
                    numberOfFingersClosed = 0
                    if distanceIndexExtremities * 1.5 < distanceIndexWrist:
                        numberOfFingersClosed += 1
                    if distanceMiddleExtremities * 1.5 < distanceMiddleWrist:
                        numberOfFingersClosed += 1
                    if distanceRingExtremities * 1.5 < distanceRingWrist:
                        numberOfFingersClosed += 1
                    if distancePinkyExtremities * 1.5 < distancePinkyWrist:
                        numberOfFingersClosed += 1
                    if numberOfFingersClosed >= 3:
                        self.isFistClosed = 1
                    else:
                        self.isFistClosed = 0

                    if resultsHand.multi_handedness[num].classification[0].label == "Right":
                        if self.isFistClosed == 1:
                            self.rightHand = (hand_x,hand_y)
                        else:
                            self.rightHand = (-1, -1)
                    if resultsHand.multi_handedness[num].classification[0].label == "Left":
                        if self.isFistClosed == 1:
                            self.leftHand = (hand_x,hand_y)
                        else:
                            self.leftHand = (-1, -1)
                    if self.isFistClosed == 1:
                        result.append((hand_x,hand_y))
                    else:
                        result.append((-1, -1))
            return result

    def closeCamera(self):
        self.cap.release()