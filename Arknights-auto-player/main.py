import cv2
import os
import adb
import time
import datetime

adbkit = adb.adbKit()
t = datetime.datetime.now()
tkey = t.strftime("%Y%m%d%H%M%S")
while True:
    image_name_list = [
        os.path.abspath(os.path.dirname(__file__)) + "/images/start.png",
        os.path.abspath(os.path.dirname(__file__)) + "/images/choose_op.png",
        os.path.abspath(os.path.dirname(__file__)) + "/image/end.png",
    ]
    pngpos = tkey + ".png"
    adbkit.screenshots(pngpos)
    target_img = cv2.imread(pngpos)
    for image in image_name_list:
        find_img = cv2.imread(image)
        find_height, find_width, find_channel = find_img.shape[::]
        result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > 0.5:
            print("match success!")
            pointUpLeft = max_loc
            pointLowRight = (max_loc[0] + find_width, max_loc[1] + find_height)
            pointCentre = (
                max_loc[0] + (find_width / 2),
                max_loc[1] + (find_height / 2),
            )
            adbkit.click(pointCentre)
    delcmdd = "rm " + pngpos
    os.system(delcmdd)
    time.sleep(5)
