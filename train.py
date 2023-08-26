from ultralytics import YOLO

# Load the model.
model = YOLO('yolov8n.pt')

# Training.
results = model.train(
   data='road_sign_yolov8.yaml',
   imgsz=640,
   epochs=100,
   batch=16,
   name='road_sign_yolov8_100e'
)
