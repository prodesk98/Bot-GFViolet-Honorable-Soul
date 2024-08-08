import ultralytics
from ultralytics import YOLO

ultralytics.checks()


model = YOLO("yolov8n.yaml").load("yolov8n.pt")
model.to("cuda")
model.train(data="dataset.yaml", epochs=256)
