import cv2
import easyocr
import logging

logger = logging.getLogger(__name__)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def process_license_plate(image, detections):
    try:
        results = []
        
        for detection in detections:
            x1, y1, x2, y2, conf, cls = detection
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            
            # Cắt vùng biển số
            plate_roi = image[y1:y2, x1:x2]
            
            # OCR biển số
            ocr_result = reader.readtext(plate_roi)
            
            # Log toàn bộ kết quả OCR
            logger.info(f"Raw OCR result: {ocr_result}")
            
            if ocr_result:
                # Lấy tất cả các text và confidence
                for bbox, text, ocr_conf in ocr_result:
                    # Chỉ lấy số và chữ
                    clean_text = ''.join(c for c in text if c.isalnum())
                    logger.info(f"Text: {clean_text}, OCR confidence: {ocr_conf}")
                
                # Chọn text có confidence cao nhất
                best_result = max(ocr_result, key=lambda x: x[2])
                plate_text = ''.join(c for c in best_result[1] if c.isalnum())
                ocr_confidence = best_result[2]
            else:
                plate_text = ""
                ocr_confidence = 0.0
            
            # Vẽ bounding box và hiển thị cả YOLO confidence và OCR confidence
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{plate_text} (YOLO: {conf:.2f}, OCR: {ocr_confidence:.2f})"
            cv2.putText(image, text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            if plate_text:
                results.append(f"{plate_text} ({ocr_confidence:.2f})")
        
        final_text = ' | '.join(results) if results else "No plate detected"
        return image, final_text
        
    except Exception as e:
        logger.error(f"OCR Error: {str(e)}")
        raise
