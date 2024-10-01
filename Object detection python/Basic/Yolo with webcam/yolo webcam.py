import cv2
import cvzone
from ultralytics import YOLO
import math

cam = cv2.VideoCapture(0)
cam.set(3, 500)
cam.set(4, 250)

model = YOLO("../Yolo models/yolov8n.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
"traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
"dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
"handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
"baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
"fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
"carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
"diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
"microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
"teddy bear", "hair drier", "toothbrush"
]

while True:
    success, img = cam.read()

    result = model(img, stream=True)

    for i in result:
        boxes = i.boxes
        for j in boxes:
            # x1, y1, x2, y2 = j.xyxy[0]
            # x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, w, h = int(x1), int(y1), int(x2-x1), int(y2-y1)
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((j.conf[0]*100))/100
            cls = int(j.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]}{conf}', (max(0, x1), max(50, y1-15)), thickness=1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)