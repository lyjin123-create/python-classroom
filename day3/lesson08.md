# 📌 8차시: 함수 기초 (Functions)

| 항목 | 내용 |
|:---:|------|
| **주제** | 함수 정의(def), 매개변수, 리턴값, 기본값, 키워드 인수, 다중 반환 |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 7차시 (반복문) |
| **목표** | 나만의 함수를 정의하고 호출하여 코드를 구조화하고 재사용할 수 있다 |

---

## 🎯 학습 목표

1. 함수의 개념과 필요성(코드 재사용성, 모듈화)을 이해한다.
2. `def` 키워드로 함수를 정의하고, 매개변수와 `return`을 활용할 수 있다.
3. 매개변수 기본값(Default Parameter)과 키워드 인수를 사용할 수 있다.
4. 파이썬의 편리한 다중 값 반환(`return a, b`)을 활용할 수 있다.

---

## 📖 강의 내용 (25분)

### 1. 함수(Function)란?

> 💡 **비유**: 함수는 **"자판기"** 또는 **"요리 레시피"**입니다.  
> - **입력 (재료/동전)**: 매개변수(Parameter)  
> - **처리 (요리하기/음료 뽑기)**: 함수 내부 코드  
> - **출력 (완성된 요리/음료수)**: 반환값(Return)

매번 똑같은 긴 코드를 복사-붙여넣기 하는 대신, **이름을 붙여 묶어두고 필요할 때마다 이름만 불러서(호출) 실행**합니다.

---

### 2. 함수 정의와 호출

파이썬에서는 `def` 키워드로 함수를 만듭니다.

```python
"""
def 함수이름(매개변수1, 매개변수2, ...):
    실행할 코드
    return 반환값
"""

# 1) 가장 단순한 함수 (입력 X, 출력 X)
def say_hello():
    print("안녕하세요! 좋은 하루 되세요.")

say_hello()  # 호출


# 2) 매개변수가 있는 함수 (입력 O, 출력 X)
def greet(name):
    print(f"반갑습니다, {name}님!")

greet("홍길동")
greet("김철수")
```

---

### 3. return문 — "결과물을 돌려주기"

`print()`는 화면에 글자만 보여주는 것이고, `return`은 계산된 결과 데이터를 **함수를 호출한 곳으로 전달**합니다.

```python
def add(a, b):
    result = a + b
    return result

# return된 값을 변수에 담거나 다른 계산에 활용 가능!
total = add(10, 20)
print(f"합계: {total}")
print(f"합계에 5를 곱한 값: {total * 5}")
```

> ⚠️ **주의**: 함수 실행 중 `return`을 만나면 그 즉시 결과값을 전달하고 **함수는 종료**됩니다.

---

### 4. 매개변수 기본값 (Default Argument)

자주 쓰이는 기본값을 미리 정해두면, 인수를 생략하고 호출할 수 있습니다.

```python
def order_coffee(menu, size="Regular", ice=True):
    temp = "아이스" if ice else "따뜻한"
    print(f"주문 접수: [{temp}] {menu} ({size} 사이즈)")

order_coffee("아메리카노")                     # 기본값 사용 (Regular, 아이스)
order_coffee("카페라떼", size="Large")         # size만 변경
order_coffee("바닐라라떼", ice=False)          # 따뜻하게
```

> ⚠️ **규칙**: 기본값이 있는 매개변수는 **반드시 기본값이 없는 매개변수 뒤쪽에** 배치해야 합니다.

---

### 5. 키워드 인수 (Keyword Argument)

인수를 전달할 때 매개변수 이름을 명시하면, 순서를 바꿔서 전달해도 안전하게 들어갑니다.

```python
def create_user(name, age, city):
    print(f"이름: {name}, 나이: {age}, 거주지: {city}")

# 순서대로 전달 (위치 인수)
create_user("김철수", 30, "서울")

# 매개변수 이름으로 전달 (키워드 인수) - 순서 상관 없음!
create_user(city="부산", name="이영희", age=28)
```

---

### 6. 여러 값 반환하기 (Multiple Returns)

파이썬은 쉼표(`,`)를 이용해 여러 값을 동시에 반환할 수 있습니다. (실제로는 하나의 튜플로 반환 후 언패킹)

```python
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    mul_val = a * b
    return sum_val, diff_val, mul_val

# 언패킹으로 받기
s, d, m = calculate(10, 3)
print(f"합: {s}, 차: {d}, 곱: {m}")
```

---

## 💻 실습 예제 (25분)

### [예제 8-1] 기본 함수 만들기
- **실생활 시나리오**: 앱 시작 시 보여주는 헤더 배너 출력

```python
def print_banner():
    print("=" * 40)
    print("      ☕ 파이썬 스마트 카페 v1.0")
    print("=" * 40)

print_banner()
print("시스템이 정상 시작되었습니다.")
print_banner()
```

---

### [예제 8-2] 매개변수 활용 — 안내 메시지 전송
- **실생활 시나리오**: 카카오톡 알림톡 메시지 생성기

```python
def send_notification(user_name, service_name):
    msg = f"[{service_name}] 안녕하세요, {user_name}님! 예약이 완료되었습니다."
    print("📨 발송 메시지:", msg)

send_notification("김민수", "헬스장 PT")
send_notification("이지은", "치과 검진")
```

---

### [예제 8-3] return 활용 — 원의 넓이 계산
- **실생활 시나리오**: 피자 크기(반지름)에 따른 면적 계산

```python
def get_circle_area(radius):
    pi = 3.141592
    area = pi * (radius ** 2)
    return area

regular_pizza = get_circle_area(15)  # 반지름 15cm
large_pizza = get_circle_area(20)    # 반지름 20cm

print(f"레귤러 피자 넓이: {regular_pizza:.1f} cm²")
print(f"라지 피자 넓이: {large_pizza:.1f} cm²")
print(f"라지 피자가 약 {large_pizza / regular_pizza:.2f}배 더 큽니다!")
```

---

### [예제 8-4] 기본값 매개변수 — 배달비 계산기
- **실생활 시나리오**: 기본 배달료 3,000원에 비/눈 기상 악화 할증 적용

```python
def calc_delivery_fee(distance_km, is_bad_weather=False):
    base_fee = 3000
    
    # 거리 3km 초과 시 1km당 500원 추가
    if distance_km > 3:
        base_fee += (distance_km - 3) * 500
        
    # 날씨 할증
    if is_bad_weather:
        base_fee += 1500
        
    return base_fee

print("평상시 2km 배달비:", calc_delivery_fee(2), "원")
print("평상시 5km 배달비:", calc_delivery_fee(5), "원")
print("비오는 날 5km 배달비:", calc_delivery_fee(5, is_bad_weather=True), "원")
```

---

### [예제 8-5] 여러 값 반환 — 직사각형의 둘레와 넓이
- **실생활 시나리오**: 방 바닥 인테리어 견적용 치수 산출

```python
def get_room_metrics(width, height):
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area

w = 4.5  # 가로 4.5m
h = 3.0  # 세로 3.0m

peri, room_area = get_room_metrics(w, h)
print(f"가로 {w}m, 세로 {h}m 방:")
print(f"- 몰딩 둘레: {peri}m")
print(f"- 바닥 면적: {room_area}m² (약 {room_area / 3.3:.1f}평)")
```

---

### [예제 8-6] 실전: 세금 및 실수령액 계산 함수
- **실생활 시나리오**: 아르바이트 또는 프리랜서 3.3% 사업소득 원천징수 계산

```python
def calc_freelancer_pay(gross_pay):
    """급여에서 3.3% 원천징수액과 실수령액 계산"""
    tax_rate = 0.033
    tax = int(gross_pay * tax_rate)
    net_pay = gross_pay - tax
    return tax, net_pay

payment = 1500000  # 계약금 150만원
tax_amount, real_income = calc_freelancer_pay(payment)

print(f"💰 계약 금액: {payment:,}원")
print(f"📉 원천징수세액 (3.3%): {tax_amount:,}원")
print(f"💵 실제 통장 입금액: {real_income:,}원")
```

---

### [예제 8-7] 실전: 학생 성적 분석 함수
- **실생활 시나리오**: 시험 점수 리스트를 입력받아 평균과 등급을 계산

```python
def evaluate_scores(scores):
    avg = sum(scores) / len(scores)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
        
    return avg, grade

student_scores = [85, 92, 78, 88, 95]
avg_score, letter_grade = evaluate_scores(student_scores)

print(f"과목 점수들: {student_scores}")
print(f"평균 점수: {avg_score:.1f}점 / 최종 등급: {letter_grade}")
```

---

### [예제 8-8] 함수 조합 — 카페 주문 및 결제 시스템
- **실생활 시나리오**: 메뉴 계산 함수, 할인 함수, 영수증 출력 함수를 조합

```python
# 1. 가격 계산 함수
def get_item_price(item_name, qty):
    menu_prices = {"아메리카노": 4000, "카페라떼": 4500, "치즈케이크": 6000}
    return menu_prices.get(item_name, 0) * qty

# 2. 할인 적용 함수 (멤버십 10% 할인)
def apply_membership(total, is_member):
    if is_member:
        return int(total * 0.9)
    return total

# 3. 전체 주문 처리 함수
def process_order(item, qty, is_member=False):
    subtotal = get_item_price(item, qty)
    final_price = apply_membership(subtotal, is_member)
    
    print("--- 🧾 영수증 ---")
    print(f"품목: {item} x {qty}")
    print(f"주문 금액: {subtotal:,}원")
    if is_member:
        print(f"멤버십 할인 적용: -{subtotal - final_price:,}원")
    print(f"최종 결제 금액: {final_price:,}원")
    print("-----------------")

process_order("아메리카노", 2, is_member=True)
```

---

## 🏆 도전 과제: 만능 단위 변환 함수 모음

다음 4가지 변환 기능을 가진 함수들을 만들고 테스트해보세요.
1. `celsius_to_fahrenheit(c)`: 섭씨 → 화씨 ($F = C \times 1.8 + 32$)
2. `km_to_mile(km)`: 킬로미터 → 마일 ($1 \text{ km} \approx 0.621371 \text{ mile}$)
3. `kg_to_pound(kg)`: 킬로그램 → 파운드 ($1 \text{ kg} \approx 2.20462 \text{ lb}$)
4. `krw_to_usd(krw, rate=1350)`: 원화 → 달러 (환율 매개변수는 기본값 1,350원)

```python
def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32

def km_to_mile(km):
    return km * 0.621371

def kg_to_pound(kg):
    return kg * 2.20462

def krw_to_usd(krw, rate=1350):
    return krw / rate

# 테스트
print(f"섭씨 25°C = 화씨 {celsius_to_fahrenheit(25):.1f}°F")
print(f"10 km = {km_to_mile(10):.2f} mile")
print(f"70 kg = {kg_to_pound(70):.1f} lb")
print(f"100,000원 = ${krw_to_usd(100000):.2f} (환율 1350원 기준)")
```

---

## 📝 핵심 요약 정리

1. **`def 함수이름(매개변수):`**: 함수를 선언하는 키워드.
2. **`return`**: 결과 데이터를 호출자에게 돌려주며 함수를 종료함.
3. **기본값 매개변수**: 생략 시 사용할 값을 지정하며, 일반 매개변수 뒤쪽에 위치해야 함.
4. **키워드 인수**: `함수(이름=값)` 형태로 순서에 구애받지 않고 명확하게 전달 가능.
5. **다중 반환**: `return a, b`처럼 쉼표로 여러 값을 반환할 수 있음 (튜플 언패킹).
