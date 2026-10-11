# 여러 줄 문자열과 문자열 연산

# 여러 줄 문자열 (삼중 따옴표)
poem = """
장미는 빨갛고,
제비꽃은 파랗다.
파이썬은 멋지고,
나도 그렇다!
"""
print(poem)

# 문자열 더하기 (+) = 문자열 연결
first_name = "김"
last_name = "파이"
full_name = first_name + last_name
print("이름:", full_name)        # 이름: 김파이

# 문자열 곱하기 (*) = 문자열 반복
line = "=" * 30
print(line)                      # ==============================
print("⭐" * 10)                # ⭐ 10개
print("하하 " * 3)              # 하하 3번 반복

# 문자열 길이 (len 함수)
greeting = "Hello, Python!"
print(f"'{greeting}'의 길이: {len(greeting)}자")  # 14자
