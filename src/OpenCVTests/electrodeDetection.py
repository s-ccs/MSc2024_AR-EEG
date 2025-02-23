import cv2
import numpy as np
import time

def process_image(img_rgb, template, count):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.3
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # This will write different res.png for each frame. Change this as you require
    cv2.imshow('Detected',img_rgb)
    #cv2.imwrite('res{0}.png'.format(count),img_rgb)


def main():
    vidcap = cv2.VideoCapture(0)
    if not vidcap.isOpened():
        print("Cannot open camera")
        exit()

    template = cv2.imread('H:\\GitLab\\BSc2024_AR-EEG\\src\\OpenCVTests\\ref.png',0)  # open template only once
    count = 0

    while True:
        success,image = vidcap.read()
        if not success: break         # loop and a half construct is useful
        print ('Read a new frame: ', success)
        process_image(image, template, count)
        count += 1

        if cv2.waitKey(1) == ord('q'):
            break

        time.sleep(0.1)

main()