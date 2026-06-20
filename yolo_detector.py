import cv2
import numpy as np
from ultralytics import YOLO
from urllib.request import urlopen

ESP32_IP = "192.168.43.133"
ESP32_CAPTURE = f"http://{ESP32_IP}/capture"


class YOLODetector:

    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def get_frame(self):

        try:
            img_resp = urlopen(ESP32_CAPTURE, timeout=1)
            img_np = np.asarray(bytearray(img_resp.read()), dtype="uint8")
            frame = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
            return frame
        except:
            return None

    def detect(self, frame):

        fall_detected = False
        confidence = 0
        annotated = frame

        results = self.model(frame, verbose=False)
        annotated = results[0].plot()

        if results[0].boxes is not None:

            classes = results[0].boxes.cls.cpu().numpy()
            confs = results[0].boxes.conf.cpu().numpy()

            for c, conf in zip(classes, confs):

                label = self.model.names[int(c)]

                if label.lower() == "fall":
                    fall_detected = True
                    confidence = float(conf)

        return annotated, fall_detected, confidence