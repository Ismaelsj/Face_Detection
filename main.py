import cv2

def face_cam():
    cap = cv2.VideoCapture(0)
    while(True):
            # Get pix array
        ret, frame = cap.read()
        if ret == False:
            print("Error: no video capture found.")
            break
            # Convert BGR to Ggrayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Load classifier
        lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascades/lbpcascade_frontalface_improved.xml')
            # Detect object
        faces = lbp_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            # Draw rectangle around object
        for (x, y ,w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
        cv2.imshow('frame', frame)
            # Use "esc" to escape
        if cv2.waitKey(1) == 27:
            break

face_cam()
