# [예제 4-2] 리스트 수정 — 할 일 목록 관리

# 할 일 목록
todo = ["이메일 확인", "보고서 작성", "회의 참석"]
print("📋 초기 목록:", todo)

# 1. 추가 — append (맨 뒤에)
todo.append("점심 약속")
print("\n[append] 점심 약속 추가:", todo)

# 2. 삽입 — insert (원하는 위치에)
todo.insert(1, "커피 마시기")
print("[insert] 커피 마시기 삽입:", todo)

# 3. 값 변경
todo[2] = "보고서 수정"
print("[변경] 보고서 수정으로 변경:", todo)

# 4. 삭제 — remove (값으로)
todo.remove("회의 참석")
print("[remove] 회의 참석 삭제:", todo)

# 5. 삭제 — pop (인덱스로, 꺼내기)
removed = todo.pop()
print(f"[pop] '{removed}' 꺼냄:", todo)

# 6. 삭제 — del (인덱스로)
del todo[0]
print("[del] 첫 번째 삭제:", todo)

# 7. 리스트 합치기
extra = ["운동하기", "독서하기"]
todo.extend(extra)
print("\n[extend] 추가 목록 합침:", todo)

todo = todo + ["일찍 자기"]
print("[+] 일찍 자기 추가:", todo)

print(f"\n최종 할 일: {len(todo)}개")
