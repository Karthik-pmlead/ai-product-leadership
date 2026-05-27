import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]


def euclidean(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


def eye_aspect_ratio(lm, eye, w, h):
    pts = [(int(lm[i].x*w), int(lm[i].y*h)) for i in eye]

    A = euclidean(pts[1], pts[5])
    B = euclidean(pts[2], pts[4])
    C = euclidean(pts[0], pts[3])

    return (A + B) / (2.0 * C)


def analyze_frame(frame):
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    res = face_mesh.process(rgb)
    if not res.multi_face_landmarks:
        return None

    lm = res.multi_face_landmarks[0].landmark

    left = eye_aspect_ratio(lm, LEFT_EYE, w, h)
    right = eye_aspect_ratio(lm, RIGHT_EYE, w, h)

    return (left + right) / 2.0
