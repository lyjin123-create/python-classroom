# 📌 4차시: 리스트와 튜플

| 항목 | 내용 |
|:---:|------|
| **주제** | 리스트 생성·인덱싱·슬라이싱, 리스트 메서드, 튜플 |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 3차시 (인덱싱, 슬라이싱 개념) |
| **목표** | 리스트와 튜플로 여러 데이터를 관리할 수 있다 |

---

## 🎯 학습 목표

1. 리스트를 생성하고 인덱싱·슬라이싱을 할 수 있다
2. 리스트에 데이터를 추가·삭제·수정할 수 있다
3. 리스트 메서드를 활용할 수 있다
4. 튜플의 특성과 사용 시점을 이해한다

---

## 📖 강의 내용 (25분)

### 1. 리스트(List)란?

> 💡 **비유**: 리스트는 "여러 칸이 있는 서랍장"입니다. 각 칸에 물건을 넣고, 번호로 꺼낼 수 있어요.

```python
# 리스트 만들기 — 대괄호 []로 감싸고, 쉼표로 구분
fruits = ["사과", "바나나", "딸기", "포도"]
numbers = [10, 20, 30, 40, 50]
mixed = ["김파이", 25, True, 3.14]   # 다양한 타입 가능!
empty = []                            # 빈 리스트
```

#### 리스트 vs 변수

```
# 변수: 하나의 값만 저장
score1 = 90
score2 = 85
score3 = 78
# ... 학생이 100명이면? 변수 100개?!

# 리스트: 여러 값을 하나로 관리!
scores = [90, 85, 78, 92, 88, ...]
```

---

### 2. 리스트 인덱싱·슬라이싱

문자열에서 배운 것과 **완전히 동일**합니다!

```python
colors = ["빨강", "주황", "노랑", "초록", "파랑"]
#            0       1       2       3       4
#           -5      -4      -3      -2      -1

colors[0]      # "빨강" (첫 번째)
colors[-1]     # "파랑" (마지막)
colors[1:3]    # ["주황", "노랑"] (슬라이싱)
colors[::-1]   # ["파랑", "초록", "노랑", "주황", "빨강"] (역순)
```

---

### 3. 리스트 수정

리스트는 문자열과 달리 **값을 변경할 수 있습니다**! (Mutable)

| 동작 | 방법 | 예시 |
|------|------|------|
| 값 변경 | `list[인덱스] = 새값` | `fruits[0] = "망고"` |
| 끝에 추가 | `list.append(값)` | `fruits.append("키위")` |
| 특정 위치에 삽입 | `list.insert(위치, 값)` | `fruits.insert(1, "체리")` |
| 값으로 삭제 | `list.remove(값)` | `fruits.remove("바나나")` |
| 인덱스로 삭제 | `del list[인덱스]` | `del fruits[0]` |
| 꺼내기(삭제+반환) | `list.pop(인덱스)` | `fruits.pop()` (마지막) |
| 전체 삭제 | `list.clear()` | `fruits.clear()` |

---

### 4. 리스트 메서드

| 메서드 | 기능 | 예시 |
|--------|------|------|
| `sort()` | 정렬 (원본 변경) | `nums.sort()` |
| `sort(reverse=True)` | 내림차순 정렬 | `nums.sort(reverse=True)` |
| `sorted(list)` | 정렬 (새 리스트 반환) | `new = sorted(nums)` |
| `reverse()` | 역순 (원본 변경) | `nums.reverse()` |
| `count(값)` | 값의 개수 | `nums.count(3)` |
| `index(값)` | 값의 위치 | `nums.index(3)` |
| `len(list)` | 길이 | `len(nums)` |
| `sum(list)` | 합계 (숫자) | `sum(nums)` |
| `min(list)` | 최솟값 | `min(nums)` |
| `max(list)` | 최댓값 | `max(nums)` |
| `list.extend(list2)` | 리스트 합치기 | `a.extend(b)` |

---

### 5. 튜플(Tuple)

```python
# 소괄호 ()로 생성
colors = ("빨강", "초록", "파랑")
point = (3, 4)
```

| | 리스트 | 튜플 |
|---|---|---|
| 기호 | `[]` | `()` |
| 변경 | ✅ 가능 (Mutable) | ❌ 불가 (Immutable) |
| 용도 | 바뀌는 데이터 | 바뀌면 안 되는 데이터 |
| 예시 | 장보기 목록, 일정 | 좌표, 요일, RGB 색상 |

> 💡 **비유**: 리스트 = 연필로 쓴 메모(수정 가능), 튜플 = 볼펜으로 쓴 메모(수정 불가)

---

## 💻 실습 예제 (25분)

> 📂 예제 코드 파일: `examples/ex04_01.py` ~ `ex04_08.py`

---

### [예제 4-1] 리스트 생성과 접근 — 장보기 목록

> 여러 데이터를 하나의 변수에 담아봅시다!

```python
# 장보기 목록 만들기
grocery = ["우유", "계란", "빵", "치즈", "버터"]

# 전체 출력
print("🛒 장보기 목록:", grocery)
print(f"총 {len(grocery)}개 항목")

# 인덱싱으로 접근
print(f"\n첫 번째: {grocery[0]}")    # 우유
print(f"마지막: {grocery[-1]}")      # 버터
print(f"세 번째: {grocery[2]}")      # 빵

# 슬라이싱
print(f"\n처음 3개: {grocery[:3]}")   # ['우유', '계란', '빵']
print(f"뒤에서 2개: {grocery[-2:]}")  # ['치즈', '버터']

# 리스트 길이
print(f"\n목록 길이: {len(grocery)}")

# 포함 여부 확인 (in 연산자)
print(f"\n'우유'가 목록에 있나요? {'우유' in grocery}")    # True
print(f"'사과'가 목록에 있나요? {'사과' in grocery}")      # False
```

**실행 결과:**
```
🛒 장보기 목록: ['우유', '계란', '빵', '치즈', '버터']
총 5개 항목

첫 번째: 우유
마지막: 버터
세 번째: 빵

처음 3개: ['우유', '계란', '빵']
뒤에서 2개: ['치즈', '버터']

목록 길이: 5

'우유'가 목록에 있나요? True
'사과'가 목록에 있나요? False
```

> 🔑 **핵심**: 리스트는 `[]`로 만들고, 인덱싱·슬라이싱은 문자열과 동일합니다!

---

### [예제 4-2] 리스트 수정 — 할 일 목록 관리

> 리스트에 항목을 추가하고, 삭제하고, 변경해 봅시다.

```python
# 할 일 목록
todo = ["이메일 확인", "보고서 작성", "회의 참석"]
print("📋 초기 목록:", todo)

# 1. 추가 — append (맨 뒤에)
todo.append("점심 약속")
print("\n[append] 점심 약속 추가:", todo)

# 2. 삽입 — insert (원하는 위치에)
todo.insert(1, "커피 마시기")     # 1번 위치에 삽입
print("[insert] 커피 마시기 삽입:", todo)

# 3. 값 변경
todo[2] = "보고서 수정"           # "보고서 작성" → "보고서 수정"
print("[변경] 보고서 수정으로 변경:", todo)

# 4. 삭제 — remove (값으로)
todo.remove("회의 참석")
print("[remove] 회의 참석 삭제:", todo)

# 5. 삭제 — pop (인덱스로, 꺼내기)
removed = todo.pop()              # 마지막 항목 꺼내기
print(f"[pop] '{removed}' 꺼냄:", todo)

# 6. 삭제 — del (인덱스로)
del todo[0]
print("[del] 첫 번째 삭제:", todo)

# 7. 리스트 합치기
extra = ["운동하기", "독서하기"]
todo.extend(extra)
print("\n[extend] 추가 목록 합침:", todo)

# 또는 + 연산자
todo = todo + ["일찍 자기"]
print("[+] 일찍 자기 추가:", todo)

print(f"\n최종 할 일: {len(todo)}개")
```

> 🔑 **핵심**: `append`=맨 뒤 추가, `insert`=원하는 위치 삽입, `remove`=값으로 삭제, `pop`=꺼내기

---

### [예제 4-3] 리스트 정렬 — 시험 점수 관리

> 리스트의 정렬(sort)과 통계 함수를 배워봅시다.

```python
# 국어 시험 점수
scores = [78, 92, 65, 88, 95, 72, 85, 90]
print(f"원본 점수: {scores}")

# 오름차순 정렬 (원본 변경!)
scores.sort()
print(f"오름차순: {scores}")

# 내림차순 정렬
scores.sort(reverse=True)
print(f"내림차순: {scores}")

# 통계
print(f"\n📊 성적 통계")
print(f"  학생 수: {len(scores)}명")
print(f"  총점: {sum(scores)}점")
print(f"  평균: {sum(scores) / len(scores):.1f}점")
print(f"  최고점: {max(scores)}점")
print(f"  최저점: {min(scores)}점")

# sorted() — 원본은 유지하고 새 리스트 반환
original = [30, 10, 50, 20, 40]
new_sorted = sorted(original)
print(f"\n원본 유지:   {original}")
print(f"정렬된 복사: {new_sorted}")

# reverse() — 현재 순서를 뒤집기 (정렬 아님!)
items = ["A", "C", "B", "E", "D"]
items.reverse()
print(f"\n역순: {items}")    # ['D', 'E', 'B', 'C', 'A']
```

> ⚠️ **주의**: `sort()`는 원본을 변경하고, `sorted()`는 원본을 유지합니다!

---

### [예제 4-4] 리스트 슬라이싱 활용 — 주간 데이터

> 리스트 슬라이싱으로 특정 구간의 데이터를 추출해 봅시다.

```python
# 월~일 카페 매출 (단위: 만원)
daily_sales = [45, 52, 38, 47, 63, 78, 72]
days = ["월", "화", "수", "목", "금", "토", "일"]

print("☕ 주간 카페 매출")
print("=" * 35)

# 전체 출력
for i in range(len(days)):
    bar = "█" * (daily_sales[i] // 5)
    print(f"  {days[i]}요일: {daily_sales[i]}만원 {bar}")

# 평일(월~금) vs 주말(토~일)
weekday_sales = daily_sales[:5]     # 인덱스 0~4
weekend_sales = daily_sales[5:]     # 인덱스 5~6

print(f"\n📊 분석")
print(f"  평일 매출: {weekday_sales} → 평균 {sum(weekday_sales)/len(weekday_sales):.1f}만원")
print(f"  주말 매출: {weekend_sales} → 평균 {sum(weekend_sales)/len(weekend_sales):.1f}만원")
print(f"  주간 총매출: {sum(daily_sales)}만원")

# 가장 잘 팔린 날
best_day_index = daily_sales.index(max(daily_sales))
print(f"  최고 매출: {days[best_day_index]}요일 ({max(daily_sales)}만원)")
```

---

### [예제 4-5] 중첩 리스트 — 영화관 좌석

> 리스트 안에 리스트! 2차원 데이터를 다뤄봅시다.

```python
# 영화관 좌석 배치 (O: 빈 좌석, X: 예약됨)
seats = [
    ["O", "O", "X", "X", "O"],   # A열
    ["X", "X", "O", "O", "X"],   # B열
    ["O", "O", "O", "X", "X"],   # C열
    ["X", "O", "O", "O", "O"],   # D열
]

# 좌석 현황 출력
print("🎬 영화관 좌석 현황")
print("   1  2  3  4  5")
print("-" * 18)
rows = ["A", "B", "C", "D"]
for i in range(len(seats)):
    row_str = "  ".join(seats[i])
    print(f"{rows[i]}  {row_str}")

# 특정 좌석 확인
print(f"\nB열 3번 좌석: {seats[1][2]}")    # 행=1, 열=2
print(f"D열 1번 좌석: {seats[3][0]}")      # 행=3, 열=0

# 빈 좌석 수 세기
empty_count = 0
total_count = 0
for row in seats:
    for seat in row:
        total_count += 1
        if seat == "O":
            empty_count += 1

print(f"\n전체 좌석: {total_count}석")
print(f"빈 좌석: {empty_count}석")
print(f"예약된 좌석: {total_count - empty_count}석")
print(f"예약률: {(total_count - empty_count) / total_count * 100:.0f}%")
```

> 🔑 **핵심**: `seats[행][열]`으로 2차원 데이터에 접근합니다. 행이 먼저, 열이 나중!

---

### [예제 4-6] 튜플 기초 — 변경 불가능한 데이터

> 변경하면 안 되는 데이터는 튜플로 저장합시다.

```python
# 튜플 만들기 — 소괄호 () 사용
point = (3, 4)
rgb_red = (255, 0, 0)
weekdays = ("월", "화", "수", "목", "금", "토", "일")

print(f"좌표: {point}")
print(f"빨강 RGB: {rgb_red}")
print(f"요일: {weekdays}")

# 인덱싱·슬라이싱은 리스트와 동일
print(f"\nx 좌표: {point[0]}")
print(f"y 좌표: {point[1]}")
print(f"주중: {weekdays[:5]}")
print(f"주말: {weekdays[5:]}")

# ❌ 튜플은 변경 불가!
# point[0] = 10    # TypeError: 'tuple' object does not support item assignment

# 튜플 언패킹 (아주 유용!)
x, y = point
print(f"\n언패킹: x={x}, y={y}")

r, g, b = rgb_red
print(f"언패킹: R={r}, G={g}, B={b}")

# 하나짜리 튜플은 쉼표 필요!
single = (42,)     # ✅ 튜플
not_tuple = (42)    # ❌ 그냥 숫자 42
print(f"\ntype((42,)) = {type(single)}")     # tuple
print(f"type((42))  = {type(not_tuple)}")    # int

# 튜플 ↔ 리스트 변환
colors_tuple = ("빨강", "초록", "파랑")
colors_list = list(colors_tuple)     # 튜플 → 리스트
back_to_tuple = tuple(colors_list)   # 리스트 → 튜플
print(f"\n리스트로: {colors_list}")
print(f"다시 튜플: {back_to_tuple}")
```

> 💡 **언제 튜플을 쓰나요?**
> - 좌표 (x, y), 색상 (R, G, B) 등 "고정된 묶음"
> - 딕셔너리의 키로 사용 (리스트는 불가!)
> - 실수로 변경하면 안 되는 상수 데이터

---

### [예제 4-7] 리스트 vs 튜플 비교

> 둘의 차이를 직접 비교해 봅시다.

```python
# === 리스트: 변할 수 있는 데이터 ===
schedule = ["회의", "점심", "코딩"]   # 일정은 바뀔 수 있다
print(f"📋 일정: {schedule}")

schedule.append("퇴근")
schedule[0] = "미팅"     # 변경 가능!
print(f"수정된 일정: {schedule}")

# === 튜플: 변하면 안 되는 데이터 ===
WEEKDAYS = ("월", "화", "수", "목", "금", "토", "일")   # 요일은 바뀌지 않는다
print(f"\n📅 요일: {WEEKDAYS}")
# WEEKDAYS[0] = "먼"    # ❌ TypeError!

# === 성능 비교 (참고) ===
import sys
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"\n📦 메모리 사용량")
print(f"  리스트: {sys.getsizeof(list_data)} bytes")
print(f"  튜플:   {sys.getsizeof(tuple_data)} bytes")
# 튜플이 약간 더 적은 메모리를 사용합니다!

# === 공통 기능 ===
print(f"\n공통 기능:")
print(f"  길이: list={len(list_data)}, tuple={len(tuple_data)}")
print(f"  포함: 3 in list={3 in list_data}, 3 in tuple={3 in tuple_data}")
print(f"  인덱스: list[0]={list_data[0]}, tuple[0]={tuple_data[0]}")
print(f"  슬라이싱: list[1:3]={list_data[1:3]}, tuple[1:3]={tuple_data[1:3]}")
```

---

### [예제 4-8] 실전: 성적 관리 프로그램

> 배운 것을 총동원하여 점수를 입력받고 분석해 봅시다.

```python
# 성적 관리 프로그램
print("📊 성적 관리 프로그램")
print("=" * 30)

# 과목 이름 (튜플 — 바뀌지 않으므로)
subjects = ("국어", "영어", "수학", "과학", "사회")

# 점수 입력받기 (리스트 — 바뀔 수 있으므로)
scores = []
for subject in subjects:
    score = int(input(f"  {subject} 점수: "))
    scores.append(score)

# 결과 출력
print("\n" + "=" * 30)
print("📋 성적표")
print("=" * 30)

for i in range(len(subjects)):
    bar = "█" * (scores[i] // 10)
    print(f"  {subjects[i]}: {scores[i]:>3}점 {bar}")

print("-" * 30)

# 통계
total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)
best_subject = subjects[scores.index(highest)]
worst_subject = subjects[scores.index(lowest)]

print(f"  총점: {total}점")
print(f"  평균: {average:.1f}점")
print(f"  최고 과목: {best_subject} ({highest}점)")
print(f"  최저 과목: {worst_subject} ({lowest}점)")

# 등급 판정
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"  종합 등급: {grade}")
print("=" * 30)
```

---

## 🏆 도전 과제

### [도전 1] 로또 번호 분석기

```python
# 주어진 로또 당첨 번호 목록에서 통계를 추출하세요!

# 최근 5회 당첨 번호 (가상 데이터)
lotto_results = [
    [3, 12, 18, 27, 34, 42],
    [5, 12, 21, 33, 38, 45],
    [7, 12, 15, 23, 34, 41],
    [1, 9, 18, 25, 34, 40],
    [6, 14, 18, 29, 35, 43],
]

# 모든 번호를 하나의 리스트로 합치기
all_numbers = []
for result in lotto_results:
    all_numbers.extend(result)

print("🎱 로또 당첨 번호 분석")
print("=" * 30)

# 가장 많이 나온 번호 찾기
print("\n각 번호 등장 횟수:")
checked = []
for num in sorted(set(all_numbers)):
    count = all_numbers.count(num)
    if count >= 2:
        print(f"  {num:>2}번: {'⭐' * count} ({count}회)")

# 총 번호 개수
print(f"\n총 {len(all_numbers)}개 번호 중 {len(set(all_numbers))}개 고유 번호")
```

---

## 📝 4차시 요약

| 배운 것 | 설명 | 예시 |
|---------|------|------|
| 리스트 생성 | `[]`로 여러 값 저장 | `[1, 2, 3]` |
| 인덱싱 | 위치로 접근 | `list[0]`, `list[-1]` |
| 슬라이싱 | 부분 추출 | `list[1:3]` |
| `append()` | 맨 뒤에 추가 | `list.append(값)` |
| `insert()` | 특정 위치 삽입 | `list.insert(1, 값)` |
| `remove()` | 값으로 삭제 | `list.remove(값)` |
| `pop()` | 꺼내기 (삭제+반환) | `list.pop()` |
| `sort()` | 정렬 | `list.sort()` |
| `len/sum/min/max` | 통계 함수 | `len(list)` |
| 튜플 | 변경 불가 리스트 | `(1, 2, 3)` |
| `in` 연산자 | 포함 여부 | `"a" in list` |

### 다음 시간 예고
> 5차시에서는 **딕셔너리와 집합**을 배웁니다. "이름으로 전화번호 찾기"처럼 키-값 쌍으로 데이터를 관리하는 방법을 배워요! 📞
