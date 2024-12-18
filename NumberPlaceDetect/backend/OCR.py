import cv2
import easyocr
import logging
import numpy as np

logger = logging.getLogger(__name__)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def preprocess_plate(plate_roi):
    """
    Tiền xử lý ảnh biển số để tăng độ chính xác OCR
    """
    # Chuyển sang ảnh xám
    gray = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
    
    # Tăng contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    
    # Lọc nhiễu
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    
    # Ngưỡng hóa
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Resize to larger size
    scale = 2
    width = int(thresh.shape[1] * scale)
    height = int(thresh.shape[0] * scale)
    enlarged = cv2.resize(thresh, (width, height), interpolation=cv2.INTER_CUBIC)
    
    return enlarged

def process_license_plate(image, detections):
    try:
        if len(detections) == 0:
            return image, "No plate detected"
            
        results = []
        
        for detection in detections:
            x1, y1, x2, y2, conf, cls = detection
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            
            # Cắt vùng biển số
            plate_roi = image[y1:y2, x1:x2]
            
            # Tiền xử lý ảnh
            processed_roi = preprocess_plate(plate_roi)
            
            # OCR với allowlist để chỉ nhận dạng số và chữ cái
            ocr_result = reader.readtext(processed_roi, 
                                       allowlist='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-')
            
            if ocr_result:
                # Kết hợp các text thành biển số hoàn chỉnh
                texts = []
                for _, text, conf in ocr_result:
                    clean_text = ''.join(c for c in text if c.isalnum() or c == '-')
                    if clean_text:
                        texts.append(clean_text)
                
                # Ghép các phần text lại với nhau
                plate_text = '-'.join(texts)
                
                # Vẽ bounding box và text
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, plate_text, (x1, y1-10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                results.append(plate_text)
                logger.info(f"Detected plate: {plate_text}")
        
        final_text = ' | '.join(results) if results else "No plate detected"
        return image, final_text
        
    except Exception as e:
        logger.error(f"OCR Error: {str(e)}")
        raise
