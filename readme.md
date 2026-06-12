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

---

## 6. Thực hành: Phát hiện bệnh COPD dựa trên đồ thị tri thức

### 🎯 Mục tiêu
Sử dụng bộ lọc (filter) tập hợp các **dấu hiệu điển hình** của bệnh phổi tắc nghẽn mạn tính (COPD) – bao gồm triệu chứng, yếu tố nguy cơ và biến chứng – để tìm ra những bệnh có hồ sơ tri thức tương tự nhất. Từ đó tính **điểm chuẩn đoán** nhằm hỗ trợ phân biệt COPD với các bệnh hô hấp khác (hen phế quản, viêm phổi…).

### 🔍 Truy vấn Cypher (rút gọn)
```cypher
// 1. GOM CÁC DẤU HIỆU COPD VÀO BỘ LỌC
MATCH (d:Disease)
OPTIONAL MATCH (d)-[:HAS_SYMPTOM]->(s:Symptom)
WHERE toLower(s.node_name) CONTAINS 'khó thở' OR 'thở khò khè' ...
OPTIONAL MATCH (d)<-[:INCREASES_RISK_OF]-(rf:RiskFactor)
WHERE toLower(rf.node_name) CONTAINS 'khói thuốc' OR 'khí độc' ...
OPTIONAL MATCH (d)-[:HAS_COMPLICATION]->(c:Complication)
WHERE toLower(c.node_name) CONTAINS 'tràn khí màng phổi' OR 'suy tim' ...

// 2. TÍNH ĐIỂM CHUẨN ĐOÁN
// Điểm = (Số triệu chứng khớp *2 + Số biến chứng khớp *1.5 + Số yếu tố nguy cơ khớp) * (% khớp)
...
RETURN d.node_id, d.node_name, So_Trieu_Chung_Khop, So_Bien_Chung_Khop,
       Phan_Tram_Khop, Diem_Chuan_Doan
ORDER BY Diem_Chuan_Doan DESC LIMIT 10;
```
### 📊 Kết quả top 10 bệnh có điểm tương đồng cao nhất với bộ dấu hiệu COPD

| Mã bệnh | Tên bệnh | Khớp triệu chứng | Khớp biến chứng | % khớp | Điểm chuẩn đoán |
| --- | --- | --- | --- | --- | --- |
| J44 | Bệnh phổi tắc nghẽn mạn tính (COPD) | 5 | 3 | 100.0 | 1450.0 |
| J44 | Bệnh phổi tắc nghẽn mạn tính khác | 8 | 4 | 35.0 | 840.0 |
| J44.0 | Bệnh phổi tắc nghẽn mạn tính kèm nhiễm trùng đường hô hấp dưới cấp tính | 3 | 5 | 36.67 | 605.06 |
| J44.9 | Bệnh phổi tắc nghẽn mạn tính, không xác định | 6 | 3 | 34.48 | 603.4 |
| J44.1 | Bệnh phổi tắc nghẽn mạn tính đợt cấp, không xác định | 4 | 4 | 32.35 | 549.95 |
| J44.8 | Bệnh phổi tắc nghẽn mạn tính xác định khác | 3 | 4 | 33.33 | 466.62 |
| J45.9 | Hen phế quản (hen suyễn), không xác định | 5 | 2 | 20.0 | 280.0 |
| J45.8 | Hen phế quản (hen suyễn) hỗn hợp | 4 | 1 | 19.23 | 182.69 |
| J45 | Hen phế quản (hen suyễn) | 3 | 1 | 17.86 | 151.81 |
| J46 | Cơn hen phế quản ác tính | 4 | 2 | 11.48 | 137.76 |

### 💡 Nhận xét

- **COPD gốc (J44)** đạt điểm tuyệt đối 1450, khớp 100% các dấu hiệu → thể hiện độ chính xác của bộ lọc.

- Các mã **J44.x** (phân nhánh của COPD) đều nằm trong top 6, điểm số giảm dần do % khớp thấp hơn (chỉ 32–37%), phản ánh đúng thực tế lâm sàng: chúng là các biến thể hoặc đợt cấp, không hội tụ đầy đủ tất cả đặc điểm nền của COPD.

- **Hen phế quản (J45, J46)** cũng xuất hiện (top 7–10) nhờ chia sẻ các triệu chứng như khó thở, thở khò khè. Tuy nhiên điểm chuẩn đoán chỉ bằng 10–20% so với COPD, giúp hệ thống có thể phân biệt tương đối hai bệnh lý dễ nhầm lẫn này.

### 📌 Ứng dụng

Kỹ thuật “gom dấu hiệu + tính điểm trọng số” có thể mở rộng cho bất kỳ nhóm bệnh nào (đái tháo đường, tăng huyết áp, suy tim…) nhằm:

- Gợi ý chẩn đoán phân biệt dựa trên dữ liệu thực tế.
- Lượng hóa mức độ tương đồng giữa các bệnh đồng mắc (comorbidity).
- Hỗ trợ xây dựng hệ khuyến nghị lâm sàng (clinical decision support).
