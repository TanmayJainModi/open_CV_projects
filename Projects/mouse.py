import cv2
import numpy as np

"""def draw(event , x, y ,flags , param):
    print("x ==" ,x)
    print("y ==", y)
    print("flag == ",flags)
    print("Parameter == ",param)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img , (x,y) ,100 , (0,255,255) ,5)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img , (x,y), (x+100 , y+100) ,(912, 255, 2) ,4)

cv2.namedWindow("res")

img = np.zeros([512,512,3] ,np.uint8)*255

cv2.setMouseCallback("res", draw)

while True:
    cv2.imshow("res" , img)
    if cv2.waitKey(1) & 0xFF == 27: #esc
        break
"""

def mouse_event(event , x ,y ,flags ,param):
    print("x ==" ,x)
    print("y ==", y)
    print("flag == ",flags)
    print("Parameter == ",param)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x ,',' ,y)
        cord = '. ' + str(x) + ', ' + str(y)
        cv2.putText(img , cord ,(x,y) , font , 1 ,(155, 23, 21) ,2)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(x ,',' ,y)

        b = img[y , x, 0]
        g = img[y,x, 1]
        r = img[y, x ,2]

        color_bgr = ". " + str(b) + ", " + str(g) + ", " + str(r)
        cv2.putText(img , color_bgr ,(x,y) , font , 1 ,(15, 23, 21) ,2)

cv2.namedWindow(winname="res")

img = np.zeros((512 , 512 ,3) , np.uint8)*255
cv2.setMouseCallback("res" , mouse_event)

while True:
    cv2.imshow("res" , img)
    if cv2.waitKey(1) & 0xFF == 27: #esc
        break

cv2.destroyAllWindows()