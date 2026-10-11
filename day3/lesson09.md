# 📌 9차시: 함수 심화 & 파일 I/O

| 항목 | 내용 |
|:---:|------|
| **주제** | 지역/전역 변수(Scope), *args, **kwargs, 람다, 파일 읽기/쓰기(`with`문) |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 8차시 (함수 기초) |
| **목표** | 가변 인수를 다루고, 텍스트 파일을 읽고 써서 데이터를 영구 보관할 수 있다 |

---

## 🎯 학습 목표

1. 지역 변수(Local)와 전역 변수(Global)의 차이 및 변수의 유효 범위(Scope)를 이해한다.
2. `*args`와 `**kwargs`로 개수가 정해지지 않은 다양한 입력을 유연하게 처리한다.
3. 람다(lambda) 함수를 활용하여 한 줄 함수와 정렬 키(key)를 작성할 수 있다.
4. `open()` 함수와 `with` 문을 이용해 파일을 읽고(`'r'`), 새로 쓰고(`'w'`), 덧붙이는(`'a'`) 방법을 마스터한다.

---

## 📖 강의 내용 (25분)

### 1. 변수의 유효 범위 (Scope: 지역변수 vs 전역변수)

> 💡 **비유**: 
> - **지역 변수 (Local)**: 내 집(방 안)에서만 쓸 수 있는 개인 슬리퍼 🩴 (함수 안에서만 존재)
> - **전역 변수 (Global)**: 아파트 단지 공용 놀이터 벤치 🪑 (프로그램 전체 어디서나 접근 가능)

```python
total = 100  # 전역 변수 (Global)

def my_func():
    count = 10       # 지역 변수 (Local)
    print(total)     # 읽기 가능: 100
    print(count)     # 10

my_func()
# print(count)       # ❌ Error! count는 함수 밖에서는 존재하지 않음!
```

> ⚠️ **주의 (`global` 키워드)**: 함수 안에서 전역 변수의 값을 직접 바꾸려면 `global total`을 써야 하지만, 코드가 꼬이기 쉬워 실무에서는 함수에 매개변수로 전달하고 `return`으로 받아 업데이트하는 패턴을 권장합니다.

---

### 2. 가변 인수: `*args`와 `**kwargs`

인수가 몇 개 들어올지 미리 알 수 없을 때 사용합니다.

#### 1) `*args` (Arguments)
- 여러 개의 위치 인수를 **튜플(tuple)**로 한꺼번에 묶어서 받습니다.

```python
def print_all(*args):
    print("받은 데이터:", args)
    for item in args:
        print(f"- {item}")

print_all("사과", "바나나", "포도")
print_all(1, 2, 3, 4, 5, 6)
```

#### 2) `**kwargs` (Keyword Arguments)
- `키=값` 형태의 여러 인수를 **딕셔너리(dict)**로 한꺼번에 받습니다.

```python
def print_profile(**kwargs):
    print("사용자 프로필:")
    for key, val in kwargs.items():
        print(f"  {key}: {val}")

print_profile(name="김철수", age=28, job="개발자", city="서울")
```

---

### 3. 람다(Lambda) 함수 — 한 줄 익명 함수

이름 없이 간단하게 한 줄로 작성하는 함수입니다. 주로 `sort()`, `map()`, `filter()`의 인수로 자주 쓰입니다.

```python
# 일반 함수
def add(a, b):
    return a + b

# 람다 함수: lambda 매개변수: 반환표현식
add_lambda = lambda a, b: a + b
print(add_lambda(3, 5))  # 8

# 실전 사용: 리스트 정렬 기준 지정
students = [("김철수", 80), ("이영희", 95), ("박민수", 70)]
# 점수(튜플의 1번째 요소) 기준으로 정렬
students.sort(key=lambda s: s[1], reverse=True)
print(students)  # [('이영희', 95), ('김철수', 80), ('박민수', 70)]
```

---

### 4. 파일 입출력 (File I/O)

프로그램이 종료되어도 데이터를 컴퓨터 하드디스크에 **영구 보관**하기 위해 파일을 사용합니다.

| 모드 | 의미 | 설명 |
|:---:|:---:|------|
| `'r'` | Read (읽기) | 파일이 없으면 에러 발생 |
| `'w'` | Write (새로 쓰기) | 파일이 있으면 내용 덮어씀 (기존 내용 삭제됨) |
| `'a'` | Append (덧붙이기) | 기존 파일 끝에 새 내용을 추가 |

#### `with` 문의 마법 (★ 표준 권장)
`file.close()`를 깜빡하면 파일이 손상되거나 잠길 수 있습니다. `with` 문을 사용하면 블록을 빠져나갈 때 **자동으로 파일을 안전하게 닫아줍니다**.

```python
# 파일 쓰기 (utf-8 인코딩 필수: 한글 깨짐 방지)
with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 파일 저장 성공!\n")

# 파일 읽기
with open("memo.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

## 💻 실습 예제 (25분)

### [예제 9-1] 지역변수와 전역변수
- **실생활 시나리오**: 상점 포인트 전역 관리 vs 주문별 할인 로컬 계산

```python
total_store_points = 1000  # 상점 전체 누적 포인트

def earn_points(customer_name, spent_money):
    global total_store_points
    # 적립 포인트 (이 함수 안에서만 쓰이는 로컬 변수)
    earned = int(spent_money * 0.05)
    total_store_points += earned
    print(f"{customer_name}님 적립: +{earned}P")

earn_points("홍길동", 50000)
earn_points("김영희", 20000)
print(f"상점 총 적립된 포인트: {total_store_points}P")
```

---

### [예제 9-2] `*args` 활용 — 다중 점수 평균 계산기
- **실생활 시나리오**: 과목 수가 3개든 7개든 상관없이 모든 점수의 평균 구하기

```python
def calc_average(*scores):
    if not scores:
        return 0
    total = sum(scores)
    count = len(scores)
    return total / count

print("3과목 평균:", calc_average(90, 85, 95))
print("5과목 평균:", calc_average(80, 75, 90, 85, 100))
print("입력 없음:", calc_average())
```

---

### [예제 9-3] `**kwargs` 활용 — 맞춤형 회원 등록
- **실생활 시나리오**: 필수 정보 외에 선택 입력 항목(취미, 차량유무 등) 자유롭게 저장

```python
def register_member(name, phone, **extra_info):
    member = {
        "name": name,
        "phone": phone,
        "extra": extra_info
    }
    print(f"✅ 회원 등록 완료: {name} ({phone})")
    for key, val in extra_info.items():
        print(f"   - {key}: {val}")
    return member

m1 = register_member("이민호", "010-1111-2222", email="minho@test.com", hobby="등산")
m2 = register_member("박신혜", "010-3333-4444", car=True, city="경기 성남", vip_level="Gold")
```

---

### [예제 9-4] 람다 함수와 데이터 정렬
- **실생활 시나리오**: 온라인 쇼핑몰 상품 목록 정렬 (가격순, 리뷰수 순)

```python
products = [
    {"name": "무선 마우스", "price": 25000, "reviews": 120},
    {"name": "기계식 키보드", "price": 89000, "reviews": 45},
    {"name": "모니터 거치대", "price": 32000, "reviews": 310},
    {"name": "C타입 케이블", "price": 8900, "reviews": 540}
]

# 1. 가격 낮은 순 정렬
by_price = sorted(products, key=lambda p: p["price"])
print("💰 가격 낮은 순:")
for p in by_price:
    print(f"  {p['name']}: {p['price']:,}원")

# 2. 리뷰 많은 순 정렬
by_reviews = sorted(products, key=lambda p: p["reviews"], reverse=True)
print("\n⭐ 리뷰 많은 순:")
for p in by_reviews:
    print(f"  {p['name']}: {p['reviews']}개")
```

---

### [예제 9-5] 파일 쓰기 (`'w'`) — 오늘 하루 한 줄 일기장
- **실생활 시나리오**: 사용자에게 입력을 받아 텍스트 파일로 저장하기

```python
filename = "daily_diary.txt"

print("📖 오늘 하루를 기록해보세요!")
entry = input("한 줄 일기: ")
weather = input("오늘 날씨: ")

with open(filename, "w", encoding="utf-8") as f:
    f.write("=== 나의 일기장 ===\n")
    f.write(f"날씨: {weather}\n")
    f.write(f"내용: {entry}\n")

print(f"✅ '{filename}' 파일에 안전하게 저장되었습니다.")
```

---

### [예제 9-6] 파일 읽기 (`'r'`) — 저장된 파일 내용 출력
- **실생활 시나리오**: 저장된 일기장 파일 내용을 읽어와 화면에 표시

```python
filename = "daily_diary.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()  # 줄 단위 리스트로 읽기
        
    print(f"\n📂 [{filename}] 내용 불러오기:")
    for line in lines:
        print(line, end="")  # line 자체에 \n이 포함되어 있으므로 end=""
except FileNotFoundError:
    print("⚠️ 일기 파일이 아직 존재하지 않습니다!")
```

---

### [예제 9-7] 파일 추가 모드 (`'a'`) — 가계부 지출 내역 누적
- **실생활 시나리오**: 기존 기록을 지우지 않고 새 지출 내역을 파일 맨 뒤에 계속 추가

```python
import datetime

expense_file = "expenses.txt"

item = input("지출 항목 (예: 점심 식사): ")
amount = int(input("금액 (원): "))

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
log_entry = f"[{now}] {item}: {amount:,}원\n"

# 'a' (append) 모드로 열어서 덧붙이기
with open(expense_file, "a", encoding="utf-8") as f:
    f.write(log_entry)

print("✅ 가계부에 지출 내역이 추가되었습니다!")
```

---

### [예제 9-8] CSV 파일 파싱 및 통계 내기
- **실생활 시나리오**: 콤마(`,`)로 구분된 텍스트 데이터 파일 읽어서 분석

```python
# 1. 샘플 CSV 파일 생성
csv_filename = "sales.csv"
sample_data = """품목,수량,단가
아메리카노,5,4000
카페라떼,3,4500
샌드위치,2,6500
초코머핀,4,3500
"""

with open(csv_filename, "w", encoding="utf-8") as f:
    f.write(sample_data)

# 2. CSV 파일 읽고 파싱하여 총 매출 계산
total_revenue = 0

with open(csv_filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")  # 헤더(첫 줄)
    
    print(f"📊 매출 분석표 [{header[0]} / {header[1]} / {header[2]}]")
    print("-" * 35)
    
    for line in lines[1:]:  # 데이터 행만 순회
        row = line.strip().split(",")
        item = row[0]
        qty = int(row[1])
        price = int(row[2])
        subtotal = qty * price
        total_revenue += subtotal
        print(f"{item:<8} {qty:>2}개 x {price:>5,}원 = {subtotal:>7,}원")

print("-" * 35)
print(f"총 매출액: {total_revenue:,}원")
```

---

## 🏆 도전 과제: 파일 기반 영구 메모장 프로그램

프로그램을 껐다 켜도 내용이 유지되는 콘솔 메모장 앱을 작성하세요.
1. `1. 메모 작성`: 내용 입력받아 `memo_pad.txt`에 덧붙여 저장 (`'a'`)
2. `2. 메모 목록 조회`: `memo_pad.txt`의 모든 메모 읽어서 번호와 함께 출력 (`'r'`)
3. `3. 메모 초기화`: 파일 내용 모두 비우기 (`'w'`)
4. `4. 종료`

```python
MEMO_FILE = "memo_pad.txt"

while True:
    print("\n" + "=" * 30)
    print("📝 스마트 콘솔 메모장")
    print("1. 새 메모 작성  2. 메모 목록 보기  3. 메모 전체 삭제  4. 종료")
    print("=" * 30)
    
    cmd = input("메뉴 번호: ")
    
    if cmd == "1":
        content = input("저장할 메모 내용: ")
        with open(MEMO_FILE, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        print("✅ 메모가 저장되었습니다.")
        
    elif cmd == "2":
        try:
            with open(MEMO_FILE, "r", encoding="utf-8") as f:
                memos = f.readlines()
            if not memos:
                print("📭 저장된 메모가 없습니다.")
            else:
                print(f"📋 총 {len(memos)}개의 메모:")
                for idx, memo in enumerate(memos, 1):
                    print(f"  {idx}. {memo.strip()}")
        except FileNotFoundError:
            print("📭 아직 생성된 메모 파일이 없습니다.")
            
    elif cmd == "3":
        confirm = input("⚠️ 정말 모든 메모를 지우시겠습니까? (y/n): ")
        if confirm.lower() == "y":
            with open(MEMO_FILE, "w", encoding="utf-8") as f:
                f.write("")
            print("🗑️ 모든 메모가 삭제되었습니다.")
            
    elif cmd == "4":
        print("👋 메모장을 종료합니다.")
        break
    else:
        print("⚠️ 1~4번 중 하나를 선택하세요.")
```

---

## 📝 핵심 요약 정리

1. **변수 스코프**: 지역 변수는 함수 내부에서만 유효하며, 전역 변수는 전체 프로그램에서 접근 가능.
2. **`*args`**: 개수가 정해지지 않은 위치 인수를 튜플 형태로 수신.
3. **`**kwargs`**: `key=value` 형태의 키워드 인수를 딕셔너리 형태로 수신.
4. **`lambda`**: `lambda 매개변수: 식` 형태의 간단한 일회성 익명 함수.
5. **파일 I/O & `with`문**:
   - `'r'`(읽기), `'w'`(새로 쓰기/덮어쓰기), `'a'`(이어 쓰기)
   - `with open(...) as f:` 구문으로 안전하게 자동 닫기(`close`) 보장.
   - 한글 깨짐 방지를 위해 항상 `encoding="utf-8"` 명시!
