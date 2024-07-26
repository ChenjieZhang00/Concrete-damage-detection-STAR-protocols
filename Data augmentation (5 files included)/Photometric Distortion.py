import cv2
import numpy as np


def photometric_distortion(image):
    # Brightness adjustment
    delta = np.random.uniform(-32, 32)
    image = image + delta

    # Contrast adjustment
    alpha = np.random.uniform(0.5, 1.5)
    image = image * alpha

    # Saturation adjustment
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_hsv[:, :, 1] = image_hsv[:, :, 1] * np.random.uniform(0.5, 1.5)
    image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    # Hue adjustment
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_hsv[:, :, 0] = (image_hsv[:, :, 0] + np.random.uniform(-18, 18)) % 180
    image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    return np.clip(image, 0, 255).astype(np.uint8)
