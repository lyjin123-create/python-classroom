# [예제 5-1] 딕셔너리 기초 — 연락처 관리

contacts = {
    "김철수": "010-1234-5678",
    "이영희": "010-2345-6789",
    "박민수": "010-3456-7890"
}

print("📱 연락처")
print("=" * 30)

for name, phone in contacts.items():
    print(f"  {name}: {phone}")

print(f"\n김철수 번호: {contacts['김철수']}")

result = contacts.get("홍길동", "등록되지 않은 연락처")
print(f"홍길동 번호: {result}")

contacts["최지영"] = "010-4567-8901"
print(f"\n[추가] 최지영: {contacts['최지영']}")

contacts["김철수"] = "010-1111-2222"
print(f"[수정] 김철수: {contacts['김철수']}")

del contacts["박민수"]
print(f"\n[삭제 후] 총 {len(contacts)}명")
for name, phone in contacts.items():
    print(f"  {name}: {phone}")
