# 📊 BÁO CÁO THỐNG KÊ ĐỒ THỊ TRI THỨC: PHÂN HỆ BỆNH MẠN TÍNH

![Dataset](https://img.shields.io/badge/Dataset-Chronic_Diseases-red.svg)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)
![Nodes](https://img.shields.io/badge/Nodes-1,982-blue.svg)
![Edges](https://img.shields.io/badge/Edges-6,488-orange.svg)

Báo cáo này trình bày các chỉ số phân tích chi tiết của đồ thị tri thức sau khi đã được trích lọc (filter) độc lập, chỉ tập trung vào danh sách các mã ICD-10 thuộc nhóm **Bệnh Mãn Tính**.

---

## 1. Kích Thước Tổng Thể (Macro Metrics)
Đồ thị con (sub-graph) chuyên biệt cho bệnh mãn tính thể hiện một cấu trúc mạng lưới tập trung và độ chính xác cao:
* **Tổng số Cạnh (Edges / Liên kết):** 6,488
* **Tổng số Đỉnh (Nodes / Thực thể):** 1,982

---

## 2. Phân Bố Số Lượng Đỉnh (Node Distribution)
Hệ thống phân loại thực thể y khoa thành 9 nhóm chính. Việc can thiệp y tế và yếu tố nguy cơ chiếm tỷ trọng cao phản ánh đúng đặc thù quản lý dài hạn của các bệnh mãn tính:

| Loại Thực Thể (Node Type) | Ý Nghĩa Khái Niệm | Số Lượng | Tỷ Trọng (%) |
| :--- | :--- | :--- | :--- |
| **Intervention** | Can thiệp y tế / Phẫu thuật | 357 | 18.01% |
| **RiskFactor** | Yếu tố nguy cơ | 344 | 17.36% |
| **Symptom** | Triệu chứng lâm sàng | 278 | 14.03% |
| **Complication** | Biến chứng | 271 | 13.67% |
| **Demographic** | Đặc điểm nhân khẩu học | 246 | 12.41% |
| **DiagnosticTest**| Xét nghiệm / Chẩn đoán | 201 | 10.14% |
| **Drug** | Thuốc điều trị | 140 | 7.06% |
| **Disease** | Bệnh (Mã ICD-10) | 84 | 4.24% |
| **Pathogen** | Tác nhân gây bệnh | 61 | 3.08% |

---

## 3. Độ Dày Tri Thức & Mật Độ Đồ Thị (Graph Density)
Với mức trung bình đạt **77.24 liên kết cho mỗi bệnh**, đồ thị thể hiện mật độ thông tin lâm sàng cực kỳ dày đặc. Một nút Bệnh Mãn Tính bất kỳ trong mạng lưới sẽ kết nối trung bình với:

| Loại Liên Kết (Từ Bệnh Mãn Tính) | Số lượng kết nối trung bình |
| :--- | :--- |
| Số biến chứng liên quan (`HAS_COMPLICATION`) | 14.4 biến chứng / bệnh |
| Số yếu tố nguy cơ (`INCREASES_RISK_OF`) | 13.0 yếu tố / bệnh |
| Số triệu chứng (`HAS_SYMPTOM`) | 12.7 triệu chứng / bệnh |
| Số phương pháp can thiệp (`PART_OF_TREATMENT`) | 11.9 phương pháp / bệnh |
| Nhóm nhân khẩu học ảnh hưởng (`AFFECTS_POPULATION`) | 10.1 yếu tố / bệnh |
| Số phương pháp xét nghiệm (`DIAGNOSED_BY`) | 8.0 phương pháp / bệnh |
| Số loại thuốc điều trị (`TREATS`) | 5.5 loại thuốc / bệnh |
| Số tác nhân gây bệnh (`CAUSES`) | 1.7 tác nhân / bệnh |

---

## 4. Chất Lượng Nguồn Tham Khảo (Source Lineage)
Mạng lưới tri thức bệnh mãn tính được củng cố bởi các nguồn dữ liệu có độ uy tín tối đa. Hệ thống không sử dụng dữ liệu nguồn dịch (Tier 3, 4) hay nguồn tự do (Tier 5) cho tệp bệnh này:

| Phân Cấp Uy Tín (Tier) | Đặc Điểm Nguồn Trích Xuất | Số Lượng Cạnh | Tỷ Trọng (%) |
| :--- | :--- | :--- | :--- |
| **Tầng 1 (Chính thống VN)** | Các trang của Bộ Y tế, tạp chí y khoa (`gov.vn`, `vjid.vn`...) | 5,983 | 92.22% |
| **Tầng 2 (Y tế Tư nhân/BV)** | Các bệnh viện lớn, hệ thống nhà thuốc (`vinmec.com`, `medlatec`...) | 505 | 7.78% |

---

## 5. Tỷ Lệ Bao Phủ Dữ Liệu (Coverage Ratio)
Mục tiêu thu thập dữ liệu trên danh sách mã ICD-10 bệnh mãn tính đã hoàn thành xuất sắc:
* **Tổng mã bệnh mãn tính mục tiêu:** 84 mã
* **Số bệnh mãn tính trích xuất thành công:** 84 mã
* **Tiến độ bao phủ:** **100.00%** (Hoàn thành tuyệt đối việc ghim dữ liệu cho toàn bộ danh sách).
