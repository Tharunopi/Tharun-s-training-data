import cv2, math, cvzone
import numpy as np
from ultralytics import YOLO
from sort import *

mask = cv2.imread("mask_c.png")
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)
limit = [415, 297, 673, 297]
total_vechiles = []

vid = cv2.VideoCapture("cars.mp4")
vid.set(3, 1280)
vid.set(4, 720)

model = YOLO("yolov8n.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
"traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
"dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
"handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
"baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
"fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
"carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "potted plant", "bed",
"dining table", "toilet", "tv monitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
"microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
"teddy bear", "hair drier", "toothbrush"
]

while True:
    success, img = vid.read()
    img_region = cv2.bitwise_and(img, mask)
    result = model(img_region, stream=True)
    detections = np.empty((0, 5))

    for i in result:
        data = i.boxes
        for j in data:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y2

            conf = math.ceil((j.conf[0]*100))/100
            cls = int(j.cls[0])
            curr_cls = classNames[cls]

            if curr_cls in ["bicycle", "car", "motorbike", "bus", "truck"] and conf >= 0.5:
                # cvzone.cornerRect(img_region, (x1, y1, w, h), l=9)
                # cvzone.putTextRect(img_region, f'{curr_cls}{conf}', (max(0, x1), max(50, y1-15)), scale=0.6, thickness=1, offset=5)
                curr_array = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, curr_array))

        result_tracker = tracker.update(detections)
        cv2.line(img, (limit[0], limit[1]), (limit[2], limit[3]), (0, 0, 255), 5)

        for k in result_tracker:
            x1, y1, x2, y2, id = k
            x1, y1, x2, y2, id = int(x1), int(y1), int(x2), int(y2), int(id)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h), l=9)
            cvzone.putTextRect(img, f'{id}', (max(0, x1), max(50, y1 - 15)), scale=1, thickness=2,offset=8)

            cx, cy = x1+w//2, y1+h//2
            cv2.circle(img, (cx, cy), 3, (255, 0, 255),cv2.FILLED, 3)

            if limit[0] < cx < limit[2] and limit[1]-10 < cy < limit[3]+20 and total_vechiles.count(id) == 0:
                cv2.line(img, (limit[0], limit[1]), (limit[2], limit[3]), (0, 255, 255), 5)
                total_vechiles.append(id)

            cvzone.putTextRect(img, f'count: {len(total_vechiles)}', (50, 50))

        cv2.imshow("Video", img)
        cv2.waitKey(1)