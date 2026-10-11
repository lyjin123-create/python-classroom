# 📌 2차시: 변수와 자료형 — 숫자, 문자열

| 항목 | 내용 |
|:---:|------|
| **주제** | 변수, 숫자형(int, float), 문자열(str), 형변환, input() |
| **시간** | 50분 (강의 20분 + 실습 30분) |
| **선수 지식** | 1차시 (print, 연산자) |
| **목표** | 변수를 활용하고, 사용자 입력을 받아 처리한다 |

---

## 🎯 학습 목표

1. 변수의 개념을 이해하고 사용할 수 있다
2. 숫자형(정수, 실수)의 연산을 수행할 수 있다
3. 문자열의 기본 사용법을 익힌다
4. input()으로 사용자 입력을 받을 수 있다
5. 형변환(type casting)을 할 수 있다

---

## 📖 강의 내용 (20분)

### 1. 변수(Variable)란?

> 💡 **비유**: 변수는 "이름표가 붙은 상자"입니다. 상자에 값을 넣고, 이름으로 꺼내 쓸 수 있어요.

```python
name = "김파이"   # "name"이라는 상자에 "김파이"를 넣음
age = 25          # "age"라는 상자에 25를 넣음
```

#### `=`는 "같다"가 아니라 "대입(저장)"의 의미!
- 수학: `x = 5` → "x는 5와 같다"
- 파이썬: `x = 5` → "x라는 변수에 5를 저장해라"

#### 변수 이름 규칙

| 규칙 | 올바른 예 | 잘못된 예 |
|------|-----------|-----------|
| 문자, 숫자, 밑줄(_) 사용 가능 | `my_name`, `score1` | - |
| 숫자로 시작 불가 | `name1` | `1name` ❌ |
| 대소문자 구분 | `Name` ≠ `name` | - |
| 예약어 사용 불가 | `my_if` | `if`, `for`, `while` ❌ |
| 공백 사용 불가 | `my_name` | `my name` ❌ |

> 💡 **좋은 변수 이름**: 의미를 알 수 있는 이름이 좋아요!  
> `x = 25` (나쁨) → `age = 25` (좋음) → `student_age = 25` (더 좋음)

---

### 2. 숫자 자료형

| 자료형 | 설명 | 예시 |
|--------|------|------|
| `int` (정수) | 소수점 없는 숫자 | `1`, `-5`, `0`, `100` |
| `float` (실수) | 소수점 있는 숫자 | `3.14`, `-0.5`, `1.0` |

```python
x = 10       # int (정수)
y = 3.14     # float (실수)
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
```

---

### 3. 문자열 자료형

| 표기법 | 예시 |
|--------|------|
| 작은따옴표 | `'hello'` |
| 큰따옴표 | `"hello"` |
| 삼중 작은따옴표 | `'''여러 줄'''` |
| 삼중 큰따옴표 | `"""여러 줄"""` |

---

### 4. input() 함수

```python
name = input("이름을 입력하세요: ")
```

> ⚠️ **중요**: input()은 항상 **문자열(str)**로 반환합니다!  
> 숫자 계산을 하려면 `int()` 또는 `float()`로 변환해야 해요.

---

### 5. 형변환 (Type Casting)

| 함수 | 역할 | 예시 |
|------|------|------|
| `int()` | 정수로 변환 | `int("10")` → `10` |
| `float()` | 실수로 변환 | `float("3.14")` → `3.14` |
| `str()` | 문자열로 변환 | `str(100)` → `"100"` |
| `type()` | 자료형 확인 | `type(10)` → `<class 'int'>` |

---

## 💻 실습 예제 (30분)

> 📂 예제 코드 파일: `examples/ex02_01.py` ~ `ex02_10.py`

---

### [예제 2-1] 변수 기초 — 값 저장하고 사용하기

```python
# 변수에 값 저장하기
name = "파이썬"
age = 30
height = 175.5
is_student = True

# 변수 출력하기
print(name)       # 파이썬
print(age)        # 30
print(height)     # 175.5
print(is_student) # True

# 변수의 자료형 확인
print()
print("=== 자료형 확인 ===")
print(f"name의 타입: {type(name)}")       # <class 'str'>
print(f"age의 타입: {type(age)}")         # <class 'int'>
print(f"height의 타입: {type(height)}")   # <class 'float'>
print(f"is_student의 타입: {type(is_student)}")  # <class 'bool'>
```

> 🔑 **핵심**: `type()` 함수로 변수에 저장된 값의 종류(자료형)를 알 수 있어요.

---

### [예제 2-2] 변수 값 변경하기

```python
# 변수의 값은 언제든지 바꿀 수 있어요!
x = 10
print(f"처음 x = {x}")   # 10

x = 20
print(f"변경 후 x = {x}")  # 20

x = x + 5    # x에 5를 더한 결과를 다시 x에 저장
print(f"5를 더한 후 x = {x}")  # 25

# 여러 변수 한 줄에 대입
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# 같은 값을 여러 변수에 대입
x = y = z = 0
print(f"x={x}, y={y}, z={z}")
```

---

### [예제 2-3] 변수 값 교환 (Swap)

```python
# 두 변수의 값을 교환하기

# 다른 언어에서는 임시 변수가 필요하지만...
# temp = a
# a = b
# b = temp

# 파이썬은 한 줄이면 끝!
a = "사과"
b = "바나나"
print(f"교환 전: a={a}, b={b}")  # a=사과, b=바나나

a, b = b, a
print(f"교환 후: a={a}, b={b}")  # a=바나나, b=사과

# 숫자도 마찬가지!
x = 100
y = 200
x, y = y, x
print(f"x={x}, y={y}")  # x=200, y=100
```

> 💡 **파이썬만의 편리한 기능!** `a, b = b, a` 한 줄로 값을 교환할 수 있어요.

---

### [예제 2-4] 숫자 연산 — 복합 대입 연산자

```python
# 기본 연산
x = 10
y = 3

print(f"{x} + {y} = {x + y}")          # 13
print(f"{x} - {y} = {x - y}")          # 7
print(f"{x} × {y} = {x * y}")          # 30
print(f"{x} ÷ {y} = {x / y:.4f}")      # 3.3333
print(f"{x} ÷ {y}의 몫 = {x // y}")    # 3
print(f"{x} ÷ {y}의 나머지 = {x % y}") # 1
print(f"{x}의 {y}제곱 = {x ** y}")      # 1000

# 복합 대입 연산자 (축약 표현)
print("\n=== 복합 대입 연산자 ===")
score = 0
print(f"초기 점수: {score}")

score += 10    # score = score + 10
print(f"+10 후: {score}")    # 10

score += 20    # score = score + 20
print(f"+20 후: {score}")    # 30

score -= 5     # score = score - 5
print(f"-5 후: {score}")     # 25

score *= 2     # score = score * 2
print(f"×2 후: {score}")     # 50

score //= 3    # score = score // 3
print(f"÷3의 몫: {score}")   # 16
```

| 복합 대입 연산자 | 의미 | 예시 |
|:---:|------|:---:|
| `+=` | 더하고 저장 | `x += 3` = `x = x + 3` |
| `-=` | 빼고 저장 | `x -= 3` = `x = x - 3` |
| `*=` | 곱하고 저장 | `x *= 3` = `x = x * 3` |
| `/=` | 나누고 저장 | `x /= 3` = `x = x / 3` |
| `//=` | 몫 저장 | `x //= 3` = `x = x // 3` |
| `%=` | 나머지 저장 | `x %= 3` = `x = x % 3` |
| `**=` | 거듭제곱 저장 | `x **= 3` = `x = x ** 3` |

---

### [예제 2-5] 형변환 (Type Casting)

```python
# ========== 문자열 → 숫자 ==========
num_str = "100"
print(f"'{num_str}'의 타입: {type(num_str)}")  # str

# int()로 정수 변환
num_int = int(num_str)
print(f"int 변환 후: {num_int}, 타입: {type(num_int)}")
print(f"계산: {num_int + 50}")   # 150

# float()로 실수 변환
pi_str = "3.14"
pi = float(pi_str)
print(f"float 변환: {pi}, 타입: {type(pi)}")

# ========== 숫자 → 문자열 ==========
age = 25
# print("나는 " + age + "살")   # ❌ TypeError!
print("나는 " + str(age) + "살")   # ✅ OK
# 하지만 f-string을 쓰면 자동 변환!
print(f"나는 {age}살")              # ✅ 더 편리!

# ========== 정수 ↔ 실수 ==========
print(f"\nint(3.7) = {int(3.7)}")     # 3 (소수점 버림! 반올림 아님!)
print(f"int(3.2) = {int(3.2)}")       # 3
print(f"int(-3.7) = {int(-3.7)}")     # -3
print(f"float(5) = {float(5)}")       # 5.0

# ========== 주의: 변환 불가능한 경우 ==========
# int("hello")   # ❌ ValueError!
# int("3.14")    # ❌ ValueError! (소수점 있으면 int 직접 변환 불가)
# 해결: int(float("3.14")) → 3
print(f'int(float("3.14")) = {int(float("3.14"))}')
```

> ⚠️ **주의**: `int(3.7)`은 **반올림이 아니라 소수점 버림**입니다! 반올림은 `round(3.7)` → 4

---

### [예제 2-6] 문자열 만들기 — 따옴표 사용법

```python
# 작은따옴표
str1 = '작은따옴표 문자열'
print(str1)

# 큰따옴표
str2 = "큰따옴표 문자열"
print(str2)

# 문자열 안에 따옴표가 필요할 때
print("I'm a student")           # 큰따옴표 안에 작은따옴표
print('그는 "천재"라고 불린다')      # 작은따옴표 안에 큰따옴표
print("It\'s a beautiful day")    # 이스케이프 문자 사용

# 여러 줄 문자열 (삼중 따옴표)
menu = """
===== 오늘의 메뉴 =====
🍔 햄버거      5,000원
🍕 피자        12,000원
🍜 라멘         8,000원
🥗 샐러드       7,000원
========================
"""
print(menu)

# raw string (r"..."): 이스케이프 문자를 무시
print("일반: C:\\Users\\Documents")
print(r"Raw:  C:\Users\Documents")   # r을 붙이면 \를 그대로 출력
```

---

### [예제 2-7] input으로 사용자 입력 받기 — 기초

```python
# === 이름 입력받기 ===
name = input("이름을 입력하세요: ")
print(f"안녕하세요, {name}님! 반갑습니다! 😊")

# === 나이 입력받기 (형변환 필요!) ===
age_str = input("나이를 입력하세요: ")
print(f"  입력값: '{age_str}', 타입: {type(age_str)}")

age = int(age_str)   # 문자열 → 정수 변환!
print(f"  변환 후: {age}, 타입: {type(age)}")
print(f"  내년에는 {age + 1}살이 됩니다!")

# === 한 줄로 입력받고 바로 변환 ===
height = float(input("키(cm)를 입력하세요: "))
print(f"키: {height}cm")
```

> ⚠️ **가장 흔한 실수!**  
> input()은 항상 **문자열**을 돌려줍니다.  
> `"10" + "20"` = `"1020"` (문자열 연결)  
> `10 + 20` = `30` (숫자 덧셈)  
> 반드시 `int()` 또는 `float()`로 변환하세요!

---

### [예제 2-8] input 활용 — 간단한 인사 프로그램

```python
# 여러 정보를 입력받아 인사하는 프로그램
print("🎤 인터뷰 프로그램")
print("=" * 30)

name = input("이름이 뭐예요? ")
age = int(input("나이가 어떻게 되세요? "))
food = input("좋아하는 음식은? ")
color = input("좋아하는 색깔은? ")

print()
print("=" * 30)
print(f"📋 인터뷰 결과")
print("=" * 30)
print(f"🧑 이름: {name}")
print(f"🎂 나이: {age}세 (태어난 해: 약 {2024 - age}년)")
print(f"🍽️ 좋아하는 음식: {food}")
print(f"🎨 좋아하는 색깔: {color}")
print("=" * 30)
```

---

### [예제 2-9] 실전 예제 — 사칙연산 계산기

```python
# 두 수를 입력받아 사칙연산을 수행하는 계산기

print("🧮 간단한 계산기")
print("=" * 25)

num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))

print()
print(f"===== 계산 결과 =====")
print(f"  {num1} + {num2} = {num1 + num2}")
print(f"  {num1} - {num2} = {num1 - num2}")
print(f"  {num1} × {num2} = {num1 * num2}")

if num2 != 0:
    print(f"  {num1} ÷ {num2} = {num1 / num2:.4f}")
    print(f"  {num1} ÷ {num2}의 몫 = {num1 // num2:.0f}")
    print(f"  {num1} ÷ {num2}의 나머지 = {num1 % num2}")
else:
    print("  ⚠️ 0으로 나눌 수 없습니다!")

print(f"  {num1}의 {num2}제곱 = {num1 ** num2}")
print("=" * 22)
```

---

### [예제 2-10] 실전 예제 — 단위 변환기

```python
# 다양한 단위 변환

print("📏 단위 변환기")
print("=" * 30)

# 1. 센티미터 → 인치
cm = float(input("길이(cm)를 입력하세요: "))
inch = cm / 2.54
print(f"  {cm}cm = {inch:.2f}인치")

# 2. 킬로그램 → 파운드
kg = float(input("무게(kg)를 입력하세요: "))
lb = kg * 2.205
print(f"  {kg}kg = {lb:.2f}파운드")

# 3. 섭씨 → 화씨
celsius = float(input("온도(°C)를 입력하세요: "))
fahrenheit = celsius * 9/5 + 32
print(f"  {celsius}°C = {fahrenheit:.1f}°F")

print("=" * 30)
```

---

## 🏆 도전 과제

### [도전 1] BMI 계산기 만들기

> BMI = 몸무게(kg) ÷ 키(m)²

```python
print("📊 BMI 계산기")
print("=" * 30)

height_cm = float(input("키(cm)를 입력하세요: "))
weight = float(input("몸무게(kg)를 입력하세요: "))

# cm를 m로 변환
height_m = height_cm / 100

# BMI 계산
bmi = weight / (height_m ** 2)

print()
print(f"📋 결과")
print(f"  키: {height_cm}cm ({height_m:.2f}m)")
print(f"  몸무게: {weight}kg")
print(f"  BMI: {bmi:.1f}")
print()

# BMI 판정 (미리보기: 다음에 배울 if문!)
if bmi < 18.5:
    print("  판정: 저체중 🟡")
elif bmi < 25:
    print("  판정: 정상 🟢")
elif bmi < 30:
    print("  판정: 과체중 🟠")
else:
    print("  판정: 비만 🔴")
```

### [도전 2] 시간 변환 프로그램

```python
# 초(second)를 입력받아 시, 분, 초로 변환
total_seconds = int(input("초를 입력하세요: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"\n{total_seconds}초 = {hours}시간 {minutes}분 {seconds}초")
# 예: 3661초 = 1시간 1분 1초
```

---

## 📝 2차시 요약

| 배운 것 | 설명 | 예시 |
|---------|------|------|
| 변수 | 값을 저장하는 이름 붙은 상자 | `x = 10` |
| int | 정수 | `42`, `-5` |
| float | 실수 (소수점) | `3.14` |
| str | 문자열 | `"hello"` |
| `type()` | 자료형 확인 | `type(10)` → `int` |
| `input()` | 사용자 입력 (항상 str 반환) | `input("이름: ")` |
| `int()` | 정수로 변환 | `int("10")` |
| `float()` | 실수로 변환 | `float("3.14")` |
| `str()` | 문자열로 변환 | `str(100)` |
| f-string | 문자열 포매팅 | `f"나이: {age}"` |
| `+=` 등 | 복합 대입 연산자 | `x += 5` |

### 다음 시간 예고
> 3차시에서는 **문자열 심화**를 배웁니다. 문자열에서 특정 글자를 꺼내고(인덱싱), 일부분을 잘라내고(슬라이싱), 다양한 메서드로 변환하는 방법을 배워요! ✂️
