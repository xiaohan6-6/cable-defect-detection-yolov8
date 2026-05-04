from ultralytics import YOLO

if __name__ == "__main__":
    # 加载YOLOv8模型
    model = YOLO("yolov8s.pt")
    # 训练配置
    model.train(
        data="dataset.yaml",
        epochs=50,
        imgsz=640,
        device="cpu"
    )
