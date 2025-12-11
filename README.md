# Vietnam Fishery Production Forecasting  

## Giới thiệu  
- Dự án phân tích và dự báo sản lượng thủy sản Việt Nam từ tháng 1/2005 đến 11/2025.  
- Mục tiêu: hiểu xu hướng, mùa vụ và xây dựng mô hình dự báo chính xác.  

## Dữ liệu  
- Nguồn: dữ liệu sản lượng thủy sản theo tháng được cào từ Cục Thống kê ( https://www.nso.gov.vn/en/monthly-report/) trong file `data.xlsx`.  
- Có 251 quan sát, tần suất tháng, định dạng `YYYY-MM-DD` với ngày luôn là ngày đầu tháng.  

## Quy trình phân tích  
- **Biểu đồ gốc**: vẽ chuỗi thời gian toàn bộ để thấy xu hướng tăng và dao động mùa vụ.  
- **Trend**: sử dụng trung bình trượt 12 tháng (moving average) để lấy đường xu hướng.  
- **Khử trend**: trừ đi trend để lấy phần dao động mùa vụ (detrended series).  
- **Zoom 3 năm**: lựa chọn bất kỳ ba năm liên tiếp (ví dụ 2015–2017) để xem chi tiết sự biến động theo tháng.  
- **ACF và PACF**: vẽ hàm tự tương quan và tự tương quan riêng phần để kiểm tra tính dừng và đề xuất tham số ARIMA.  
- **Huấn luyện mô hình**: dùng mô hình SARIMA (1,1,1)(1,1,1,12) phù hợp với chuỗi có mùa vụ 12 tháng.  
- **Đánh giá**: chia dữ liệu thành tập train và test 12 tháng cuối; tính RMSE và MAPE để đo độ chính xác.  
- **Dự báo**: dự báo 12 tháng tiếp theo và so sánh với tập test.  

## Kết quả  
- RMSE ≈ 46.99.  
- MAPE ≈ 3.78% cho tập test, cho thấy mô hình dự báo rất chính xác.  

## Biểu đồ  
- Biểu đồ dữ liệu gốc: toàn bộ chuỗi thời gian 2005–2025.  
- Biểu đồ trend: đường trung bình trượt 12 tháng.  
- Biểu đồ detrended: phần dao động mùa vụ sau khi khử trend.  
- Biểu đồ zoom 3 năm: ví dụ giai đoạn 2015–2017.  
- Biểu đồ ACF.  
- Biểu đồ PACF.  
- Biểu đồ so sánh tập test và dự báo SARIMA (không hiển thị confidence interval).  

## Sử dụng  
- Chạy `fishery_full_analysis.py` để thực hiện toàn bộ quy trình: tải dữ liệu, phân tích, huấn luyện mô hình và tạo biểu đồ.  
- Đảm bảo cài đặt các thư viện: `pandas`, `numpy`, `matplotlib`, `statsmodels`, `sklearn`.  

## Kết luận  
- Dữ liệu sản lượng thủy sản có xu hướng tăng dần qua các năm và có mùa vụ rõ rệt theo năm.  
- Mô hình SARIMA với tham số (1,1,1)(1,1,1,12) đã mô tả tốt cấu trúc chuỗi thời gian và cho kết quả dự báo chính xác với sai số thấp.  
- Quy trình phân tích có thể mở rộng cho các bài toán dự báo chuỗi thời gian khác với tần suất tháng. 
