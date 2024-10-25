
Mình support Project bạn: [Trương Cao Vũ](https://www.facebook.com/profile.php?id=100014272756773)


### Bảng 1 - Chỉ Số, Ý Nghĩa và Thế nào là tốt

| **Chỉ Số**              | **Ý Nghĩa**                                                                                         | **Thế nào là tốt?**                                                                                      |
|-------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Time Training/Inference | Thời gian huấn luyện hoặc suy luận cho mỗi lần đánh giá mô hình.                                      | Thời gian ngắn giúp tối ưu hiệu suất mô hình.                                                             |
| Precision               | Tỉ lệ giữa số dự đoán đúng (true positives) và tổng số các dự đoán (true positives + false positives). Precision cao nghĩa là mô hình ít dự đoán sai. | Precision cao thể hiện độ chính xác của mô hình trong việc đưa ra dự đoán đúng.                           |
| Recall                  | Tỉ lệ giữa số dự đoán đúng và tổng số đối tượng thực sự có (true positives + false negatives). Recall cao nghĩa là mô hình phát hiện tốt các đối tượng. | Recall cao thể hiện khả năng phát hiện đầy đủ các đối tượng trong dữ liệu.                                |
| mAP@0.5                 | Mean Average Precision tại ngưỡng IoU = 0.5, đo lường độ chính xác của dự đoán khi yêu cầu độ chồng lấn giữa các hộp giới hạn là 50%. | mAP@0.5 cao cho thấy mô hình có khả năng phát hiện tốt các đối tượng với độ chính xác hộp giới hạn (bounding boxes). |
| mAP@0.5:0.95            | Mean Average Precision trung bình qua nhiều ngưỡng IoU từ 0.5 đến 0.95. Chỉ số này phản ánh khả năng dự đoán chính xác với các mức độ chồng lấn khác nhau. | mAP@0.5:0.95 cao thể hiện khả năng tổng quát hóa tốt của mô hình, đặc biệt trong các bài toán có các đối tượng chồng lấn. |

### Bảng 2 - Kết quả các Chỉ Số từ các giai đoạn Huấn Luyện và Kiểm Tra

| **Chỉ Số**              | **Validation - trước huấn luyện** | **Validation - 3 epochs - Yolov8n - No Augmentation** | **Validation - 15 epochs - Yolov8n - No Augmentation** | **Test - 15 epochs - Yolov8n - No Augmentation** | **Validation - 30 epochs - Yolov8m - withAug** | **Test - 30 epochs - Yolov8m - withAug** |
|-------------------------|-----------------------------------|------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------|------------------------------------------------|------------------------------------------|
| Time Training/Inference | N/A                               | 0.08 giờ                                             | 0.4 giờ                                               | 0.01 giờ                                         | 1.5 giờ                                        | 0.02 giờ                                     |
| Precision               | 0.526                             | 0.808                                                | 0.865                                                 | 0.904                                           | 0.912                                          | 0.889                                        |
| Recall                  | 0.333                             | 0.713                                                | 0.811                                                 | 0.597                                           | 0.867                                          | 0.829                                        |
| mAP@0.5                 | 0.526                             | 0.808                                                | 0.898                                                 | 0.904                                           | 0.921                                          | 0.892                                        |
| mAP@0.5:0.95            | 0.333                             | 0.499                                                | 0.618                                                 | 0.597                                           | 0.652                                          | 0.628                                        |


### Nhận xét: 


- Trước khi huấn luyện: Khi thực hiện đánh giá ban đầu trên tập validation, mô hình YOLOv8 đạt Precision là 0.526, Recall là 0.333, mAP@0.5 là 0.526, và mAP@0.5:0.95 là 0.333. Đây là các chỉ số từ mô hình YOLOv8 cơ bản chưa được tối ưu hóa.
- Sau khi huấn luyện (3 epochs - Yolov8s - No Augmentation) – 0.08h (4.8min): Sau 3 epochs huấn luyện, các chỉ số cho thấy sự cải thiện đáng kể: Precision tăng lên 0.808, Recall đạt 0.713, mAP@0.5 là 0.808 và mAP@0.5:0.95 là 0.499. Những kết quả này thể hiện rằng mô hình đã học được đặc trưng quan trọng của đối tượng người trong các ảnh nhiệt.
- Sau khi huấn luyện (15 epochs - Yolov8s - No Augmentation) – 0.4h (24min): Sau 15 epochs huấn luyện, các chỉ số tiếp tục cải thiện với Precision đạt 0.865, Recall là 0.811, mAP@0.5 đạt 0.898 và mAP@0.5:0.95 đạt 0.618 trên tập validation. Điều này thể hiện rằng mô hình đã học tốt hơn về khả năng phát hiện và nhận diện đối tượng trong các điều kiện phức tạp.
- Chuyển qua huấn luyện (30 epochs – Yolov8m – with Augmentation) – 1.5h (90min): Sau khi hoàn tất huấn luyện với mô hình Yolov8m và bổ sung kỹ thuật tăng cường dữ liệu (augmentation), mô hình tiếp tục cải thiện trên tất cả các chỉ số. Precision đạt 0.912, Recall tăng lên 0.867, mAP@0.5 đạt 0.921, và mAP@0.5:0.95 đạt 0.652. Kỹ thuật tăng cường dữ liệu đã giúp mô hình trở nên mạnh mẽ hơn trong việc nhận diện đối tượng người dưới các điều kiện phức tạp và biến động của dữ liệu.


