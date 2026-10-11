# 📌 11차시: 모듈 & 예외 처리 (Modules & Exceptions)

| 항목 | 내용 |
|:---:|------|
| **주제** | 모듈 import, 표준 라이브러리, pip, try-except-else-finally, 예외 처리 |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 10차시 (클래스) |
| **목표** | 유용한 내장/외부 모듈을 가져와 활용하고, 에러가 나도 프로그램이 멈추지 않게 방어할 수 있다 |

---

## 🎯 학습 목표

1. 모듈(Module)의 개념과 `import` 방식(3가지)을 이해한다.
2. 파이썬 대표 내장 라이브러리(`random`, `datetime`, `json`, `os`)를 실생활 예제에 적용할 수 있다.
3. `pip`를 사용해 외부 라이브러리를 설치하고 관리하는 원리를 파악한다.
4. `try-except-else-finally` 구조로 예외 상황을 안전하게 처리할 수 있다.

---

## 📖 강의 내용 (25분)

### 1. 모듈(Module)이란?

> 💡 **비유**: 모듈은 **"전문가 공구함"** 🧰 입니다.  
> 모든 도구를 내가 처음부터 다 깎아서 만들 필요 없이, 이미 잘 만들어진 도구함을 가져와(`import`) 바로 쓰면 됩니다.

#### 모듈 불러오는 3가지 문법
```python
# 1) 기본 import: 모듈명.함수명()
import math
print(math.sqrt(16))  # 4.0 (제곱근)

# 2) 특정 함수만 가져오기: 함수명()
from random import randint
print(randint(1, 10))

# 3) 긴 모듈명에 별칭(alias) 붙이기
import datetime as dt
now = dt.datetime.now()
```

---

### 2. 알아두면 필수인 파이썬 내장 라이브러리

파이썬에는 별도 설치 없이 바로 쓸 수 있는 강력한 "배터리 포함(Batteries Included)" 모듈들이 있습니다.

| 모듈명 | 주요 기능 | 대표 함수/속성 |
|:---:|------|------|
| `random` | 난수 생성, 무작위 뽑기 | `randint()`, `choice()`, `sample()` |
| `datetime` | 날짜, 시간 연산, D-Day | `now()`, `strftime()`, `timedelta` |
| `json` | 데이터 직렬화 (웹 표준 포맷) | `dumps()`, `loads()` |
| `os` | 파일 경로, 폴더 탐색 | `listdir()`, `path.exists()`, `remove()` |

---

### 3. 외부 패키지 매니저: pip

파이썬 공식 패키지 저장소(PyPI)에서 전 세계 개발자들이 만든 수십만 개의 오픈소스를 한 줄로 설치합니다.

```bash
# 터미널(CMD/PowerShell)에서 실행
pip install requests      # HTTP 통신 라이브러리
pip install flask         # 웹 개발 프레임워크
pip list                  # 설치된 목록 확인
```

---

### 4. 예외(Exception) 처리란?

> 💡 **비유**: 자동차의 **"에어백과 안전벨트"** 🪢  
> 주행 중 예상치 못한 돌발 상황(사고)이 발생했을 때, 엔진이 박살나고 프로그램이 비정상 종료되는 것을 막고 안전하게 수습하는 장치입니다.

#### 기본 문법
```python
"""
try:
    에러가 발생할 가능성이 있는 코드
except 에러종류:
    에러가 발생했을 때 수습할 코드
else:
    에러가 발생하지 않았을 때만 실행할 코드 (선택)
finally:
    에러 발생 여부와 상관없이 무조건 마지막에 실행되는 코드 (선택)
"""
```

#### 초보자가 자주 만나는 대표적인 에러들
- `ValueError`: 숫자로 바꿀 수 없는 문자열을 `int("abc")` 했을 때
- `ZeroDivisionError`: 숫자를 0으로 나누려 할 때 (`10 / 0`)
- `IndexError`: 리스트 범위를 벗어난 인덱스를 요청할 때
- `KeyError`: 딕셔너리에 없는 키를 조회할 때
- `FileNotFoundError`: 존재하지 않는 파일을 읽으려 할 때

---

## 💻 실습 예제 (25분)

### [예제 11-1] random 모듈 — 로또 6/45 번호 추첨기
- **실생활 시나리오**: 1~45 중 중복 없이 6개 번호 무작위 자동 추출

```python
import random

def generate_lotto():
    # random.sample: 중복 없이 지정한 개수만큼 추출
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()  # 오름차순 정렬
    return numbers

print("🎰 이번 주 로또 추천 번호 5게임:")
print("=" * 35)
for i in range(1, 6):
    game = generate_lotto()
    print(f"제 {i}게임: {game}")
```

---

### [예제 11-2] datetime 모듈 — D-Day 및 만 나이 계산기
- **실생활 시나리오**: 목표 시험일까지 남은 일수(D-Day) 계산

```python
import datetime

# 1. 현재 날짜와 시각
now = datetime.datetime.now()
print("현재 날짜와 시간:", now.strftime("%Y년 %m월 %d일 %H시 %M분"))

# 2. D-Day 계산
target_date = datetime.datetime(2026, 12, 31)
today = datetime.datetime.now()

diff = target_date - today
print(f"📅 2026년 마지막 날까지 D-{diff.days}일 남았습니다!")
```

---

### [예제 11-3] json 모듈 — 파이썬 데이터 ↔ JSON 문자열 변환
- **실생활 시나리오**: 웹 서버 통신 및 설정 파일 저장

```python
import json

user_data = {
    "name": "김철수",
    "age": 29,
    "skills": ["Python", "Flask", "SQL"],
    "is_employed": True
}

# 1. 딕셔너리 → JSON 문자열 (dumps)
json_str = json.dumps(user_data, ensure_ascii=False, indent=2)
print("📝 변환된 JSON 문자열:")
print(json_str)

# 2. JSON 문자열 → 딕셔너리 (loads)
parsed = json.loads(json_str)
print(f"다시 파이썬 객체로 복원: 이름은 {parsed['name']}, 보유 스킬 {len(parsed['skills'])}개")
```

---

### [예제 11-4] try-except 기본 — 안전한 정수 입력받기
- **실생활 시나리오**: 숫자를 넣어야 하는데 문자를 넣었을 때 튕기지 않게 방어

```python
while True:
    try:
        user_input = input("나이를 입력하세요: ")
        age = int(user_input)
        print(f"입력하신 나이는 {age}세입니다.")
        break  # 성공 시 루프 탈출
    except ValueError:
        print("⚠️ 잘못된 입력입니다! 숫자만 입력해주세요.")
```

---

### [예제 11-5] 다중 except 문 — 나누기 계산기
- **실생활 시나리오**: 입력 실수와 0으로 나누기 에러를 구분하여 친절히 안내

```python
try:
    a = int(input("첫 번째 숫자(분자): "))
    b = int(input("두 번째 숫자(분모): "))
    result = a / b
except ValueError:
    print("❌ 문자가 아닌 정수를 입력해야 합니다.")
except ZeroDivisionError:
    print("❌ 0으로는 나눌 수 없습니다! 분모에 0이 아닌 숫자를 넣으세요.")
except Exception as e:
    print(f"❌ 알 수 없는 에러가 발생했습니다: {e}")
else:
    print(f"✅ 연산 결과: {a} ÷ {b} = {result:.2f}")
finally:
    print("🏁 계산기 동작을 종료합니다.")
```

---

### [예제 11-6] 파일 열기 예외 처리와 안전한 리소스 관리
- **실생활 시나리오**: 찾는 파일이 없을 때 프로그램 다운 방지

```python
file_name = "secret_report.txt"

try:
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.read()
    print("파일 내용:", data)
except FileNotFoundError:
    print(f"⚠️ '{file_name}' 파일을 찾을 수 없습니다.")
    print("   새 기본 템플릿 파일을 생성합니다...")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("기본 보고서 서식입니다.\n")
```

---

### [예제 11-7] `raise` — 규칙 위반 시 의도적 예외 발생
- **실생활 시나리오**: 나이가 음수이거나 150세를 넘을 때 예외를 터뜨려 차단

```python
def check_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"나이는 0~150 사이여야 합니다 (입력값: {age})")
    print(f"인증 완료: {age}세")

try:
    check_age(25)
    check_age(-5)  # 에러 발생!
except ValueError as e:
    print("❌ 입력 검증 실패:", e)
```

---

## 🏆 도전 과제: 안전한 회원가입 유효성 검사기

회원가입 폼에서 아이디와 비밀번호를 검증하는 프로그램을 작성하세요.
- 아이디 규칙: 최소 4자 이상
- 비밀번호 규칙: 최소 8자 이상이며 숫자가 1개 이상 포함되어야 함
- 규칙에 어긋나면 `raise ValueError("구체적 이유")`를 발생시키고 `try-except`로 에러 메시지를 사용자에게 출력한 후 다시 입력받으세요.

```python
def validate_signup(user_id, password):
    if len(user_id) < 4:
        raise ValueError("아이디는 최소 4글자 이상이어야 합니다.")
        
    if len(password) < 8:
        raise ValueError("비밀번호는 최소 8글자 이상이어야 합니다.")
        
    # 숫자가 1개 이상 들어있는지 확인
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        raise ValueError("비밀번호에는 숫자가 최소 1개 이상 포함되어야 합니다.")
        
    return True

# 메인 실행 루프
while True:
    try:
        uid = input("\n아이디 입력: ")
        pw = input("비밀번호 입력: ")
        validate_signup(uid, pw)
        print("🎉 회원가입 조건 통과! 가입을 축하합니다.")
        break
    except ValueError as e:
        print(f"❌ 가입 실패: {e} 다시 시도하세요.")
```

---

## 📝 핵심 요약 정리

1. **`import` 방식**: 전체 모듈 가져오기(`import random`), 특정 기능만 가져오기(`from math import sqrt`), 별칭(`as`).
2. **필수 내장 모듈**: `random`(난수), `datetime`(날짜/시간), `json`(데이터 직렬화), `os`(운영체제 경로/파일).
3. **`pip install`**: 외부 패키지를 손쉽게 설치하는 파이썬 패키지 매니저.
4. **예외 처리 구조**:
   - `try`: 에러 가능성 있는 코드
   - `except [에러타입]`: 에러 수습
   - `else`: 에러 없을 때만 실행
   - `finally`: 언제나 반드시 실행
5. **`raise Exception("이유")`**: 개발자가 직접 명시적으로 에러를 발생시킬 때 사용.
