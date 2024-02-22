import cv2
import datetime
import  math
from constants import Radius
from constants import centre
from constants import colors


def get_ticks():
    hours_i=[]
    hours_f=[]

    for i in range(0,360,6):
        x_coordinate=int(centre[0] + Radius * math.cos(i*math.pi/180))
        y_coordinate = int(centre[1] + Radius * math.sin(i * math.pi / 180))
        hours_i.append((x_coordinate,y_coordinate))

    for i in range(0, 360, 6):

        x_coordinate = int(centre[0] + (Radius-20) * math.cos(i * math.pi / 180))
        y_coordinate = int(centre[1] + (Radius-20) * math.sin(i * math.pi / 180))
        hours_f.append((x_coordinate, y_coordinate))
    return  hours_i, hours_f

def getDigitalTime(h,m,s):


	time = ""
	hour = ""
	minute = ""
	second = ""
	if(h<10):
		hour = "0{}:".format(h)
	else:
		hour = "{}:".format(h)
	if(m<10):
		minute = "0{}:".format(m)
	else:
		minute = "{}:".format(m)
	if(s<10):
		second = "0{}".format(s)
	else:
		second = "{}".format(s)
	time = hour+minute+second
	return time

def draw_time(image):

    time_now=datetime.datetime.now().time()
    hour = math.fmod(time_now.hour,12)
    minute = time_now.minute
    second = time_now.second

    second_angle= math.fmod(second * 6 + 270 ,360)
    minute_angle=math.fmod(minute * 6+ 270 ,360)
    hour_angle=math.fmod((hour*30)+(minute/2) + 270 ,360)

    second_x=int(centre[0] + (Radius-25) * math.cos(second_angle * math.pi/180))
    second_y = int(centre[1] + (Radius - 25) * math.sin(second_angle * math.pi / 180))
    cv2.line(image,centre,(second_x,second_y),colors["black"],2)

    minute_x = int(centre[0] + (Radius - 60) * math.cos(minute_angle * math.pi / 180))
    minute_y = int(centre[1] + (Radius - 60) * math.sin(minute_angle * math.pi / 180))
    cv2.line(image, centre, (minute_x, minute_y), colors["red"],3)

    hour_x = int(centre[0] + (Radius-100) * math.cos(hour_angle * math.pi/180))
    hour_y = int(centre[1] + (Radius - 100) * math.sin(hour_angle * math.pi / 180))
    cv2.line(image,centre,(hour_x,hour_y),colors["green"],7)

    cv2.circle(image,centre,5,colors["dark_gray"],-1)
    time = getDigitalTime(int(hour), int(minute),int (second))
    cv2.putText(image,time,(200,390),cv2.FONT_HERSHEY_TRIPLEX,1.6,colors["red"],1,cv2.LINE_AA)
    return image




