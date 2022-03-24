import mediapipe as mp
from Calibration.CalibrationTool import *
from Model.ScreenData import ScreenData


class MediapipeTool :
    def __init__(self):

        self.isMocker = True

        try :
            self.calibration_util = CalibrationTool()
            self.isMocker = False
        except:
            self.isMocker = True

        #self.cap = cv2.VideoCapture(701)

        try :
            self.cap = cv2.VideoCapture(0)
            self.isMocker = False
        except:
            self.isMocker = True


        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.left_hand = ()
        self.right_hand = ()
        self.is_fist_closed = 0
        self.hand_points = []

        self.screen = ScreenData()


    """
    Met en place le calibrage
    """
    def set_up_calibration(self):
        _, img = self.cap.read()
        return self.calibration_util.setup(img)

    """
    Définit le paramètre de la détection des mains
    """
    def init_hand_capture(self):
        if not self.isMocker:
            self.mp_hands = mp.solutions.hands
            self.hands = self.mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

    """
    Calcule les coordonnées des mains et rempli les attributs left_hand et right_hand
    """
    def hand_detection(self):
        if not self.isMocker and self.cap.isOpened():
            ret, frame = self.cap.read()


            frame = self.calibration_util.calibrate_picture(frame, False)

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            image.flags.writeable = False

            results_hand = self.hands.process(image)

            image_height, image_width, _ = image.shape

            self.left_hand = ()
            self.right_hand = ()
            if results_hand.multi_hand_landmarks:
                for num, hand in enumerate(results_hand.multi_hand_landmarks):

                    hand_x = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * self.screen.width
                    hand_y = hand.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * self.screen.height

                    self.closed_fist_detection(hand)

                    if results_hand.multi_handedness[num].classification[0].label == "Right":
                        #self.right_hand = self.calibration_util.calibrate_point((hand_x, hand_y))
                        if self.calibration_util.is_done:
                            self.right_hand = (self.screen.width-hand_x, hand_y)
                        else:
                            self.right_hand = (hand_x, hand_y)

                    if results_hand.multi_handedness[num].classification[0].label == "Left":
                        #self.left_hand = self.calibration_util.calibrate_point((hand_x, hand_y))
                        if self.calibration_util.is_done:
                            self.left_hand = (self.screen.width-hand_x, hand_y)
                        else:
                            self.left_hand = (hand_x, hand_y)


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

                    screen_width = self.screen.width
                    screen_height = self.screen.height

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

    """
    Ferme la caméra
    """
    def close_camera(self):
        if not self.isMocker:
            self.cap.release()

    """
    Redémarre la caméra
    """
    def reopen_camera(self):
        if not self.isMocker:
            self.cap = cv2.VideoCapture(0)

    """
    Vérifie si la main est ouverte ou fermée et rempli l'attribut is_fist_closed
    """
    def closed_fist_detection(self, hand):
        if not self.isMocker:

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