import numpy as np
import cv2

img = cv2.imread(r"D:\user\Desktop\for_school\artificial_intelligence\HW1\HW1\data\detect\02.jpg")

obj = {"face": [720, 70, 120, 120]}

cv2.rectangle(img, (obj["face"][0], obj["face"][1]), (obj["face"][2]+obj["face"][0], obj["face"][3]+obj["face"][1]), (0, 255, 0), 2)
# cv2.rectangle(img, (obj['dog'][0], obj['dog'][1]), (obj['dog'][2], obj['dog'][3]), (0, 255, 255), 2)

# cv2.putText(img,"Bunny Girl Senpai",(obj["Bunny Girl Senpai"][0], obj["Bunny Girl Senpai"][1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0,255,0),2,cv2.LINE_AA)
# cv2.putText(img,"dog",(obj['dog'][0], obj['dog'][1]), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,255),1,cv2.LINE_AA)

cv2.imshow("Window", img)
cv2.waitKey(0)