# print의 end와 sep 옵션

# end: 출력 끝에 붙는 문자 변경 (기본값: 줄바꿈 \n)
print("Hello", end=" ")
print("World")         # Hello World (한 줄에 출력됨!)
print()                 # 빈 줄

# end 활용: 카운트다운
print("발사 카운트다운: ", end="")
print(5, end="...")
print(4, end="...")
print(3, end="...")
print(2, end="...")
print(1, end="...")
print("🚀 발사!")
print()

# sep: 여러 값 사이의 구분자 변경 (기본값: 공백 " ")
print("2024", "01", "15", sep="-")      # 2024-01-15
print("010", "1234", "5678", sep="-")   # 010-1234-5678
print("서울", "부산", "대구", sep=" → ")  # 서울 → 부산 → 대구
print("A", "B", "C", "D", sep="")       # ABCD (구분자 없음)
