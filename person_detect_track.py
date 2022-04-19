import cv2

filepath = "./in.mp4"

# read video
cap = cv2.VideoCapture(filepath)
while not cap.isOpened():
    cap = cv2.VideoCapture(filepath)
    cv2.waitKey(1000)
    print ("Wait for the header")
pos_frame = cap.get(1)

# handle
while True:
    flag, frame = cap.read()
    cv2.imshow("frame by frame", frame)
    # handle here

    # wait for anykey that's pressed
    cv2.waitKey(0)
    
