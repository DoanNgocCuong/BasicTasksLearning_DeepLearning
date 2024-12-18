- Bước 1 : Phát hiện ra cái biển (chưa có bêết là biển số bao nhiêu) 
-> cắt khung biến số ra.

- Bước 2 : OCR (Nhận diện chữ và số trong ảnh) 
-> nhận diện chữ và số trong khung biến số.

--------------------------------

Training Mô hình cho bước 1: 
- 

Dataset có sẵn các ảnh chứa biển số xe đã được gán nhãn. 

- Chia 3 tập: Train, Valid, Test



+, Dùng thư viện roboflow để kết nối với dataset. 
+, Cấu trúc thư mục sau khi down dataset về: 


Vẽ cấu trúc thư mục sau khi down về bằng markdown
```bash
/kaggle/working/PersonDection-5/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── train/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
├── data.yaml
├── README.dataset.txt
├── README.roboflow.txt
└── roboflow.zip
```

- Train và valid để train model. 
+, Train: gán nhãn cho máy học. 
??? Bản chất là quá trình điều chỉnh các tham số của mô hình để cho học dữ liệu đấy. 
+, Valid: được sử dụng trong quá trình training, 
+, 1 epoch là 1 lần model đi hết qua dữ liệu TẬP TRAIN. 
Sau khi hết 1 epoch, model sẽ được đánh giá bằng dữ liệu TẬP VALID. => Model sẽ tự điều chỉnh tham số của nó để cải thiện độ chính xác 

+, Đến epoch thứ 2 => model lại đi qua tập TRAIN, và đánh giá bằng tập VALID. ....

+, .... 1 lần đi qua hết dữ liệu là 1 epoch. 


---------

Khi mà model Yolov8 chưa được training, thì khi chạy thử trên 1 cái ảnh, kết quả nó tệ như này 
(mô hình nhận diện không đúng biển số xe)

----
Kết quả đánh ra mô hình trước huấn luyện: 

```bash
Speed: 0.7ms preprocess, 3.1ms inference, 0.0ms loss, 1.1ms postprocess per image
Results saved to runs/detect/val
Đánh giá trước khi huấn luyện trên tập validation:
Precision: 0.001
Recall: 0.000
mAP@0.5: 0.001
mAP@0.5:0.95: 0.000
```

Ý nghĩa các chỉ số 
```markdown
| **Metrics**       | **Ý Nghĩa**                                                                                          |
|-------------------|------------------------------------------------------------------------------------------------------|
| **Time Training/Inference** | Thời gian huấn luyện hoặc suy luận cho mỗi lần đánh giá mô hình. Thời gian ngắn giúp tối ưu hiệu suất mô hình. |
| **Precision**      | Tỉ lệ giữa số dự đoán đúng (true positives) và tổng số các dự đoán (true positives + false positives). Precision cao nghĩa là mô hình ít dự đoán sai. |
| **Recall**         | Tỉ lệ giữa số dự đoán đúng và tổng số đối tượng thực sự có (true positives + false negatives). Recall cao nghĩa là mô hình phát hiện tốt các đối tượng. |
| **mAP@0.5**        | Mean Average Precision tại ngưỡng IoU = 0.5, đo lường độ chính xác của dự đoán khi yêu cầu độ chồng lấn giữa các hộp giới hạn là 50%. |
| **mAP@0.5:0.95**   | Mean Average Precision trung bình qua nhiều ngưỡng IoU từ 0.5 đến 0.95. Chỉ số này phản ánh khả năng dự đoán chính xác với các mức độ chồng lấn khác nhau. |
```


