import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

pose_landmark_drawing_spec = mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4)
pose_connection_drawing_spec = mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                pose_landmark_drawing_spec, pose_connection_drawing_spec)

            landmarks = results.pose_landmarks.landmark
            hip_left = landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value]
            hip_right = landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value]

            center_x = (hip_left.x + hip_right.x) / 2

            image_width = image.shape[1]

            if center_x > 0.5:
                cv2.putText(image, "Alerta", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Retorno', image)

        k = cv2.waitKey(1)
        if k == ord("k"):
            break

cap.release()
cv2.destroyAllWindows()
