import numpy as np
import cv2


def pre_process_img(img):
    # if color img, convert to gray
    gray = cv2.cvtColor(src=np.array(img), code=cv2.COLOR_BGR2GRAY)

    # resize the image - making the image bigger for better pixel visibility to get better results
    resized_img = cv2.resize(src=gray, dsize=None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    processed_img = cv2.adaptiveThreshold(src=resized_img,
                                          maxValue=255,
                                          adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          thresholdType=cv2.THRESH_BINARY,
                                          blockSize=61,
                                          C=11)
    return processed_img
