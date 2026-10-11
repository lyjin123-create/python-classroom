# 📌 5차시: 딕셔너리와 집합

| 항목 | 내용 |
|:---:|------|
| **주제** | 딕셔너리(dict) 생성·접근·수정, 메서드, 집합(set) |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 4차시 (리스트, 튜플) |
| **목표** | 딕셔너리와 집합의 특성을 이해하고 활용할 수 있다 |

---

## 🎯 학습 목표

1. 딕셔너리를 생성하고 데이터를 추가·수정·삭제할 수 있다
2. 딕셔너리 메서드(keys, values, items)를 활용할 수 있다
3. 집합의 특성(중복 없음, 순서 없음)을 이해한다
4. 집합 연산(합·교·차집합)을 할 수 있다

---

## 📖 강의 내용 (25분)

### 1. 딕셔너리(Dictionary)란?

> 💡 **비유**: 딕셔너리는 "사전"입니다. 단어(키)를 찾으면 뜻(값)을 알 수 있어요!

```python
# {키: 값} 형태로 생성
person = {
    "이름": "김파이",
    "나이": 25,
    "직업": "개발자"
}
```

#### 리스트 vs 딕셔너리

```
# 리스트: 순서(번호)로 접근
fruits = ["사과", "바나나", "딸기"]
fruits[0]  → "사과"

# 딕셔너리: 키(이름)로 접근
prices = {"사과": 1500, "바나나": 3000, "딸기": 5000}
prices["사과"]  → 1500
```

> 💡 **핵심 차이**: 리스트는 "몇 번째?"로 찾고, 딕셔너리는 "이름이 뭐?"로 찾습니다.

---

### 2. 딕셔너리 CRUD

| 동작 | 방법 | 예시 |
|------|------|------|
| 생성 | `{키: 값}` | `{"name": "파이"}` |
| 읽기 | `dict[키]` 또는 `dict.get(키)` | `person["이름"]` |
| 추가/수정 | `dict[키] = 값` | `person["주소"] = "서울"` |
| 삭제 | `del dict[키]` 또는 `dict.pop(키)` | `del person["나이"]` |

> ⚠️ **중요**: `dict[키]`는 키가 없으면 **에러**! `dict.get(키)`는 키가 없으면 **None** 반환.

---

### 3. 딕셔너리 메서드

| 메서드 | 반환 | 예시 |
|--------|------|------|
| `keys()` | 키 목록 | `person.keys()` → `dict_keys(["이름", "나이"])` |
| `values()` | 값 목록 | `person.values()` → `dict_values(["김파이", 25])` |
| `items()` | (키, 값) 쌍 | `person.items()` → `dict_items([("이름", "김파이"), ...])` |
| `update(dict2)` | 병합 | `dict1.update(dict2)` |
| `get(키, 기본값)` | 안전한 접근 | `person.get("주소", "없음")` |

---

### 4. 집합(Set)이란?

```python
fruits = {"사과", "바나나", "딸기", "사과"}   # 중복 자동 제거!
print(fruits)   # {"사과", "바나나", "딸기"}
```

| 특성 | 설명 |
|------|------|
| 중복 없음 | 같은 값이 들어가면 자동으로 하나만 유지 |
| 순서 없음 | 인덱싱(번호 접근) 불가 |
| 변경 가능 | `add()`, `remove()` 등으로 수정 가능 |

---

### 5. 집합 연산

| 연산 | 기호 | 메서드 | 설명 |
|------|:---:|--------|------|
| 합집합 | `\|` | `union()` | 둘 중 하나라도 있으면 |
| 교집합 | `&` | `intersection()` | 둘 다 있어야 |
| 차집합 | `-` | `difference()` | A에만 있는 것 |
| 대칭차집합 | `^` | `symmetric_difference()` | 한쪽에만 있는 것 |

---

## 💻 실습 예제 (25분)

> 📂 예제 코드 파일: `examples/ex05_01.py` ~ `ex05_08.py`

---

### [예제 5-1] 딕셔너리 기초 — 연락처 관리

> 이름으로 전화번호를 찾는 연락처를 만들어 봅시다.

```python
# 연락처 딕셔너리
contacts = {
    "김철수": "010-1234-5678",
    "이영희": "010-2345-6789",
    "박민수": "010-3456-7890"
}

print("📱 연락처")
print("=" * 30)

# 전체 출력
for name, phone in contacts.items():
    print(f"  {name}: {phone}")

# 특정 연락처 찾기
print(f"\n김철수 번호: {contacts['김철수']}")

# get() — 안전한 접근 (없어도 에러 안 남)
result = contacts.get("홍길동", "등록되지 않은 연락처")
print(f"홍길동 번호: {result}")

# 연락처 추가
contacts["최지영"] = "010-4567-8901"
print(f"\n[추가] 최지영: {contacts['최지영']}")

# 연락처 수정
contacts["김철수"] = "010-1111-2222"
print(f"[수정] 김철수: {contacts['김철수']}")

# 연락처 삭제
del contacts["박민수"]
print(f"\n[삭제 후] 총 {len(contacts)}명")
for name, phone in contacts.items():
    print(f"  {name}: {phone}")
```

> 🔑 **핵심**: `dict["키"]`는 에러 위험, `dict.get("키", 기본값)`이 더 안전합니다!

---

### [예제 5-2] 딕셔너리 수정 — 카페 메뉴판

> 카페 메뉴의 가격을 관리해 봅시다.

```python
# 카페 메뉴 (음료: 가격)
menu = {
    "아메리카노": 4500,
    "카페라떼": 5000,
    "카푸치노": 5500,
    "녹차라떼": 5500,
    "핫초코": 5000,
}

print("☕ 카페 메뉴판")
print("=" * 25)
for drink, price in menu.items():
    print(f"  {drink:<8} {price:>6,}원")
print("=" * 25)

# 신메뉴 추가
menu["딸기스무디"] = 6500
menu["레몬에이드"] = 6000
print("\n🆕 신메뉴 추가 완료!")

# 가격 인상 (전체 500원 인상)
print("\n📈 가격 인상 (전체 +500원)")
for drink in menu:
    menu[drink] += 500

# 업데이트된 메뉴 출력
print("=" * 25)
for drink, price in menu.items():
    print(f"  {drink:<8} {price:>6,}원")
print("=" * 25)

# 메뉴 검색
search = input("\n검색할 음료: ")
if search in menu:
    print(f"  ✅ {search}: {menu[search]:,}원")
else:
    print(f"  ❌ '{search}'은(는) 메뉴에 없습니다.")
```

---

### [예제 5-3] 딕셔너리 메서드 — 학생 성적표

> keys(), values(), items()를 활용하여 성적 데이터를 분석합시다.

```python
# 학생 성적 (과목: 점수)
grades = {
    "국어": 85,
    "영어": 92,
    "수학": 78,
    "과학": 88,
    "사회": 95,
}

print("📊 성적표")
print("=" * 30)

# keys() — 과목 목록
print(f"과목 목록: {list(grades.keys())}")

# values() — 점수 목록
scores = list(grades.values())
print(f"점수 목록: {scores}")

# items() — (과목, 점수) 쌍으로 출력
print("\n과목별 점수:")
for subject, score in grades.items():
    stars = "⭐" * (score // 20)
    print(f"  {subject}: {score}점 {stars}")

# 통계
print(f"\n총점: {sum(scores)}점")
print(f"평균: {sum(scores) / len(scores):.1f}점")

# 최고 점수 과목 찾기
best_subject = max(grades, key=grades.get)
worst_subject = min(grades, key=grades.get)
print(f"최고: {best_subject} ({grades[best_subject]}점)")
print(f"최저: {worst_subject} ({grades[worst_subject]}점)")

# 과목 추가
grades["체육"] = 100
print(f"\n체육 추가 → 총 {len(grades)}과목")
```

---

### [예제 5-4] 중첩 딕셔너리 — 직원 정보 관리

> 딕셔너리 안에 딕셔너리! 복잡한 데이터를 구조화합시다.

```python
# 직원 정보 (딕셔너리 안에 딕셔너리)
employees = {
    "E001": {
        "이름": "김개발",
        "부서": "개발팀",
        "직급": "대리",
        "연봉": 4500,
    },
    "E002": {
        "이름": "이디자",
        "부서": "디자인팀",
        "직급": "사원",
        "연봉": 3800,
    },
    "E003": {
        "이름": "박기획",
        "부서": "기획팀",
        "직급": "과장",
        "연봉": 5500,
    },
}

# 전체 직원 목록
print("👥 직원 목록")
print("=" * 50)
print(f"{'사번':<6} {'이름':<6} {'부서':<8} {'직급':<5} {'연봉':>6}")
print("-" * 50)

for emp_id, info in employees.items():
    print(f"{emp_id:<6} {info['이름']:<6} {info['부서']:<8} {info['직급']:<5} {info['연봉']:>5,}만원")

# 특정 직원 정보 조회
print(f"\n🔍 E001 상세: {employees['E001']}")
print(f"   이름: {employees['E001']['이름']}")

# 직원 추가
employees["E004"] = {
    "이름": "최인사",
    "부서": "인사팀",
    "직급": "사원",
    "연봉": 3500,
}
print(f"\n✅ 신규 입사: {employees['E004']['이름']}")

# 연봉 인상
emp_id = "E002"
employees[emp_id]["연봉"] += 500
print(f"✅ {employees[emp_id]['이름']} 연봉 인상 → {employees[emp_id]['연봉']:,}만원")
```

---

### [예제 5-5] 딕셔너리 활용 — 투표 집계

> 딕셔너리로 데이터의 빈도수를 세봅시다.

```python
# 반장 선거 투표 결과
votes = ["김철수", "이영희", "김철수", "박민수", "이영희",
         "김철수", "김철수", "박민수", "이영희", "김철수",
         "이영희", "박민수", "김철수", "이영희", "이영희"]

# 투표 집계
result = {}
for name in votes:
    if name in result:
        result[name] += 1
    else:
        result[name] = 1

# 결과 출력
print("🗳️ 반장 선거 결과")
print("=" * 30)

# 득표순 정렬
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

for rank, (name, count) in enumerate(sorted_result, 1):
    bar = "█" * count
    ratio = count / len(votes) * 100
    print(f"  {rank}위 {name}: {count}표 ({ratio:.0f}%) {bar}")

# 당선자
winner = sorted_result[0][0]
print(f"\n🎉 당선자: {winner}!")

# === 더 쉬운 방법: dict.get() 활용 ===
print("\n--- dict.get() 활용 버전 ---")
result2 = {}
for name in votes:
    result2[name] = result2.get(name, 0) + 1    # 없으면 0, 있으면 +1
print(result2)
```

> 💡 **핵심 패턴**: `dict.get(키, 0) + 1`은 빈도수를 셀 때 가장 많이 쓰는 패턴입니다!

---

### [예제 5-6] 집합 기초 — 중복 제거

> 집합의 "중복 없음" 특성을 활용해 봅시다.

```python
# 집합 만들기
fruits = {"사과", "바나나", "딸기", "사과", "포도", "바나나"}
print(f"집합: {fruits}")           # 중복 자동 제거!
print(f"개수: {len(fruits)}개")     # 4개

# 리스트에서 중복 제거
scores = [90, 85, 90, 78, 85, 92, 78, 88]
print(f"\n원본 리스트: {scores}")
unique_scores = list(set(scores))
print(f"중복 제거: {unique_scores}")

# 집합에 추가·삭제
my_set = {"파이썬", "자바", "C언어"}
my_set.add("코틀린")          # 추가
my_set.add("파이썬")          # 이미 있으면 무시됨
print(f"\nadd 후: {my_set}")

my_set.discard("자바")        # 삭제 (없어도 에러 안 남)
my_set.discard("루비")        # 없지만 에러 없음
print(f"discard 후: {my_set}")

# remove()는 없으면 에러!
# my_set.remove("루비")   # ❌ KeyError!

# 출석부에서 중복 체크
attendance = ["김철수", "이영희", "박민수", "김철수", "최지영", "이영희"]
unique = set(attendance)
print(f"\n출석 명단: {unique}")
print(f"실제 출석: {len(unique)}명 (기록: {len(attendance)}건)")
```

---

### [예제 5-7] 집합 연산 — 취미 분석

> 집합 연산으로 "공통점"과 "차이점"을 찾아봅시다.

```python
# 두 사람의 취미
alice_hobbies = {"독서", "요리", "영화", "등산", "게임"}
bob_hobbies = {"요리", "운동", "게임", "음악", "사진"}

print(f"🧑 Alice의 취미: {alice_hobbies}")
print(f"🧑 Bob의 취미:   {bob_hobbies}")

# 합집합 — 둘 중 하나라도 하는 취미
all_hobbies = alice_hobbies | bob_hobbies
print(f"\n🔗 모든 취미 (합집합): {all_hobbies}")

# 교집합 — 둘 다 하는 취미
common = alice_hobbies & bob_hobbies
print(f"🤝 공통 취미 (교집합): {common}")

# 차집합 — Alice만 하는 취미
alice_only = alice_hobbies - bob_hobbies
bob_only = bob_hobbies - alice_hobbies
print(f"✨ Alice만: {alice_only}")
print(f"✨ Bob만:   {bob_only}")

# 대칭차집합 — 한 사람만 하는 취미
unique_hobbies = alice_hobbies ^ bob_hobbies
print(f"🔀 한쪽만 하는 취미: {unique_hobbies}")

# 부분집합 확인
print(f"\nAlice ⊃ {{'독서', '요리'}}? {{'독서', '요리'}.issubset(alice_hobbies)}")

# === 실전 활용: 수강 과목 분석 ===
print("\n" + "=" * 30)
spring = {"파이썬", "통계학", "영어회화", "경제학"}
fall = {"파이썬", "데이터분석", "영어회화", "마케팅"}

print(f"🌸 봄학기: {spring}")
print(f"🍂 가을학기: {fall}")
print(f"📌 이어서 듣는 과목: {spring & fall}")
print(f"📌 봄에만 들은 과목: {spring - fall}")
print(f"📌 가을에 새로 듣는 과목: {fall - spring}")
```

---

### [예제 5-8] 실전: 간단한 영한사전

> 딕셔너리를 활용한 사전 프로그램을 만들어 봅시다.

```python
# 영한사전 데이터
dictionary = {
    "python": "파이썬 (프로그래밍 언어)",
    "apple": "사과",
    "book": "책",
    "computer": "컴퓨터",
    "data": "자료, 데이터",
    "hello": "안녕하세요",
}

print("📖 간단한 영한사전")
print("=" * 30)
print("명령어: 검색할 단어 입력")
print("  !추가  → 새 단어 추가")
print("  !목록  → 전체 단어 보기")
print("  !종료  → 프로그램 종료")
print("=" * 30)

while True:
    word = input("\n🔍 단어 입력: ").strip().lower()

    if word == "!종료":
        print("👋 사전을 종료합니다.")
        break

    elif word == "!목록":
        print(f"\n📚 등록된 단어 ({len(dictionary)}개):")
        for eng, kor in sorted(dictionary.items()):
            print(f"  {eng:<12} → {kor}")

    elif word == "!추가":
        new_eng = input("  영어 단어: ").strip().lower()
        new_kor = input("  한국어 뜻: ").strip()
        dictionary[new_eng] = new_kor
        print(f"  ✅ '{new_eng}'이(가) 추가되었습니다!")

    elif word in dictionary:
        print(f"  ✅ {word} → {dictionary[word]}")

    else:
        print(f"  ❌ '{word}'을(를) 찾을 수 없습니다.")
        add = input("  추가하시겠습니까? (y/n): ").strip().lower()
        if add == "y":
            meaning = input("  한국어 뜻: ").strip()
            dictionary[word] = meaning
            print(f"  ✅ '{word}'이(가) 추가되었습니다!")
```

---

## 🏆 도전 과제

### [도전 1] 편의점 재고 관리 프로그램

```python
# 편의점 재고를 딕셔너리로 관리하세요!
# 기능: 재고 조회, 입고(추가), 판매(차감), 품절 확인

inventory = {
    "삼각김밥": 15,
    "컵라면": 8,
    "우유": 12,
    "과자": 20,
    "음료수": 25,
}

print("🏪 편의점 재고 관리")
print("1. 재고 조회  2. 입고  3. 판매  4. 품절 목록  5. 종료")

while True:
    choice = input("\n메뉴 선택: ")

    if choice == "1":
        print("\n📦 현재 재고:")
        for item, qty in inventory.items():
            status = "⚠️ 부족" if qty < 5 else ""
            print(f"  {item}: {qty}개 {status}")

    elif choice == "2":
        item = input("  입고 상품명: ")
        qty = int(input("  입고 수량: "))
        inventory[item] = inventory.get(item, 0) + qty
        print(f"  ✅ {item} {qty}개 입고 완료 (현재: {inventory[item]}개)")

    elif choice == "3":
        item = input("  판매 상품명: ")
        if item not in inventory or inventory[item] == 0:
            print("  ❌ 재고가 없습니다!")
        else:
            qty = int(input("  판매 수량: "))
            if qty > inventory[item]:
                print(f"  ❌ 재고 부족! (현재: {inventory[item]}개)")
            else:
                inventory[item] -= qty
                print(f"  ✅ {item} {qty}개 판매 (남은: {inventory[item]}개)")

    elif choice == "4":
        empty = [item for item, qty in inventory.items() if qty == 0]
        if empty:
            print(f"  🚨 품절 상품: {', '.join(empty)}")
        else:
            print("  ✅ 품절 상품 없음!")

    elif choice == "5":
        print("👋 종료합니다.")
        break
```

---

## 📝 5차시 요약

| 배운 것 | 설명 | 예시 |
|---------|------|------|
| 딕셔너리 생성 | `{키: 값}` 형태 | `{"name": "파이"}` |
| 값 접근 | `dict[키]`, `dict.get(키)` | `d["name"]` |
| 값 추가/수정 | `dict[키] = 값` | `d["age"] = 25` |
| `keys()` | 키 목록 | `d.keys()` |
| `values()` | 값 목록 | `d.values()` |
| `items()` | (키, 값) 쌍 | `d.items()` |
| 집합 생성 | `{값1, 값2}` 또는 `set()` | `{1, 2, 3}` |
| 합집합 | `\|` | `a \| b` |
| 교집합 | `&` | `a & b` |
| 차집합 | `-` | `a - b` |
| 중복 제거 | `set(리스트)` | `set([1,1,2])` → `{1,2}` |

### 다음 시간 예고
> 6차시에서는 **불 자료형과 조건문**을 배웁니다. "만약 ~이면 ~하고, 아니면 ~한다"처럼 조건에 따라 다르게 동작하는 프로그램을 만들어요! 🪧
