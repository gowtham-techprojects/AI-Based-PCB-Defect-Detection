# AI-Based PCB Defect Detection

An AI-based PCB defect detection system using YOLOv8.

## Detected Defects

- Open
- Short
- Mouse Bite
- Spur
- Copper
- Hole

## Model

YOLOv8 Nano trained on the DeepPCB dataset.

## Results

The trained model achieved approximately 98.1% mAP50 on the validation dataset.

## Test Detection

The model was tested on a PCB image and successfully detected:
- 3 Shorts
- 6 Holes

## Project Structure

PCB_Defect_Detection/
├── model/
├── results/
└── src/

## Technologies

- Python
- YOLOv8
- Ultralytics
- OpenCV
- Deep Learning
