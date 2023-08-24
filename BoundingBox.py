import cv2

def BoundingBoxCoordinates():
    imagePath = 'image.jpg'
    img = cv2.imread(imagePath)
    img.shape
    height, width, _ = img.shape

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    centre_x = x + w/2
    centre_y = y + y/2

    proportioning1 = (centre_x/width)*480
    proportioning2 = (centre_y/height)*320
    
    LEx = proportioning1 - 100
    LEy = proportioning2 - 80
    REx = proportioning1 + 40
    REy = proportioning2 - 80

    eye_config = (LEx, LEy, REx, REy)
    return eye_config
    #320,480