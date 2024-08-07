from typing import List
from ultralytics.engine.results import Results
from ultralytics import YOLO
from pathlib import Path

import numpy as np
import pyautogui
import cv2


SIZE_SCALE = 2


class Detect:
    def __init__(self, region: tuple[int, int, int, int]):
        self.model = YOLO("%s/model/gf0.pt" % Path(__file__).parent)
        self.region = region

    def predict(self, image_bytes: np.ndarray) -> List[Results] | None:
        results = self.model.predict(image_bytes)
        return results

    def display(self):
        while True:
            frame = np.array(pyautogui.screenshot(region=self.region))
            frame_cvtColor = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame_height, frame_width = frame.shape[:2]

            # results = self.predict(frame)

            boxes = []
            confidences = []

            cv2.imshow("Computer Vision", frame_cvtColor)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break
