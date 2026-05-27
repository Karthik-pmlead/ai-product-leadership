from insightface.app import FaceAnalysis
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from antispoof import run_antispoof
import cv2


app = FaceAnalysis()
app.prepare(ctx_id=0)


def extract_embedding(image_path):
    image = cv2.imread(image_path)

    faces = app.get(image)

    if len(faces) == 0:
        raise Exception("No face detected")

    embedding = faces[0].embedding

    return np.array(embedding)


def save_embedding(embedding, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(embedding, f)


def load_embedding(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)


def compare_embeddings(embedding1, embedding2):
    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return float(similarity)

def extract_embedding(image_path):

    image = cv2.imread(image_path)

    faces = app.get(image)

    # 🔴 ANTI-SPOOF CHECK
    is_live, reasons = run_antispoof(image, faces)

    if not is_live:
        raise Exception(
            "Liveness check failed: " + ", ".join(reasons)
        )

    if len(faces) == 0:
        raise Exception("No face detected")

    embedding = faces[0].embedding

    return np.array(embedding)
