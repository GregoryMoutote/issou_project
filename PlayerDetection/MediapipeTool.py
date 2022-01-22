import mediapipe as mp
from Calibration.CalibrationTool import *
import ctypes

class MediapipeTool :
    def __init__(self):

        self.calibration_util = CalibrationTool()


        #self.cap = cv2.VideoCapture(701)

        self.cap = cv2.VideoCapture(0)

        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.left_hand = ()
        self.right_hand = ()
        self.is_fist_closed = 0
        self.hand_points = []

        self.screen = ctypes.windll.user32


    def set_up_calibration(self):
        _, img = self.cap.read()
        return self.calibration_util.setup(img)


    def init_hand_capture(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)


    def hand_detection(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            image.flags.writeable = False

            results_hand = self.hands.process(image)

            image_height, image_width, _ = image.shape

            self.left_hand = ()
            self.right_hand = ()
            if results_hand.multi_hand_landmarks:
                for num, hand in enumerate(results_hand.multi_hand_landmarks):

                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * self.screen.GetSystemMetrics(0)
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * self.screen.GetSystemMetrics(1)

                    self.closed_fist_detection(hand)

                    if results_hand.multi_handedness[num].classification[0].label == "Right":
                        self.right_hand = self.calibration_util.calibrate_point((hand_x, hand_y))
                    if results_hand.multi_handedness[num].classification[0].label == "Left":
                        self.left_hand = self.calibration_util.calibrate_point((hand_x, hand_y))

    def complete_hand_detection(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            image.flags.writeable = False

            results_hand = self.hands.process(image)

            image_height, image_width, _ = image.shape

            result = []
            self.left_hand = ()
            self.right_hand = ()
            if results_hand.multi_hand_landmarks:
                for num, hand in enumerate(results_hand.multi_hand_landmarks):

                    self.closed_fist_detection(hand)

                    self.hand_points.clear()

                    screen_width = self.screen.GetSystemMetrics(0)
                    screen_height = self.screen.GetSystemMetrics(1)

                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * screen_width
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * screen_height
                    self.hand_points.append((self.calibration_util.calibrate_point((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * screen_width
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * screen_height
                    self.hand_points.append((self.calibration_util.calibrate_point((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * screen_width
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * screen_height
                    self.hand_points.append((self.calibration_util.calibrate_point((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * screen_width
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * screen_height
                    self.hand_points.append((self.calibration_util.calibrate_point((hand_x, hand_y))))
                    hand_x = hand.landmark[self.mp_hands.HandLandmark.WRIST].x * screen_width
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.WRIST].y * screen_height
                    self.hand_points.append((self.calibration_util.calibrate_point((hand_x, hand_y))))
                    result.extend(self.hand_points)
            return result

    def close_camera(self):
        self.cap.release()

    def closed_fist_detection(self, hand):
        number_of_fingers_closed = 0

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
            number_of_fingers_closed += 1
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
            number_of_fingers_closed += 1
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
            number_of_fingers_closed += 1
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
            number_of_fingers_closed += 1
        if number_of_fingers_closed >= 3:
            self.is_fist_closed = 1
        else:
            self.is_fist_closed = 0