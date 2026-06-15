import pandas as pd
from neo4j import GraphDatabase
import os

# ================= CẤU HÌNH KẾT NỐI =================
# Thay đổi URL và Password cho đúng với Neo4j của bạn
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "MatKhauCuaBan123") 

# Đường dẫn tới thư mục chứa dữ liệu của bạn
OUTPUT_DIR = "/home/adroot/data_mantinh/data/kg_output"
EDGES_FILE = os.path.join(OUTPUT_DIR, "edges.csv")
DISEASE_NODES_FILE = os.path.join(OUTPUT_DIR, "disease_nodes.csv")

# ================= HÀM XỬ LÝ =================
def clear_database(session):
    print("[-] Đang xóa dữ liệu cũ để làm mới hoàn toàn...")
    session.run("MATCH (n) DETACH DELETE n")
    print("[v] Đã dọn sạch database.")

def import_graph_topology(session, df_edges):
    print(f"[-] Đang nạp {len(df_edges)} cạnh và tạo các Node từ edges.csv...")
    
    # Gom nhóm theo loại thực thể và loại quan hệ để tạo Cypher động
    # Ví dụ: x_type='Disease', y_type='Symptom', relation='HAS_SYMPTOM'
    grouped = df_edges.groupby(['x_type', 'y_type', 'relation'])
    
    for (x_type, y_type, rel), group in grouped:
        # Chuẩn bị dữ liệu dạng list of dicts
        batch = group[['x_id', 'x_name', 'y_id', 'y_name', 'evidence', 'source_url']].fillna("").to_dict('records')
        
        # Câu lệnh Cypher: Dùng MERGE để không tạo trùng lặp Node
        query = f"""
        UNWIND $batch AS row
        // 1. Tạo hoặc tìm Node X
        MERGE (x:{x_type} {{node_id: row.x_id}})
        ON CREATE SET x.node_name = row.x_name
        
        // 2. Tạo hoặc tìm Node Y
        MERGE (y:{y_type} {{node_id: row.y_id}})
        ON CREATE SET y.node_name = row.y_name
        
        // 3. Nối quan hệ giữa X và Y
        MERGE (x)-[r:{rel}]->(y)
        SET r.evidence = row.evidence,
            r.source_url = row.source_url
        """
        session.run(query, batch=batch)
    print("[v] Hoàn tất xây dựng bộ khung Đồ thị!")

def enrich_disease_nodes(session, df_disease):
    print(f"[-] Đang bổ sung thông tin ICD-10 cho {len(df_disease)} bệnh...")
    batch = df_disease[['node_id', 'icd10_full', 'node_description']].fillna("").to_dict('records')
    
    query = """
    UNWIND $batch AS row
    MATCH (d:Disease {node_id: row.node_id})
    SET d.icd10_full = row.icd10_full,
        d.node_description = row.node_description
    """
    session.run(query, batch=batch)
    print("[v] Hoàn tất cập nhật thông tin chi tiết!")

# ================= CHẠY CHƯƠNG TRÌNH =================
def main():
    if not os.path.exists(EDGES_FILE):
        print(f"Lỗi: Không tìm thấy {EDGES_FILE}")
        return

    df_edges = pd.read_csv(EDGES_FILE, dtype=str)
    df_disease = pd.read_csv(DISEASE_NODES_FILE, dtype=str) if os.path.exists(DISEASE_NODES_FILE) else pd.DataFrame()

    # Kết nối Neo4j
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            # 1. Dọn dẹp nhà cửa (Bỏ comment dòng dưới nếu muốn giữ data cũ)
            clear_database(session)
            
            # 2. Đổ edges (Tạo ra tất cả Bệnh, Triệu chứng, Thuốc... và nối chúng lại)
            import_graph_topology(session, df_edges)
            
            # 3. Đắp thêm da thịt cho Node Bệnh (Thêm mã ICD-10 full, mô tả...)
            if not df_disease.empty:
                enrich_disease_nodes(session, df_disease)

    print("\n=== XONG! KHỞI TẠO GRAPH RAG THÀNH CÔNG ===")
    print("Bây giờ bạn có thể mở http://localhost:7474 để xem thành quả đồ thị siêu đẹp của mình!")

if __name__ == "__main__":
    main()
