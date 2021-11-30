import mediapipe as mp
import cv2
import numpy as np

class MediaPipeTool :
    def __init__(self):
        self.hand = []
    def body_detection(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        mp_pose = mp.solutions.pose
        mp_holistic = mp.solutions.holistic
        cap = cv2.VideoCapture(0)

        cap = cv2.VideoCapture(0)
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.8, min_tracking_confidence=0.8) as pose:
            with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
                while cap.isOpened():
                    ret, frame = cap.read()

                    # Recolor image to RGB
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image = cv2.flip(image, 1)
                    image.flags.writeable = False

                    # Make detection
                    resultsPose = pose.process(image)
                    resultsHand = hands.process(image)

                    # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    # Extract landmarks
                    try:
                        landmarks = resultsPose.pose_landmarks.landmark

                    except:
                        pass
                    image_height, image_width, _ = image.shape
                    # Render detections
                    #mp_drawing.draw_landmarks(image, resultsPose.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                     #                         mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                      #                        mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                       #                       )
                    self.hand = []
                    if resultsHand.multi_hand_landmarks:
                        for num, hand in enumerate(resultsHand.multi_hand_landmarks):
                            hand_x = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*image_width
                            hand_y = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*image_height
                            self.hand.append((hand_x,hand_y))
                            #mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                             #                         mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                              #                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2,
                               #                                              circle_radius=2),
                                #                      )

                    cv2.imshow('Mediapipe Feed', image)

                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()

# Initiate holistic model

"""
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        # print(results.face_landmarks)

        # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks

        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)



        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

"""

"""
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Detections
        print(results)

        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                print(mp_hands.HAND_CONNECTIONS)
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )

        # Save our image    
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
"""
"""
cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Detections
        print(results)

        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )


        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
"""
"""
mp_drawing = mp.solutions.drawing_utils

mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Raw Webcam Feed', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""