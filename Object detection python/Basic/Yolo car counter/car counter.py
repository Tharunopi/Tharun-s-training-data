import cv2, math, cvzone
from ultralytics import YOLO

vid = cv2.VideoCapture("cars.mp4")

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
    result = model(img, stream=True)

    for i in result:
        data = i.boxes
        for j in data:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, w, h = int(x1), int(y1), int(x2-x1), int(y2-y1)

            conf = math.ceil((j.conf[0]*100))/100
            cls = int(j.cls[0])
            curr_cls = classNames[cls]

            if curr_cls in ["bicycle", "car", "motorbike", "bus", "truck"] and conf >= 0.5:
                cvzone.cornerRect(img, (x1, y1, w, h), l=9)
                cvzone.putTextRect(img, f'{curr_cls}{conf}', (max(0, x1), max(50, y1-15)), scale=0.6, thickness=1, offset=5)

        cv2.imshow("Video", img)
        cv2.waitKey(1)