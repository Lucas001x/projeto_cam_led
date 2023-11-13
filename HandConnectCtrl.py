from cvzone.HandTrackingModule import HandDetector
import cv2
import serial

arduino = serial.Serial(port='COM12', baudrate=115200, timeout=0.1)

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False,
                        maxHands=2,
                        modelComplexity=1,
                        detectionCon=0.5,
                        minTrackCon=0.5)

# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()

    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # (x,y,z) List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

        # Count the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)
        print(f'H1 = {fingers1.count(1)}', end=" ")  # Print the count of fingers that are up

        

        if fingers1.count(1) == 4:
            arduino.write(bytes('4', 'utf-8'))
        elif fingers1.count(1) == 3:
            arduino.write(bytes('3', 'utf-8'))
        elif fingers1.count(1) == 2:
            arduino.write(bytes('2', 'utf-8'))
        elif fingers1.count(1) == 1:
            arduino.write(bytes('1', 'utf-8'))

        tipOfIndexFinger = lmList1[8][0:2]
        tipOfMiddleFinger = lmList1[12][0:2]
        # # Calculate distance between specific landmarks on the first hand and draw it on the image
        length, info, img = detector.findDistance(tipOfIndexFinger,tipOfMiddleFinger , img, color=(255, 0, 255),
                                                  scale=5)


        # Check if a second hand is detected
        if len(hands) == 2:
            # Information for the second hand
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

            # Count the number of fingers up for the second hand
            fingers2 = detector.fingersUp(hand2)
            print(f'H2 = {fingers2.count(1)}', end=" ")

            if fingers2.count(1) == 1 and fingers1.count(1) == 5:
                arduino.write(bytes('5', 'utf-8'))
            elif fingers2.count(1) == 2 and fingers1.count(1) == 5:
                arduino.write(bytes('6', 'utf-8'))
            elif fingers2.count(1) == 3 and fingers1.count(1) == 5:
                arduino.write(bytes('7', 'utf-8'))


            tipOfIndexFinger2 = lmList2[8][0:2]
            # Calculate distance between the index fingers of both hands and draw it on the image
            length, info, img = detector.findDistance(tipOfIndexFinger,tipOfIndexFinger2 , img, color=(255, 0, 0),
                                                      scale=10)

        print(" ")  # New line for better readability of the printed output

    # Display the image in a window
    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    if cv2.waitKey(1) == 13:
        cv2.destroyWindow()
