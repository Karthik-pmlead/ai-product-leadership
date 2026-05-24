import cv2
import numpy as np

# ----------------------------
# BLUR CHECK
# ----------------------------
def is_blurry(image, threshold=80):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance < threshold, variance


# ----------------------------
# BRIGHTNESS CHECK
# ----------------------------
def is_too_dark_or_bright(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean = np.mean(gray)
    return mean < 40 or mean > 220, mean


# ----------------------------
# FACE SIZE CHECK
# ----------------------------
def is_face_too_small(face_bbox, image_shape):
    x1, y1, x2, y2 = face_bbox
    face_area = (x2 - x1) * (y2 - y1)
    img_area = image_shape[0] * image_shape[1]

    ratio = face_area / img_area
    return ratio < 0.05, ratio


# ----------------------------
# MAIN CHECK PIPELINE
# ----------------------------
def run_antispoof(image, faces):
    """
    Returns:
    - is_live (bool)
    - reasons (list)
    """

    reasons = []

    # Blur check
    blurry, blur_score = is_blurry(image)
    if blurry:
        reasons.append(f"Image too blurry ({blur_score:.2f})")

    # Brightness check
    bad_light, brightness = is_too_dark_or_bright(image)
    if bad_light:
        reasons.append(f"Bad lighting ({brightness:.2f})")

    # Face presence
    if len(faces) == 0:
        reasons.append("No face detected")
        return False, reasons

    # Face size check
    bbox = faces[0].bbox.astype(int)
    small, ratio = is_face_too_small(bbox, image.shape)

    if small:
        reasons.append(f"Face too small ({ratio:.3f})")

    is_live = len(reasons) == 0

    return is_live, reasons
