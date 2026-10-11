# [예제 4-1] 리스트 생성과 접근 — 장보기 목록

# 장보기 목록 만들기
grocery = ["우유", "계란", "빵", "치즈", "버터"]

# 전체 출력
print("🛒 장보기 목록:", grocery)
print(f"총 {len(grocery)}개 항목")

# 인덱싱으로 접근
print(f"\n첫 번째: {grocery[0]}")
print(f"마지막: {grocery[-1]}")
print(f"세 번째: {grocery[2]}")

# 슬라이싱
print(f"\n처음 3개: {grocery[:3]}")
print(f"뒤에서 2개: {grocery[-2:]}")

# 리스트 길이
print(f"\n목록 길이: {len(grocery)}")

# 포함 여부 확인 (in 연산자)
print(f"\n'우유'가 목록에 있나요? {'우유' in grocery}")
print(f"'사과'가 목록에 있나요? {'사과' in grocery}")
