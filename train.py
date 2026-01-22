from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")

model.train(
    data="dataset/images/train",
    epochs=10,
    imgsz=224,
    batch=16
)
