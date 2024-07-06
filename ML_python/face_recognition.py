import cv2
import os

# Check the path to the haarcascades directory
haarcascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')

if not os.path.exists(haarcascade_path):
    print(f"Error: The file {haarcascade_path} does not exist.")
else:
    # Initialize the face classifier
    face_classifier = cv2.CascadeClassifier(haarcascade_path)

    # Open the picture
    group_photo = cv2.imread('people.jpg')

    if group_photo is None:
        print("Error: The image file 'people.jpg' does not exist or cannot be read.")
    else:
        # Convert the photo to grayscale
        gray_photo = cv2.cvtColor(group_photo, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_classifier.detectMultiScale(gray_photo, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Loop through each coordinate and plot in the original picture
        for (x, y, w, h) in faces:
            cv2.rectangle(group_photo, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Show the picture in a window
        cv2.imshow('Group Photo', group_photo)

        # Wait for a key press to close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
