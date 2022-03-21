#Read image / camera / video input



import cv2 
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640) 
cap.set(4, 480)
used_codes = []
camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        print(code.type)
        print(code.data.decode('utf-8'))
    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)
