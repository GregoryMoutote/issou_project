import mediapipe as mp
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

        self.screen = ctypes.windll.user32


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

            self.leftHand = ()
            self.rightHand = ()
            if resultsHand.multi_hand_landmarks:
                for num, hand in enumerate(resultsHand.multi_hand_landmarks):

                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * self.screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * self.screen.GetSystemMetrics(1)

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
                        self.rightHand = self.calibr_util.calibratePoint((hand_x, hand_y))
                    if resultsHand.multi_handedness[num].classification[0].label == "Left":
                        self.leftHand = self.calibr_util.calibratePoint((hand_x, hand_y))

    def complete_hand_detection(self):
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

                    self.hand_points.clear()

                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * self.screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * self.screen.GetSystemMetrics(1)
                    self.hand_points.append((self.calibr_util.calibratePoint((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * self.screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * self.screen.GetSystemMetrics(1)
                    self.hand_points.append((self.calibr_util.calibratePoint((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * self.screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * self.screen.GetSystemMetrics(1)
                    self.hand_points.append((self.calibr_util.calibratePoint((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * self.screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * self.screen.GetSystemMetrics(1)
                    self.hand_points.append((self.calibr_util.calibratePoint((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.WRIST].x * self.screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.WRIST].y * self.screen.GetSystemMetrics(1)
                    self.hand_points.append((self.calibr_util.calibratePoint((hand_x, hand_y))))
                    result.extend(self.hand_points)
            return result

    def closeCamera(self):
        self.cap.release()