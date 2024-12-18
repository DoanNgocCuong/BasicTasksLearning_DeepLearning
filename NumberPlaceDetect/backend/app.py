from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import sys
import logging
import base64
from io import BytesIO
from detection import LicensePlateDetector
from OCR import process_license_plate

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
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "allow_headers": ["Content-Type"],
        "expose_headers": ["Content-Type"],
        "methods": ["GET", "POST", "OPTIONS"]
    }
})

# Initialize detector only
detector = LicensePlateDetector()

@app.route('/detect', methods=['POST'])
def detect_license_plate():
    try:
        logger.info("Received detection request")
        
        # Get image file from request
        file = request.files['image']
        nparr = np.fromstring(file.read(), np.uint8)
        cv_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Detect license plates
        detections = detector.detect(cv_image)
        
        # Process OCR directly using process_license_plate
        processed_image, plate_text = process_license_plate(cv_image, detections)
        
        # Convert processed image to bytes
        _, img_encoded = cv2.imencode('.jpg', processed_image)
        
        logger.info("Sending processed image and plate text")
        return jsonify({
            'plate_text': plate_text,
            'image': base64.b64encode(img_encoded.tobytes()).decode('utf-8')
        })
        
    except Exception as e:
        logger.error(f"Error during processing: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("🚀 Starting Flask application...")
    app.run(host='0.0.0.0', port=3001, debug=True)