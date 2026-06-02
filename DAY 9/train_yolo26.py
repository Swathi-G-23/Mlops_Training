from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data=r"C:\Users\swath\OneDrive\Desktop\Smart Healthcare\dataset\data.yaml",
    epochs=80,
    imgsz=640,
    batch=4
)