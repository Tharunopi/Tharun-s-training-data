import cv2, cvzone, math
from ultralytics import YOLO
from sort import Sort
import numpy as np

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
mask = cv2.imread("people mask.png")
tracker = Sort(max_age=15, min_hits=3, iou_threshold=0.3)
limit1 = [170, 297, 430, 297]
limit2 = [500, 350, 700, 350]
up_count = []
down_count = []

vid = cv2.VideoCapture("people.mp4")
vid.set(3, 1280)
vid.set(4, 720)

while True:
    success, img = vid.read()
    img_region = cv2.bitwise_and(img, mask)
    detections = np.empty((0, 5))
    result = model(img_region, stream=True)

    for i in result:
        data = i.boxes
        for j in data:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            conf = math.ceil((j.conf[0]*100))/100
            cls = int(j.cls[0])
            curr_class = classNames[cls]

            if conf > 0.50 and curr_class =="person":
                curr_array = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, curr_array))

        tracker_result = tracker.update(detections)
        cv2.line(img_region, (limit1[0], limit1[1]), (limit1[2], limit1[3]), (0, 0, 255), 5)
        cv2.line(img_region, (limit2[0], limit2[1]), (limit2[2], limit2[3]), (0, 0, 255), 5)

        for i in tracker_result:
            x1, y1, x2, y2, id = i
            x1, y1, x2, y2, id = int(x1), int(y1), int(x2), int(y2), int(id)
            w, h = x2-x1, y2-y1
            cx, cy = x1+w//2, y1+h//2

            cvzone.cornerRect(img_region, (x1, y1, w, h), l=9)
            cvzone.putTextRect(img_region, f'peron id {id}', (max(0, x1), max(50, y1-15)), scale=1, thickness=1, offset=5)

            cv2.circle(img_region, (cx, cy), 3, (255, 0, 255), cv2.FILLED)

            if limit1[0] < cx < limit1[2] and limit1[1]-20 < cy < limit1[3]+20:
                if up_count.count(id) == 0:
                    cv2.line(img_region, (limit1[0], limit1[1]), (limit1[2], limit1[3]), (255, 0, 255), 5)
                    up_count.append(id)

            if limit2[0] < cx <limit2[2] and limit2[1]-20 < cy < limit2[3]+20:
                if down_count.count(id) == 0:
                    cv2.line(img_region, (limit2[0], limit2[1]), (limit2[2], limit2[3]), (255, 0, 255), 5)
                    down_count.append(id)

            cvzone.putTextRect(img_region, f'Up count: {len(up_count)}', (50, 50))
            cvzone.putTextRect(img_region, f'Down count {len(down_count)}', (500, 50))

        cv2.imshow("People count", img_region)
        cv2.waitKey(1)