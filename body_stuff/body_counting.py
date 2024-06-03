import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

pose_landmark_spec = mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4)
pose_connection_spec = mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)

cap = cv2.VideoCapture(0)

body_detected = False
body_count = 0
frame_without_body = 0

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = holistic.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                      pose_landmark_spec, pose_connection_spec)
            frame_without_body = 0
            if not body_detected:
                body_detected = True
                body_count += 1
        else:
            frame_without_body += 1
            if frame_without_body > 10:
                body_detected = False

        cv2.putText(image, f'Contagem de Corpos: {body_count}',
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 0),
                    2,
                    cv2.LINE_AA)

        cv2.imshow('Retorno', image)

        if cv2.waitKey(1) & 0xFF == ord('k'):
            break

cap.release()
cv2.destroyAllWindows()
