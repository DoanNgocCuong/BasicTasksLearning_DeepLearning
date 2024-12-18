from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
import cv2
import numpy as np
from ultralytics import YOLO
import os
import sys
import logging
from io import BytesIO
from pathlib import Path

# Set console output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Set up detailed logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Configure CORS to allow all origins
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "allow_headers": ["Content-Type"],
        "expose_headers": ["Content-Type"],
        "methods": ["GET", "POST", "OPTIONS"]
    }
})

# Initialize YOLO model
SCRIPTS_FOLDER = Path(__file__).parent
model = YOLO(SCRIPTS_FOLDER / "model/best.pt")

@app.route('/detect', methods=['POST'])
def detect_license_plate():
    try:
        logger.info("Received detection request")
        
        # Get image file from request
        file = request.files['image']
        
        # Read image
        nparr = np.fromstring(file.read(), np.uint8)
        cv_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        logger.info("Running YOLO detection")
        # Run YOLO detection
        results = model(cv_image, conf=0.2, verbose=False)
        
        # Draw bounding boxes
        for result in results[0].boxes.data:
            x1, y1, x2, y2, conf, cls = result
            cv2.rectangle(cv_image, 
                         (int(x1), int(y1)), 
                         (int(x2), int(y2)), 
                         (0, 255, 0), 2)
        
        # Convert processed image to bytes
        _, img_encoded = cv2.imencode('.jpg', cv_image)
        img_bytes = BytesIO(img_encoded.tobytes())
        
        logger.info("Sending processed image")
        return send_file(img_bytes, mimetype='image/jpeg')
        
    except Exception as e:
        logger.error(f"Error during detection: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("🚀 Starting Flask application...")
    app.run(host='0.0.0.0', port=3001, debug=True)