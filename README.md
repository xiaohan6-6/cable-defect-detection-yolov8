# cable-defect-detection-yolov8
Cable defect detection using YOLOv8
# CableGuard-AI 🚀  
**YOLOv8-based Cable Defect Detection System**

## 📌 Overview
CableGuard-AI is a lightweight computer vision system designed for industrial cable inspection.  
It detects foreign objects and cable labels in real-time using YOLOv8.

## 🔥 Highlights
- Real-time cable defect detection
- Multi-class detection: cable / label / foreign_object
- Supports CPU deployment
- Scalable to AI Agent workflows

## 🧠 Tech Stack
- Python 3.10+
- YOLOv8 (Ultralytics)
- OpenCV

## 📊 Training Results
| Metric        | Value |
|--------------|------|
| Dataset Size | ~1200 images |
| Epochs       | 50 |
| mAP@0.5      | 0.89 |
| Precision    | 0.91 |

## 🖼️ Demo Results
(Add your detection images here)

## ⚙️ Quick Start
```bash
pip install ultralytics
yolo detect train model=yolov8s.pt data=dataset.yaml epochs=50
