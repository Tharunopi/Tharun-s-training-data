from ultralytics import YOLO
import cv2

model = YOLO('custom model/yolov8n.pt')
result = model("coconut image(3).jpg", show=True)
cv2.waitKey(0)