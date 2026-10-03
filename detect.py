from ultralytics import YOLO

# Load trained model
model = YOLO("model/best.pt")

# Test PCB image
image_path = "results/YOLOv8_PCB_Defect_Detection.jpg"

# Run prediction
results = model.predict(
    source=image_path,
    conf=0.25,
    save=True
)

print("PCB defect detection completed!")
