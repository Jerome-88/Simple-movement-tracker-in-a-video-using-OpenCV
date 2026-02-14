import cv2
import numpy as np
'''
img=cv2.imread("bangun.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_hue =np.array([65,0,0])
upper_hue=np.array([120,255,255])

mask=cv2.inRange(hsv,lower_hue,upper_hue)

result=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("img",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
ball=[]

cap=cv2.VideoCapture("videobola.mp4")
out= cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc('M','J','P','G'),30,(1920,1080))

while cap.isOpened():
    ret,frame = cap.read()
    if ret is False:
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_hue=np.array([21,0,0])
    upper_hue=np.array([45,255,255])
    mask=cv2.inRange(hsv,lower_hue,upper_hue)

    (contours,_)=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    center=None
    
    if len(contours)>0:
        c=max(contours, key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        n=cv2.moments(c)
        try:
            center=(int(n["m10"]/n["m00"]),int(n["m01"]/n["m00"]))
            cv2.circle(frame,center,10,(255,0,0),-1)
            ball.append(center)
        except:
            pass
    if len(ball)>2:
        for i in range(1,len(ball)):
            cv2.line(frame,ball[i-1],ball[i],(0,0,255),5)
    out.write(frame)
out.release()

