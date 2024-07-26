import cv2
import numpy as np


def geometric_distortion(image, boxes):
    h, w = image.shape[:2]

    # Rotate
    angle = np.random.uniform(-10, 10)
    M_rot = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    image = cv2.warpAffine(image, M_rot, (w, h))

    # Translation
    x_trans = np.random.uniform(-0.1, 0.1) * w
    y_trans = np.random.uniform(-0.1, 0.1) * h
    M_trans = np.float32([[1, 0, x_trans], [0, 1, y_trans]])
    image = cv2.warpAffine(image, M_trans, (w, h))

    # Zoom
    scale = np.random.uniform(0.8, 1.2)
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    # Horizontal flip
    if np.random.rand() > 0.5:
        image = cv2.flip(image, 1)

    return image, boxes
