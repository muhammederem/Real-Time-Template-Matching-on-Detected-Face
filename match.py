import cv2
from matplotlib import pyplot as plt
import numpy as np
def match(frame,template):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]

    if gray.shape[0] >= template.shape[0]:
        res = cv2.matchTemplate(gray, template, cv2.TM_SQDIFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        result = (max_val, top_left, bottom_right)
        if result[0] >= 0.98:
            print(' {:.2f}%'.format(result[0] * 100))
            cv2.rectangle(frame, top_left, bottom_right, 255, 1)
            cv2.putText(frame, 'kafa ', (top_left[0]+40, top_left[1] + 25),
                        cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255))
            return frame
    else:
        return frame