import.cv2

capture = cv2.VideoCapture(0)

face_hear_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    _, image = capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_hear_cascade.detectMultiscale(gray, 2.1, 5)


    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h),
                      (0, 255,0), 10)
        cv2.imshow("video", image)
        k = cv2.waitKey(35) & 0xFF

        if k == 27:
            break

cv2.release()