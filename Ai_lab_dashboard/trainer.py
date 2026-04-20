from ultralytics import YOLO
import os
import json
from datetime import datetime

class Trainer:

    def __init__(self):
        self.model_version = "v1"

    def train(self):

        model = YOLO("yolov8n.pt")

        model.train(
            data="dataset/data.yaml",
            epochs=5,
            imgsz=640
        )

        # Save versioned model
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        save_path = f"models/{self.model_version}_{timestamp}.pt"

        model.save(save_path)

        self.log_version(save_path)

        return save_path

    def log_version(self, path):

        file = "versions.json"

        if not os.path.exists(file):
            data = []
        else:
            with open(file, "r") as f:
                data = json.load(f)

        data.append({"model": path})

        with open(file, "w") as f:
            json.dump(data, f)