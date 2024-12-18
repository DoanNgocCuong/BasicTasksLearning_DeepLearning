```
project/
├── backend/                       # Code xử lý server-side (API, model)
│   ├── app.py                     # Flask app (backend API)
│   ├── model/
│   │   └── best.pt                # Model YOLO đã huấn luyện
│   ├── uploads/                   # Thư mục chứa ảnh upload và kết quả
│   └── requirements.txt           # Thư viện cần thiết cho backend
├── frontend/                      # Code xử lý client-side (UI, static files)
│   ├── index.html                 # Trang chính giao diện người dùng
│   ├── static/
│   │   ├── style.css              # File CSS cho UI
│   │   └── script.js              # File JavaScript xử lý logic
├── README.md                      # Hướng dẫn sử dụng

```