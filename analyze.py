import pandas as pd
import os

# Cấu hình nguồn tham khảo
DOMAIN_TIERS = {
    "Tầng 1 (Chính thống VN)": ["gov.vn", "tapchiyhocduphong.vn", "vjmed.org.vn", "vjid.vn", "yhth.vn"],
    "Tầng 2 (Bệnh viện/Nhà thuốc VN)": ["nhathuoclongchau", "pharmacity", "vinmec", "medlatec", "tamanhhospital", "hongngochospital"],
    "Tầng 3 (Học thuật Quốc tế)": ["ncbi", "pubmed", "jamanetwork", "nejm", "thelancet"],
    "Tầng 4 (Tổ chức Y tế QT)": ["cdc.gov", "who.int", "nih.gov", "msdmanuals", "mayoclinic", "clevelandclinic", "hopkinsmedicine", "nhs.uk"]
}

def analyze_filtered_kg():
    print("[*] Đang đọc dữ liệu...")
    
    # 1. Đọc các file dữ liệu
    df_man_tinh = pd.read_csv('danh_sach_benh_man_tinh.csv')
    df_disease = pd.read_csv('disease_nodes.csv')
    df_edges = pd.read_csv('edges.csv', dtype=str)

    # 2. Chuẩn hóa tên để đối chiếu (tìm đúng node_id từ danh sách mã bệnh mãn tính)
    def clean_name(x):
        return str(x).lower().replace('\n', '').strip()

    df_man_tinh['clean_name'] = df_man_tinh['Ten_Benh'].apply(clean_name)
    df_disease['clean_name'] = df_disease['node_name'].apply(clean_name)

    # Ghép hai bảng để lấy ra danh sách các node_id HỢP LỆ (thuộc nhóm bệnh mãn tính)
    merged = pd.merge(df_disease, df_man_tinh, on='clean_name', how='inner')
    valid_disease_ids = set(merged['node_id'])
    
    # 3. LỌC: Chỉ lấy các cạnh liên quan đến node_id của bệnh mãn tính
    df_edges_filtered = df_edges[
        (df_edges['x_id'].isin(valid_disease_ids) & (df_edges['x_type'] == 'Disease')) |
        (df_edges['y_id'].isin(valid_disease_ids) & (df_edges['y_type'] == 'Disease'))
    ]

    total_edges = len(df_edges_filtered)
    
    # Gom tất cả các node từ x_id và y_id sau khi đã lọc
    x_nodes = df_edges_filtered[['x_id', 'x_type']].rename(columns={'x_id': 'id', 'x_type': 'type'})
    y_nodes = df_edges_filtered[['y_id', 'y_type']].rename(columns={'y_id': 'id', 'y_type': 'type'})
    df_nodes = pd.concat([x_nodes, y_nodes]).dropna().drop_duplicates(subset=['id'])
    
    total_nodes = len(df_nodes)
    
    print("="*70)
    print(" BÁO CÁO THỐNG KÊ ĐỒ THỊ (ĐÃ LỌC THEO DANH SÁCH BỆNH MÃN TÍNH)")
    print("="*70)
    
    print("\n[1] KÍCH THƯỚC ĐỒ THỊ (GRAPH SIZE):")
    print(f"  - Tổng số Cạnh (Edges): {total_edges:,}")
    print(f"  - Tổng số Đỉnh (Nodes): {total_nodes:,}")

    print("\n[2] PHÂN BỐ SỐ NODE & TỶ LỆ (%):")
    node_counts = df_nodes['type'].value_counts()
    for ntype, count in node_counts.items():
        pct = (count / total_nodes) * 100
        print(f"  - {ntype:15}: {count:<6,} nodes ({pct:5.2f}%)")
        
    total_diseases_in_graph = node_counts.get("Disease", 0)
    
    print("\n[3] THỐNG KÊ NGUỒN THAM KHẢO THEO TẦNG (%):")
    if 'source_url' in df_edges_filtered.columns:
        urls = df_edges_filtered['source_url'].dropna()
        def categorize_domain(url):
            url_str = str(url).lower()
            for tier_name, domains in DOMAIN_TIERS.items():
                if any(d in url_str for d in domains):
                    return tier_name
            return "Tầng 5 (Nguồn tự do/Khác)"
        tier_counts = urls.apply(categorize_domain).value_counts()
        for tier, count in tier_counts.items():
            pct = (count / len(urls)) * 100
            print(f"  - {tier:30}: {count:<6,} links ({pct:5.2f}%)")

    print("\n[4] ĐỘ TOÀN VẸN CỦA ĐỒ THỊ (GRAPH DENSITY):")
    if total_diseases_in_graph > 0:
        avg_degree = total_edges / total_diseases_in_graph
        print(f"  - Mật độ cạnh trung bình: {avg_degree:.2f} liên kết / 1 Bệnh")
        print("  - Phân tích độ \"dày\" trung bình cho 1 Bệnh:")
        for ntype in ['Drug', 'Symptom', 'Complication', 'DiagnosticTest', 'RiskFactor', 'Demographic', 'Intervention', 'Pathogen']:
            type_edges = df_edges_filtered[(df_edges_filtered['x_type'] == ntype) | (df_edges_filtered['y_type'] == ntype)]
            avg_per_disease = len(type_edges) / total_diseases_in_graph
            print(f"      + Có {avg_per_disease:4.1f} {ntype} / 1 Bệnh")
            
    print("\n[5] TỶ LỆ PHỦ SÓNG (DỰA TRÊN MÃ ICD-10 BỆNH MÃN TÍNH):")
    total_man_tinh = len(df_man_tinh)
    print(f"  - Tổng mã bệnh mãn tính trong danh sách: {total_man_tinh}")
    print(f"  - Số bệnh mãn tính đã có liên kết đồ thị: {total_diseases_in_graph}")
    if total_man_tinh > 0:
        print(f"  => Tiến độ bao phủ tập bệnh mãn tính : {(total_diseases_in_graph/total_man_tinh)*100:.2f}%")

if __name__ == "__main__":
    analyze_filtered_kg()

