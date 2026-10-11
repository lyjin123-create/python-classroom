import os

# [예제 9-8] CSV 파일 저장, 읽기 및 매출 분석

csv_filename = "sales_sample.csv"

# 1. 파일 쓰기
sample_data = """품목,수량,단가
아메리카노,12,4000
카페라떼,8,4500
초코머핀,5,3500
샌드위치,4,6500
"""

with open(csv_filename, "w", encoding="utf-8") as f:
    f.write(sample_data)

print(f"✅ '{csv_filename}' 파일 생성 완료\n")

# 2. 파일 읽기 및 집계
total_revenue = 0

print("📊 [일일 매출 분석 보고서]")
print("=" * 40)

with open(csv_filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")
    print(f" {header[0]:<8} | {header[1]:>4} | {header[2]:>6} | {'매출액':>8}")
    print("-" * 40)
    
    for line in lines[1:]:
        row = line.strip().split(",")
        item = row[0]
        qty = int(row[1])
        price = int(row[2])
        subtotal = qty * price
        total_revenue += subtotal
        print(f" {item:<8} | {qty:>4}개 | {price:>5,}원 | {subtotal:>7,}원")

print("=" * 40)
print(f" 💰 총 매출 합계: {total_revenue:>20,}원")

# 정리 (임시 파일 삭제)
if os.path.exists(csv_filename):
    os.remove(csv_filename)
