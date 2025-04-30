# Ctrl + I for co - pilot

import cv2
import numpy as np
import mediapipe as mp

#Read image
img = cv2.imread('face.jpg')

#Media pipe processes images in RGB format
rgb_img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

#Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

#Process the image
result = face_mesh.process(rgb_img)  #Detects faces in the image
#finds 468 landmarks on each face 
#Returns the result inside teh result object

#WIDTH AND HEIGHT
height , width ,_ = img.shape

#LOOPING THROUGH THE DETECTED FACES AND THEIR LANDMARKS 
for facial_landmarks in result.multi_face_landmarks: #contains a list of faces detected along with their 468 landmarks
    for i in range(0,468):
        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)
        #drawing a circle on the detected point
        cv2.circle(img , (x,y) , 1 ,(100 ,100 ,0) , -1)


cv2.imshow("Image",img)
cv2.waitKey(0)