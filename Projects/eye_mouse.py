import cv2
import mediapipe as mp
import pyautogui

camera = cv2.VideoCapture(0)
face_mesh_landmarks = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w , screen_h = pyautogui.size()

while True:
    _ , frame = camera.read() 
    frame = cv2.flip(frame,1)
    window_h , window_w ,_= frame.shape
    rgb_image = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    processed_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks
    if all_face_landmark_points :
        one_face_landmark_points = all_face_landmark_points[0].landmark
        for id,landmark_point in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            
            if(id == 1):
                mouse_x = int(screen_w/window_w * x)
                mouse_y = int(screen_h/window_h * y)
                pyautogui.moveTo(mouse_x,mouse_y)

            cv2.circle(frame , (x,y) ,3 ,(0,0,255))
        left_eye = [one_face_landmark_points[145],one_face_landmark_points[159]]
        for landmark_point in left_eye:
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            cv2.circle(frame , (x,y) ,3 ,(0,0,255))
        if(left_eye[0].y - left_eye[1].y < 0.01):
            pyautogui.click()
            pyautogui.sleep(2)
            print("mouse clicked")

    cv2.imshow("eye_mouse" , frame)
    if cv2.waitKey(100) == 27:
        break

camera.release()
cv2.destroyAllWindows()