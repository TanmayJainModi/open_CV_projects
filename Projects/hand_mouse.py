import cv2
import mediapipe as mp
import pyautogui

capture_hands = mp.solutions.hands.Hands()
drawing_option = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
screen_width , screen_height = pyautogui.size()

while True:
    _, image = cap.read()
    image= cv2.flip(image,1)
    image_height , image_width ,_= image.shape
    rgb_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    x1 = y1 = x2 = y2 =0
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image, hand)
            one_hand_landmark = hand.landmark
            for id ,lm in enumerate(one_hand_landmark):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                if id == 8:
                    mouse_x = (screen_width / image_width * x)
                    mouse_y = (screen_height/image_height *y)
                    cv2.circle(image , (x , y) ,10 ,( 0 ,255,255))
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(image,(x,y) ,10 , (0,0,255))
                    x2 = x
                    y2 = y
        dist= y2-y1
        if(dist<20):
            pyautogui.click()
    cv2.imshow("hand mouse" , image)


    key = cv2.waitKey(100)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()