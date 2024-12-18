from ultralytics import YOLO
import cv2
import logging
from pathlib import Path

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
            return results[0].boxes.data
            
        except Exception as e:
            logger.error(f"Detection error: {str(e)}")
            raise 