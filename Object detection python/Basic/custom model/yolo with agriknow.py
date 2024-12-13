import cv2, cvzone, math
from ultralytics import YOLO
import numpy as np
from sort import Sort

model = YOLO('yolov8n.pt')
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

tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)
video = cv2.VideoCapture('people.mp4')
video.set(3, 1280)
video.set(4, 720)

while True:
    succes, img = video.read()
    detections = np.empty((0, 5))
    result = model(img, stream=True)

    for i in result:
        data = i.boxes
        for j in data:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            conf = math.ceil((j.conf[0]*100))/100
            cls = int(j.cls[0])
            cur_cls = classNames[cls]

            if conf > 0.50:
                cur_array = [x1, y1, x2, y2, conf]
                detections = np.vstack((detections, cur_array))

        tracker_result = tracker.update(detections)

        for k in tracker_result:
            x1, y1, x2, y2, id = k
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            cx, cy = x1+w//2, y1+h//2
            cv2.circle(img, (cx, cy), 5, (0, 255, 255), 5)
            cvzone.cornerRect(img, (x1, y1, w, h))
            cvzone.putTextRect(img, f'{cur_cls}{id}  {conf}', (max(0, x1), max(15, y1)))

        cv2.imshow("image", img)
        cv2.waitKey(1)