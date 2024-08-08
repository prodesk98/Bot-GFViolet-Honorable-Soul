from typing import List
from ultralytics.engine.results import Results
from ultralytics import YOLO
from pathlib import Path

import numpy as np
import pyautogui
import cv2

from loguru import logger


USE_GPU: bool = True
FRAME_SHAPE = (640, 640)


class Detect:
    def __init__(self, region: tuple[int, int, int, int]):
        self.model = YOLO("%s/model/gf0v1.pt" % Path(__file__).parent)
        if USE_GPU:
            self.model.to("cuda")
        self.region = region

    def predict(self, image_bytes: np.ndarray) -> List[Results] | None:
        results = self.model.track(image_bytes)
        return results

    def display(self):
        while True:
            frame = np.array(pyautogui.screenshot(region=self.region))
            frame_cvtColor = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            resized_frame = cv2.resize(frame_cvtColor, FRAME_SHAPE)

            results = self.predict(resized_frame)
            logger.debug(results)

            annotated_frame = results[0].plot()

            cv2.imshow("Computer Vision", annotated_frame)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break
