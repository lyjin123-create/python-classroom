# 📌 6차시: 불 자료형과 조건문

| 항목 | 내용 |
|:---:|------|
| **주제** | 불(bool), 비교 연산자, 논리 연산자, if/elif/else |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 5차시 (자료구조 전체) |
| **목표** | 조건에 따라 다른 코드를 실행할 수 있다 |

---

## 🎯 학습 목표

1. 불(bool) 자료형의 참/거짓을 이해한다
2. 비교 연산자와 논리 연산자를 사용할 수 있다
3. if-elif-else 조건문으로 분기를 만들 수 있다
4. 조건문을 활용한 실전 프로그램을 만들 수 있다

---

## 📖 강의 내용 (25분)

### 1. 불(Bool) 자료형

> 💡 **비유**: 불 자료형은 "스위치"입니다. 켜짐(True) 또는 꺼짐(False), 두 가지만 있어요!

```python
is_adult = True
is_raining = False

print(type(True))    # <class 'bool'>
print(type(False))   # <class 'bool'>
```

#### 파이썬의 참/거짓 규칙

| 거짓(False)으로 취급되는 값 | 참(True)으로 취급되는 값 |
|---|---|
| `False` | `True` |
| `0`, `0.0` | `0이 아닌 모든 숫자` |
| `""` (빈 문자열) | `"hello"` (내용 있는 문자열) |
| `[]` (빈 리스트) | `[1, 2]` (내용 있는 리스트) |
| `{}` (빈 딕셔너리) | `{"a": 1}` |
| `None` | 그 외 모든 값 |

---

### 2. 비교 연산자

| 연산자 | 의미 | 예시 | 결과 |
|:---:|------|:---:|:---:|
| `==` | 같다 | `5 == 5` | `True` |
| `!=` | 다르다 | `5 != 3` | `True` |
| `>` | 크다 | `5 > 3` | `True` |
| `<` | 작다 | `5 < 3` | `False` |
| `>=` | 크거나 같다 | `5 >= 5` | `True` |
| `<=` | 작거나 같다 | `3 <= 5` | `True` |

> ⚠️ **주의**: `=`는 대입, `==`는 비교! 헷갈리지 마세요!

---

### 3. 논리 연산자

| 연산자 | 의미 | 예시 | 결과 |
|:---:|------|:---:|:---:|
| `and` | 둘 다 참이면 참 | `True and True` | `True` |
| `or` | 하나만 참이면 참 | `True or False` | `True` |
| `not` | 반대로 | `not True` | `False` |

> 💡 **비유**:
> - `and` = "그리고" — 비도 오**고** 바람도 불면 → 나가지 말자
> - `or` = "또는" — 비가 오**거나** 바람이 불면 → 우산 가져가자
> - `not` = "아닌" — 비가 오지 **않으면** → 산책 가자

---

### 4. 조건문 if

```python
if 조건:
    # 조건이 참일 때 실행할 코드 (들여쓰기 필수!)
```

> ⚠️ **중요**: 파이썬에서 **들여쓰기**는 문법입니다! 스페이스 4칸 또는 탭 1개로 통일하세요.

---

### 5. if-elif-else

```python
if 조건1:
    # 조건1이 참이면
elif 조건2:
    # 조건2가 참이면
elif 조건3:
    # 조건3이 참이면
else:
    # 모든 조건이 거짓이면
```

> 💡 **비유**: 조건문 = 갈림길의 이정표 🪧
> "비가 오면 우산을 가져가고, 아니면 선글라스를 가져간다"

---

## 💻 실습 예제 (25분)

> 📂 예제 코드 파일: `examples/ex06_01.py` ~ `ex06_08.py`

---

### [예제 6-1] 비교·논리 연산자 연습

> 다양한 비교와 논리 연산을 직접 해봅시다.

```python
# === 비교 연산자 ===
x, y = 10, 20

print(f"x={x}, y={y}")
print(f"x == y: {x == y}")      # False
print(f"x != y: {x != y}")      # True
print(f"x > y: {x > y}")        # False
print(f"x < y: {x < y}")        # True
print(f"x >= 10: {x >= 10}")    # True
print(f"x <= 5: {x <= 5}")      # False

# 문자열 비교
print(f"\n'apple' == 'apple': {'apple' == 'apple'}")   # True
print(f"'Apple' == 'apple': {'Apple' == 'apple'}")     # False (대소문자 구분!)

# === 논리 연산자 ===
age = 25
has_id = True

print(f"\nage={age}, has_id={has_id}")
print(f"age >= 19 and has_id: {age >= 19 and has_id}")    # True
print(f"age >= 19 or has_id: {age >= 19 or has_id}")      # True
print(f"not has_id: {not has_id}")                         # False

# 복합 조건
score = 85
print(f"\nscore={score}")
print(f"80 <= score < 90: {80 <= score < 90}")   # True (파이썬만의 편리한 문법!)
```

> 🔑 **핵심**: 파이썬은 `80 <= score < 90` 같은 연속 비교가 가능합니다!

---

### [예제 6-2] 짝수/홀수 판별기

> 가장 기본적인 조건문을 작성해 봅시다.

```python
# 짝수/홀수 판별
number = int(input("정수를 입력하세요: "))

if number % 2 == 0:
    print(f"{number}은(는) 짝수입니다! 🟢")
else:
    print(f"{number}은(는) 홀수입니다! 🔵")

# 추가 판별
if number > 0:
    print(f"{number}은(는) 양수입니다.")
elif number < 0:
    print(f"{number}은(는) 음수입니다.")
else:
    print("0이네요!")

# 3의 배수 판별
if number != 0 and number % 3 == 0:
    print(f"{number}은(는) 3의 배수이기도 합니다!")
```

---

### [예제 6-3] 성적 등급 판정

> if-elif-else로 여러 조건을 분기해 봅시다.

```python
# 성적 등급 판정기
print("📊 성적 등급 판정기")
print("=" * 25)

score = int(input("점수를 입력하세요 (0~100): "))

# 유효 범위 검사
if score < 0 or score > 100:
    print("❌ 0~100 사이의 점수를 입력하세요!")
else:
    # 등급 판정
    if score >= 90:
        grade = "A"
        emoji = "🏆"
        comment = "훌륭합니다!"
    elif score >= 80:
        grade = "B"
        emoji = "👍"
        comment = "잘했어요!"
    elif score >= 70:
        grade = "C"
        emoji = "😊"
        comment = "보통이에요."
    elif score >= 60:
        grade = "D"
        emoji = "😅"
        comment = "좀 더 노력해요!"
    else:
        grade = "F"
        emoji = "😢"
        comment = "다시 도전하세요!"

    print(f"\n결과:")
    print(f"  점수: {score}점")
    print(f"  등급: {grade} {emoji}")
    print(f"  평가: {comment}")

    # 합격 여부
    if score >= 60:
        print(f"  ✅ 합격!")
    else:
        print(f"  ❌ 불합격 (60점 이상 필요)")
```

---

### [예제 6-4] 입장료 계산기

> 나이에 따라 다른 요금을 적용해 봅시다.

```python
# 놀이공원 입장료 계산기
print("🎢 놀이공원 입장료 계산기")
print("=" * 30)

age = int(input("나이를 입력하세요: "))

# 나이별 요금 체계
if age < 0:
    print("❌ 올바른 나이를 입력해주세요!")
elif age <= 3:
    price = 0
    category = "영유아 (무료)"
elif age <= 12:
    price = 15000
    category = "어린이"
elif age <= 18:
    price = 20000
    category = "청소년"
elif age <= 64:
    price = 30000
    category = "성인"
else:
    price = 15000
    category = "시니어"

if age >= 0:
    print(f"\n📋 입장권 정보")
    print(f"  나이: {age}세")
    print(f"  구분: {category}")
    print(f"  입장료: {price:,}원")

    # 추가 할인
    is_disabled = input("\n장애인 할인 적용? (y/n): ").strip().lower()
    if is_disabled == "y":
        discount = price * 0.5
        price -= discount
        print(f"  장애인 할인 (50%): -{discount:,.0f}원")

    is_local = input("지역주민 할인 적용? (y/n): ").strip().lower()
    if is_local == "y":
        discount = price * 0.2
        price -= discount
        print(f"  지역주민 할인 (20%): -{discount:,.0f}원")

    print(f"\n  💰 최종 금액: {price:,.0f}원")
```

---

### [예제 6-5] 윤년 판별기

> 복합 조건문으로 윤년을 판별해 봅시다.

```python
# 윤년 판별 규칙:
# 1) 4로 나누어떨어지면 윤년
# 2) 그 중 100으로 나누어떨어지면 평년
# 3) 그 중 400으로 나누어떨어지면 윤년

year = int(input("연도를 입력하세요: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"✅ {year}년은 윤년입니다! (2월 29일 있음)")
    days_in_feb = 29
else:
    print(f"❌ {year}년은 평년입니다. (2월 28일)")
    days_in_feb = 28

print(f"   {year}년 2월은 {days_in_feb}일까지 있습니다.")

# 확인용: 전후 윤년 찾기
print(f"\n📅 {year}년 근처 윤년:")
for y in range(year - 8, year + 9):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        marker = " ← 입력" if y == year else ""
        print(f"  {y}년{marker}")
```

> 💡 **팁**: 복잡한 조건은 괄호로 묶으면 읽기 쉽습니다!

---

### [예제 6-6] 가위바위보 게임

> 조건문 + random 모듈로 미니 게임을 만들어 봅시다.

```python
import random

print("✊✌️🖐️ 가위바위보 게임!")
print("=" * 25)

# 선택지
choices = ["가위", "바위", "보"]

# 사용자 입력
print("1. 가위  2. 바위  3. 보")
user_choice = int(input("선택하세요 (1/2/3): "))

if user_choice < 1 or user_choice > 3:
    print("❌ 1, 2, 3 중에서 선택하세요!")
else:
    user = choices[user_choice - 1]

    # 컴퓨터 선택 (랜덤)
    computer = random.choice(choices)

    print(f"\n🧑 나: {user}")
    print(f"🤖 컴퓨터: {computer}")
    print()

    # 승패 판정
    if user == computer:
        print("🤝 비겼습니다!")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        print("🎉 이겼습니다! 축하해요!")
    else:
        print("😢 졌습니다... 다시 도전하세요!")
```

> 💡 `random.choice(리스트)` — 리스트에서 무작위로 하나를 뽑습니다!

---

### [예제 6-7] 택배비 계산기

> 여러 조건(무게, 지역)을 조합하여 요금을 계산합시다.

```python
# 택배비 계산기
print("📦 택배비 계산기")
print("=" * 30)

weight = float(input("무게(kg)를 입력하세요: "))
print("배송 지역: 1.수도권  2.지방  3.제주/도서산간")
region = int(input("지역을 선택하세요 (1/2/3): "))

# 무게별 기본 요금
if weight <= 0:
    print("❌ 올바른 무게를 입력하세요!")
elif weight <= 2:
    base_price = 3000
    weight_category = "소형 (2kg 이하)"
elif weight <= 5:
    base_price = 5000
    weight_category = "중형 (5kg 이하)"
elif weight <= 10:
    base_price = 7000
    weight_category = "대형 (10kg 이하)"
elif weight <= 20:
    base_price = 10000
    weight_category = "특대형 (20kg 이하)"
else:
    print("❌ 20kg 초과는 접수가 불가합니다!")
    base_price = 0

if weight > 0 and weight <= 20:
    # 지역별 추가 요금
    if region == 1:
        region_name = "수도권"
        region_extra = 0
    elif region == 2:
        region_name = "지방"
        region_extra = 2000
    elif region == 3:
        region_name = "제주/도서산간"
        region_extra = 5000
    else:
        region_name = "알 수 없음"
        region_extra = 0

    total = base_price + region_extra

    print(f"\n📋 택배 요금 내역")
    print(f"  무게: {weight}kg ({weight_category})")
    print(f"  지역: {region_name}")
    print(f"  기본 요금: {base_price:,}원")
    print(f"  지역 추가: +{region_extra:,}원")
    print(f"  ─────────────────")
    print(f"  💰 총 요금: {total:,}원")
```

---

### [예제 6-8] 실전: 로그인 시스템

> ID/비밀번호를 검증하는 로그인 시스템을 만들어 봅시다.

```python
# 등록된 사용자 정보
users = {
    "admin": "1234",
    "user1": "python",
    "guest": "guest123",
}

print("🔐 로그인 시스템")
print("=" * 25)

# ID 입력
username = input("아이디: ").strip()

# ID 확인
if username not in users:
    print(f"\n❌ '{username}'은(는) 등록되지 않은 아이디입니다.")
    print("계정이 없으시면 회원가입을 해주세요.")
else:
    # 비밀번호 입력
    password = input("비밀번호: ")

    if password == users[username]:
        print(f"\n✅ 로그인 성공! {username}님 환영합니다! 🎉")

        # 관리자 권한 체크
        if username == "admin":
            print("🛡️ 관리자 권한으로 접속하셨습니다.")
            print("📋 등록된 사용자 목록:")
            for user in users:
                print(f"  - {user}")
        else:
            print("일반 사용자로 접속하셨습니다.")
    else:
        print("\n❌ 비밀번호가 틀렸습니다!")
        print("비밀번호를 잊으셨으면 관리자에게 문의하세요.")

# 조건부 표현식 (삼항 연산자) 소개
print("\n--- 조건부 표현식 (삼항 연산자) ---")
age = 20
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age} → {status}")

score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수: {score} → {result}")
```

> 💡 **조건부 표현식**: `값A if 조건 else 값B` — 한 줄로 조건 분기 가능!

---

## 🏆 도전 과제

### [도전 1] 커피숍 주문 시스템

```python
# 커피숍 주문 시스템
# 1. 메뉴 선택 (아메리카노/라떼/카푸치노/모카)
# 2. 사이즈 선택 (Small/Medium/Large)
# 3. 온도 선택 (Hot/Ice)
# 4. 총 가격 계산 & 출력

menu = {
    "아메리카노": 4000,
    "카페라떼": 4500,
    "카푸치노": 5000,
    "카페모카": 5500,
}

size_extra = {"S": 0, "M": 500, "L": 1000}

print("☕ 커피숍 주문 시스템")
print("=" * 30)

# 메뉴 출력
print("\n📋 메뉴:")
for i, (drink, price) in enumerate(menu.items(), 1):
    print(f"  {i}. {drink}: {price:,}원")

# 메뉴 선택
choice = int(input("\n메뉴 번호: "))
drink_names = list(menu.keys())
if 1 <= choice <= len(drink_names):
    selected = drink_names[choice - 1]
    base_price = menu[selected]

    # 사이즈 선택
    size = input("사이즈 (S/M/L): ").strip().upper()
    if size not in size_extra:
        size = "M"

    # 온도 선택
    temp = input("온도 (Hot/Ice): ").strip().capitalize()
    if temp not in ("Hot", "Ice"):
        temp = "Hot"

    # Ice는 +500원
    ice_extra = 500 if temp == "Ice" else 0

    # 총 가격
    total = base_price + size_extra[size] + ice_extra

    print(f"\n{'=' * 30}")
    print(f"🧾 주문 내역")
    print(f"  메뉴: {selected} ({temp})")
    print(f"  사이즈: {size}")
    print(f"  기본가: {base_price:,}원")
    if size_extra[size] > 0:
        print(f"  사이즈 추가: +{size_extra[size]:,}원")
    if ice_extra > 0:
        print(f"  아이스 추가: +{ice_extra:,}원")
    print(f"  ─────────────")
    print(f"  💰 총 금액: {total:,}원")
    print(f"{'=' * 30}")
else:
    print("❌ 올바른 메뉴 번호를 선택하세요!")
```

---

## 📝 6차시 요약

| 배운 것 | 설명 | 예시 |
|---------|------|------|
| `bool` | 참/거짓 | `True`, `False` |
| 비교 연산자 | 값 비교 | `==`, `!=`, `>`, `<` |
| 논리 연산자 | 조건 결합 | `and`, `or`, `not` |
| `if` | 조건이 참이면 실행 | `if x > 0:` |
| `elif` | 추가 조건 | `elif x == 0:` |
| `else` | 나머지 경우 | `else:` |
| 조건부 표현식 | 한 줄 조건 | `"짝" if x%2==0 else "홀"` |
| 들여쓰기 | 코드 블록 구분 | 스페이스 4칸 |

### 다음 시간 예고
> 7차시에서는 **반복문**을 배웁니다. 같은 작업을 수십, 수백 번 자동으로 반복하는 방법! while과 for를 배워 진정한 프로그래밍의 힘을 느껴보세요! 🔄
