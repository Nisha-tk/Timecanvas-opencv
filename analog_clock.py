import cv2
import numpy as np
import datetime

from constants import colors, canvas_size,Radius
from helpfunctions import get_ticks , draw_time

image= np.zeros(canvas_size,dtype=np.uint8)
image[:]=[255,255,255]

hours_i , hours_f = get_ticks()
for i in range(len(hours_i)):

    if i% 5==0:
        cv2.line(image, hours_i[i],hours_f[i],colors['black'],3)
    else:
        cv2.circle(image,hours_i[i],5,colors["gray"],-1)
cv2.circle(image,(320,320) , Radius+10 , colors["yellow"],2)
cv2.putText(image,"TITAN",(215,230),cv2.FONT_HERSHEY_TRIPLEX,2,colors["dark_gray"],1,cv2.LINE_AA)
while True:

    image_original=image.copy()
    clock_face= draw_time(image_original)
    cv2.imshow("clock",image_original)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()



