# 📌 7차시: 반복문 (Loops)

| 항목 | 내용 |
|:---:|------|
| **주제** | while문, for문, range(), break, continue, 리스트 컴프리헨션 |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 6차시 (조건문, bool) |
| **목표** | 반복 작업을 파이썬 코드로 자동화하고 흐름을 제어할 수 있다 |

---

## 🎯 학습 목표

1. `while`문의 동작 원리와 무한루프 방지법을 이해한다.
2. `for`문과 `range()`를 활용하여 지정된 횟수나 데이터 시퀀스를 순회할 수 있다.
3. `break`와 `continue`로 반복문 흐름을 세밀하게 제어한다.
4. 중첩 반복문과 리스트 컴프리헨션(List Comprehension) 기초를 익힌다.

---

## 📖 강의 내용 (25분)

### 1. 반복문이란?

> 💡 **비유**: 알람 시계의 "5분 뒤 다시 울림(스누즈)" 기능이나, 세탁기가 "탈수를 3회 반복"하는 것과 같습니다.  
> 똑같은 일을 사람이 100번 타이핑하는 대신, 컴퓨터에게 **"조건이 맞을 때까지 반복해줘"**라고 시키는 명령입니다.

```python
# 반복문이 없다면:
print("안녕하세요!")
print("안녕하세요!")
print("안녕하세요!")
# 100번 쓰려면 100줄 필요!

# 반복문이 있다면:
for i in range(100):
    print("안녕하세요!")  # 단 2줄로 해결!
```

---

### 2. while문 — "~하는 동안 계속 반복"

조건이 `True`인 동안 코드 블록을 계속 반복 실행합니다.

```python
"""
while 조건:
    반복할 코드
    조건을 바꿀 코드 (카운터 증가 등)
"""

count = 1
while count <= 5:
    print(f"{count}번째 반복 중...")
    count += 1  # ★ 매우 중요: 카운터를 안 올리면 무한루프(Infinite Loop) 발생!

print("반복 종료!")
```

> ⚠️ **주의: 무한 루프 탈출법**  
> 실수로 코드가 영원히 멈추지 않는다면 터미널에서 **`Ctrl + C`**를 누르면 강제 종료됩니다.

---

### 3. for문과 range() — "정해진 횟수나 항목 순회"

파이썬의 `for`문은 리스트, 문자열, 범위 등 컬렉션의 요소를 **하나씩 꺼내며** 반복합니다.

```python
# 1) 리스트 순회
fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    print(f"과일: {fruit}")

# 2) range() 함수
# range(stop): 0부터 stop-1까지
# range(start, stop): start부터 stop-1까지
# range(start, stop, step): step 간격으로

for i in range(3):        # 0, 1, 2
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)
```

---

### 4. break와 continue

반복문의 흐름을 즉시 바꾸는 특별한 키워드입니다.

- **`break`**: "당장 여기서 반복문을 완전히 탈출해라!"
- **`continue`**: "이번 차례는 여기서 건너뛰고, 다음 반복으로 넘어가라!"

```python
# break 예시: 3을 만나면 즉시 종료
for num in range(1, 6):
    if num == 3:
        print("3 발견! 반복 중단!")
        break
    print(num)
# 출력: 1, 2

# continue 예시: 짝수는 건너뛰고 홀수만 출력
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)
# 출력: 1, 3, 5
```

---

### 5. 중첩 반복문 (Nested Loops)

반복문 안에 또 다른 반복문이 들어가는 구조입니다. (시계의 분침과 초침 관계)

```python
# 구구단 2단~3단
for dan in range(2, 4):
    print(f"=== {dan}단 ===")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
```

---

### 6. 리스트 컴프리헨션 (List Comprehension) 맛보기

파이썬다운 간결하고 강력한 리스트 생성 문법입니다.

```python
# 일반 방식
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# 리스트 컴프리헨션 방식 (단 한 줄!)
squares = [x ** 2 for x in range(1, 6)]
# 결과: [1, 4, 9, 16, 25]

# 조건문 포함: 1~10 중 짝수만
evens = [x for x in range(1, 11) if x % 2 == 0]
# 결과: [2, 4, 6, 8, 10]
```

---

## 💻 실습 예제 (25분)

### [예제 7-1] 카운트다운 타이머 (`while`)
- **실생활 시나리오**: 로켓 발사 카운트다운 또는 전자레인지 타이머

```python
sec = 5
print("🚀 카운트다운 시작!")

while sec > 0:
    print(f"{sec}초 전...")
    sec -= 1

print("🎉 발사! (새해 복 많이 받으세요!)")
```

---

### [예제 7-2] 로그인 비밀번호 3회 시도 (`while + input`)
- **실생활 시나리오**: 스마트폰 화면 잠금 3회 실패 시 잠김

```python
correct_pw = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pw = input(f"비밀번호를 입력하세요 ({attempts + 1}/{max_attempts}): ")
    if pw == correct_pw:
        print("🔓 로그인 성공! 환영합니다.")
        break
    else:
        print("❌ 비밀번호가 틀렸습니다.")
        attempts += 1

if attempts == max_attempts:
    print("🔒 3회 실패로 계정이 잠겼습니다. 고객센터에 문의하세요.")
```

---

### [예제 7-3] 누적 합계 계산 (`for + range`)
- **실생활 시나리오**: 1일부터 30일까지 매일 저축하는 금액 합산

```python
# 1부터 100까지의 합
total = 0
for i in range(1, 101):
    total += i

print(f"1부터 100까지의 총합: {total}")  # 5050
```

---

### [예제 7-4] 장보기 영수증 정산 (`for + 리스트/딕셔너리`)
- **실생활 시나리오**: 마트 카트에 담긴 물품과 가격 영수증 출력

```python
cart = [
    {"item": "사과 1봉지", "price": 5900, "qty": 1},
    {"item": "신선우유 1L", "price": 2800, "qty": 2},
    {"item": "통밀빵", "price": 3200, "qty": 1},
    {"item": "계란 30구", "price": 7500, "qty": 1}
]

print("🧾 [이마트] 구매 영수증")
print("=" * 35)

total_price = 0
for product in cart:
    subtotal = product["price"] * product["qty"]
    total_price += subtotal
    print(f"{product['item']:<12} {product['qty']}개  {subtotal:>7,}원")

print("-" * 35)
print(f"총 결제 금액: {total_price:>18,}원")
```

---

### [예제 7-5] 숫자 맞추기 UP/DOWN 게임 (`break + random`)
- **실생활 시나리오**: 1~100 사이의 비밀 숫자를 맞추는 미니게임

```python
import random

target = random.randint(1, 100)
count = 0

print("🎮 1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    guess = int(input("숫자 입력: "))
    count += 1
    
    if guess < target:
        print("⬆️ UP! 더 큰 숫자입니다.")
    elif guess > target:
        print("⬇️ DOWN! 더 작은 숫자입니다.")
    else:
        print(f"🎯 정답입니다! ({target})")
        print(f"총 {count}번 만에 맞추셨습니다!")
        break
```

---

### [예제 7-6] 구구단 표 출력 (`중첩 for문`)
- **실생활 시나리오**: 2단부터 9단까지 깔끔하게 출력하기

```python
for dan in range(2, 10):
    print(f"[{dan}단]", end="\t")
print()
print("-" * 65)

for i in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan}x{i}={dan*i:2d}", end="\t")
    print()
```

---

### [예제 7-7] 별 찍기 패턴 (직각삼각형, 피라미드)
- **실생활 시나리오**: 콘솔 UI 레이아웃 표현

```python
# 직각삼각형
print("--- 직각삼각형 ---")
for i in range(1, 6):
    print("*" * i)

# 피라미드 (공백 + 별)
print("\n--- 피라미드 ---")
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

---

### [예제 7-8] 리스트 컴프리헨션 실전
- **실생활 시나리오**: 회원 명단 가공 및 할인율 적용

```python
# 1. 10% 할인 가격 리스트 만들기
prices = [10000, 25000, 48000, 15000]
discounted = [int(p * 0.9) for p in prices]
print("할인가 목록:", discounted)

# 2. VIP 회원(점수 80점 이상) 명단만 추출
members = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 72},
    {"name": "박민수", "score": 95},
    {"name": "최유진", "score": 68}
]

vip_list = [m["name"] for m in members if m["score"] >= 80]
print("🌟 VIP 회원 명단:", vip_list)
```

---

## 🏆 도전 과제: 은행 ATM 시뮬레이터

사용자가 종료할 때까지 입금, 출금, 잔액 확인을 반복 수행하는 콘솔 ATM 프로그램을 작성하세요.

```python
balance = 10000  # 기본 잔액: 10,000원

while True:
    print("\n" + "=" * 30)
    print("🏧 KB국민은행 ATM")
    print("1. 잔액 조회  2. 입금  3. 출금  4. 종료")
    print("=" * 30)
    
    choice = input("원하시는 서비스 번호를 입력하세요: ")
    
    if choice == "1":
        print(f"💰 현재 잔액은 {balance:,}원 입니다.")
    elif choice == "2":
        amount = int(input("입금하실 금액을 입력하세요: "))
        if amount > 0:
            balance += amount
            print(f"✅ {amount:,}원이 입금되었습니다. 현재 잔액: {balance:,}원")
        else:
            print("⚠️ 0원 이상 입력해야 합니다.")
    elif choice == "3":
        amount = int(input("출금하실 금액을 입력하세요: "))
        if amount > balance:
            print("❌ 잔액이 부족합니다!")
        elif amount <= 0:
            print("⚠️ 0원 이상 입력해야 합니다.")
        else:
            balance -= amount
            print(f"💸 {amount:,}원이 출금되었습니다. 현재 잔액: {balance:,}원")
    elif choice == "4":
        print("👋 이용해주셔서 감사합니다. 카드를 챙겨주세요.")
        break
    else:
        print("⚠️ 올바른 번호(1~4)를 선택해주세요.")
```

---

## 📝 핵심 요약 정리

1. **`while 조건:`**: 조건이 참인 동안 반복, 루프 탈출 조건(카운터 등) 필수.
2. **`for 변수 in 시퀀스:`**: 시퀀스(리스트, 문자열 등)나 `range()`의 원소를 하나씩 꺼내며 반복.
3. **`range(start, stop, step)`**: stop 값은 **포함되지 않음**에 주의.
4. **`break`**: 루프 즉시 탈출 / **`continue`**: 이번 턴 건너뛰기.
5. **리스트 컴프리헨션**: `[표현식 for 변수 in 시퀀스 if 조건]`으로 코드를 간결하고 파이썬답게 작성.
