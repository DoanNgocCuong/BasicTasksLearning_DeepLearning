from ultralytics import YOLO
import cv2
import logging
from pathlib import Path
import numpy as np

logger = logging.getLogger(__name__)

class LicensePlateDetector:
    def __init__(self):
        SCRIPTS_FOLDER = Path(__file__).parent
        self.model = YOLO(SCRIPTS_FOLDER / "model/best.pt")
        
    def detect(self, image, conf_threshold=0.2):
        """
        Detect license plates in the image
        Returns: List of detections (coordinates and confidence)
        """
        try:
            logger.info("Running YOLO detection")
            results = self.model(image, conf=conf_threshold, verbose=False)
            
            if len(results[0].boxes) > 0:
                logger.info(f"Found {len(results[0].boxes)} license plates")
                boxes = results[0].boxes.data.cpu().numpy()
                logger.info(f"Detection boxes: {boxes}")
                return boxes
            else:
                logger.warning("No license plates detected")
                return np.array([])
            
        except Exception as e:
            logger.error(f"Detection error: {str(e)}")
            raise