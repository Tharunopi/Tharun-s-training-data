from ultralytics import YOLO
import cv2

model = YOLO('Yolo models/yolov8l.pt')
result = model('coconut image(3).jpg', show=True)
cv2.waitKey(0)