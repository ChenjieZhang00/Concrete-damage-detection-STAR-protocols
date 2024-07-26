import cv2
import numpy as np


def mosaic(images):
    # Calculate the image size after Mosaic
    h, w = images[0].shape[:2]
    mosaic_image = np.zeros((2 * h, 2 * w, 3), dtype=images[0].dtype)

    # Put four images into the four quadrants of the mosaic image
    for i in range(2):
        for j in range(2):
            img = images[i * 2 + j]
            img_h, img_w = img.shape[:2]
            mosaic_image[i * h:(i + 1) * h, j * w:(j + 1) * w] = cv2.resize(img, (w, h))

    return mosaic_image
