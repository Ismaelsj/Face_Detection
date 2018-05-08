import cv2

def face_detection():
    cap = cv2.VideoCapture(0)
    while(True):
            # Get pix array
        ret, frame = cap.read()
        if ret == False:
            print("Error: no video found.")
            break
            # Convert BGR to Ggrayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Load classifier
        face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
        eyes_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
            # Detect object
        faces = face_cascade.detectMultiScale(gray, 1.4, 5)
            # Draw rectangle around object face
        for (x, y ,w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Get eyes inside face
            eyes_gray = gray[y: y + h, x: x + w]
            eyes_color = frame[y: y + h, x: x + w]
            eyes = eyes_cascade.detectMultiScale(eyes_gray)
                # Draw rectangle around object eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(eyes_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
            # Show capture
        cv2.imshow('frame', frame)
            # Use "esc" to escape
        if cv2.waitKey(1) == 27:
            break

face_cam()
