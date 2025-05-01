import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('pose.mp4')

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

ptime = 0

while True:
    success , img = cap.read()
    img = cv2.resize(img , (500,500))
    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks :
        mpDraw.draw_landmarks(img , results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id , lm in enumerate(results.pose_landmarks.landmark):
            h , w ,c = img.shape
            print(id ,lm)
            cx , cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img , (cx,cy), 10 ,(255,0,0) , cv2.FILLED)


    cv2.imshow("Image" , img)

    ctime = time.time()
    fps = 1/(ctime - ptime)
    ptime = ctime

    cv2.putText(img , str(int(fps)) , (70,50) , cv2.FONT_HERSHEY_PLAIN , 3 , (255, 0 ,0) , 3)

    if cv2.waitKey(1) == 27:
        break