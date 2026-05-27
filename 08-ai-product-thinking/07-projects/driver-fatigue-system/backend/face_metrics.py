import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh


class FaceMetrics:

    def __init__(self):
        self.mesh = mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True
        )

        # eye landmark indices (MediaPipe)
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    def _ear(self, landmarks, eye):
        p1, p2, p3, p4, p5, p6 = [landmarks[i] for i in eye]

        def dist(a, b):
            return np.linalg.norm(np.array(a) - np.array(b))

        return (dist(p2, p6) + dist(p3, p5)) / (2.0 * dist(p1, p4))

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.mesh.process(rgb)

        if not results.multi_face_landmarks:
            return None, None

        lm = results.multi_face_landmarks[0].landmark

        h, w, _ = frame.shape

        landmarks = [(int(p.x * w), int(p.y * h)) for p in lm]

        left_ear = self._ear(landmarks, self.LEFT_EYE)
        right_ear = self._ear(landmarks, self.RIGHT_EYE)

        ear = (left_ear + right_ear) / 2.0

        return ear, landmarks
