import cv2
import numpy as np

def mixup(image1, image2, alpha=0.2):
    lam = np.random.beta(alpha, alpha)
    mixed_image = lam * image1 + (1 - lam) * image2
    return np.clip(mixed_image, 0, 255).astype(np.uint8)
