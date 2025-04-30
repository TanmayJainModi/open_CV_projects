import cv2
import mediapipe as mp
import pyautogui as py

x1 = y1 = x2 = y2 = 0
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()  #detecting hands in webcam
drawing_utils = mp.solutions.drawing_utils  #drawing detected hand landmarks on screen

while True:
    ret ,frame = webcam.read()
    frame = cv2.flip(frame ,1)
    frame_height , frame_width ,_ = frame.shape
    rgb_image = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image) #processes the image passed and returns the info detected in an object output
    hands = output.multi_hand_landmarks  #This gives you the list of hand landmarks detected in the frame.
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id ==8 :
                    cv2.circle(img = frame , center=(x,y) , radius= 8 ,color=(0,55 ,25) , thickness=3)
                    x1 = x
                    y1 = y
                elif id ==4 :
                    cv2.circle(img = frame , center=(x,y) , radius= 8 ,color=(25, 0, 25) , thickness=3)
                    x2 = x
                    y2 = y
        dist = (((x2-x1)**2 + (y2-y1)**2)**(0.5))/4
        cv2.line(frame , (x1 , y1) , (x2,y2) , (0,255,255) ,5)
        if dist < 30:
            py.press("volumedown")
        else:
            py.press("volumeup")

    cv2.imshow("hand volume control using python", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()