# 📌 3차시: 문자열 다루기 심화

| 항목 | 내용 |
|:---:|------|
| **주제** | 인덱싱, 슬라이싱, 포매팅, 문자열 메서드 |
| **시간** | 50분 (강의 20분 + 실습 30분) |
| **선수 지식** | 2차시 (변수, 자료형, 문자열 기초) |
| **목표** | 문자열을 자유자재로 다룰 수 있다 |

---

## 🎯 학습 목표

1. 문자열 인덱싱으로 특정 글자를 꺼낼 수 있다
2. 문자열 슬라이싱으로 일부분을 잘라낼 수 있다
3. 문자열 포매팅의 여러 방법(%, format, f-string)을 사용할 수 있다
4. 주요 문자열 메서드를 활용할 수 있다

---

## 📖 강의 내용 (20분)

### 1. 인덱싱(Indexing) — 글자 하나 꺼내기

> 💡 **비유**: 아파트 호수처럼, 문자열의 각 글자에는 "번호(인덱스)"가 있어요.

```
문자:  P   y   t   h   o   n
양수:  0   1   2   3   4   5
음수: -6  -5  -4  -3  -2  -1
```

- **양수 인덱스**: 왼쪽부터 0, 1, 2, ... (0부터 시작!)
- **음수 인덱스**: 오른쪽부터 -1, -2, -3, ...

```python
text = "Python"
text[0]   # 'P' (첫 글자)
text[-1]  # 'n' (마지막 글자)
```

---

### 2. 슬라이싱(Slicing) — 부분 문자열 잘라내기

```python
text[시작:끝]        # 시작~(끝-1)까지
text[시작:끝:간격]   # 간격만큼 건너뛰며
```

> ⚠️ **핵심**: 끝 인덱스는 **포함하지 않습니다**! `text[0:3]`은 0, 1, 2번째 글자만!

---

### 3. 문자열 포매팅

| 방법 | 문법 | 추천 |
|------|------|:---:|
| % 연산자 | `"이름: %s" % name` | △ (구형) |
| format() | `"이름: {}".format(name)` | ○ |
| **f-string** | `f"이름: {name}"` | **★ 강력 추천** |

---

### 4. 주요 문자열 메서드

| 메서드 | 기능 | 예시 |
|--------|------|------|
| `upper()` | 대문자로 | `"hello".upper()` → `"HELLO"` |
| `lower()` | 소문자로 | `"HELLO".lower()` → `"hello"` |
| `strip()` | 양쪽 공백 제거 | `" hi ".strip()` → `"hi"` |
| `replace(a, b)` | a를 b로 치환 | `"hello".replace("l", "r")` → `"herro"` |
| `split(sep)` | 구분자로 분리 → 리스트 | `"a,b,c".split(",")` → `['a','b','c']` |
| `join(list)` | 리스트를 하나로 결합 | `"-".join(['a','b'])` → `"a-b"` |
| `find(s)` | 위치 찾기 (-1: 없음) | `"hello".find("ll")` → `2` |
| `count(s)` | 등장 횟수 | `"hello".count("l")` → `2` |
| `startswith(s)` | ~로 시작? | `"hello".startswith("he")` → `True` |
| `endswith(s)` | ~로 끝? | `"file.py".endswith(".py")` → `True` |

> 💡 **중요**: 문자열은 **변경 불가(immutable)**입니다. 메서드는 원본을 바꾸지 않고 **새 문자열**을 반환해요!

---

## 💻 실습 예제 (30분)

> 📂 예제 코드 파일: `examples/ex03_01.py` ~ `ex03_10.py`

---

### [예제 3-1] 인덱싱 기초

```python
text = "Python"

# 양수 인덱싱
# P  y  t  h  o  n
# 0  1  2  3  4  5

print(f"text[0] = '{text[0]}'")    # P (첫 글자)
print(f"text[1] = '{text[1]}'")    # y
print(f"text[2] = '{text[2]}'")    # t
print(f"text[5] = '{text[5]}'")    # n (마지막 글자)

print()

# 음수 인덱싱
# P   y   t   h   o   n
# -6  -5  -4  -3  -2  -1

print(f"text[-1] = '{text[-1]}'")   # n (마지막 글자)
print(f"text[-2] = '{text[-2]}'")   # o
print(f"text[-6] = '{text[-6]}'")   # P (첫 글자)

# 한글도 동일!
korean = "파이썬"
print(f"\nkorean[0] = '{korean[0]}'")    # 파
print(f"korean[-1] = '{korean[-1]}'")    # 썬
```

> 🔑 **기억!** 인덱스는 **0부터** 시작합니다. 1이 아니에요!

---

### [예제 3-2] 슬라이싱 기초

```python
text = "Hello, Python!"
#       0123456789...

# [시작:끝] — 시작 포함, 끝 미포함
print(f"text[0:5] = '{text[0:5]}'")     # Hello
print(f"text[7:13] = '{text[7:13]}'")   # Python

# 시작 또는 끝 생략
print(f"text[:5] = '{text[:5]}'")       # Hello (처음부터)
print(f"text[7:] = '{text[7:]}'")       # Python! (끝까지)
print(f"text[:] = '{text[:]}'")         # Hello, Python! (전체 복사)

# 음수 인덱스 사용
print(f"text[-7:] = '{text[-7:]}'")     # Python!
print(f"text[-7:-1] = '{text[-7:-1]}'") # Python (느낌표 제외)
```

---

### [예제 3-3] 슬라이싱 — 간격(step) 활용

```python
numbers = "0123456789"

# [시작:끝:간격]
print(f"짝수 인덱스: {numbers[::2]}")     # 02468
print(f"홀수 인덱스: {numbers[1::2]}")    # 13579
print(f"3칸씩: {numbers[::3]}")           # 0369

# 역순 (step = -1)
print(f"역순: {numbers[::-1]}")           # 9876543210

# 문자열 뒤집기!
word = "desserts"
reversed_word = word[::-1]
print(f"'{word}' 뒤집기 = '{reversed_word}'")  # stressedD

# 회문(팰린드롬) 확인
palindrome = "level"
is_palindrome = palindrome == palindrome[::-1]
print(f"'{palindrome}'은 회문인가? {is_palindrome}")  # True

not_palindrome = "hello"
print(f"'{not_palindrome}'은 회문인가? {not_palindrome == not_palindrome[::-1]}")  # False
```

---

### [예제 3-4] 슬라이싱 실전 — 데이터 처리

```python
# 1. 주민번호에서 정보 추출
ssn = "990101-1234567"
birthday = ssn[:6]
gender_code = ssn[7]

print("=== 주민번호 분석 ===")
print(f"주민번호: {ssn}")
print(f"생년월일: {birthday}")
print(f"성별코드: {gender_code}", end=" → ")
print("남성" if gender_code in ('1', '3') else "여성")

# 2. 전화번호 마스킹
phone = "010-1234-5678"
masked = phone[:4] + "****" + phone[8:]
print(f"\n전화번호 마스킹: {phone} → {masked}")

# 3. 파일 확장자 추출
filename = "my_photo.jpg"
extension = filename[filename.find("."):]
print(f"\n파일명: {filename}")
print(f"확장자: {extension}")

# 4. URL에서 도메인 추출
url = "https://www.python.org/downloads"
domain = url.split("/")[2]
print(f"\nURL: {url}")
print(f"도메인: {domain}")
```

---

### [예제 3-5] 문자열 포매팅 — 3가지 방법 비교

```python
name = "김파이"
age = 20
score = 95.678

print("=== 방법 1: % 연산자 (구형) ===")
print("이름: %s" % name)
print("나이: %d세" % age)
print("점수: %.1f점" % score)
print("이름: %s, 나이: %d세" % (name, age))

print("\n=== 방법 2: format() 메서드 ===")
print("이름: {}".format(name))
print("이름: {}, 나이: {}세".format(name, age))
print("이름: {0}, 나이: {1}세, 다시 이름: {0}".format(name, age))
print("이름: {n}, 나이: {a}세".format(n=name, a=age))

print("\n=== 방법 3: f-string (★ 권장!) ===")
print(f"이름: {name}")
print(f"나이: {age}세")
print(f"점수: {score:.1f}점")    # 소수점 1자리
print(f"점수: {score:.2f}점")    # 소수점 2자리

# f-string 안에서 계산도 가능!
print(f"내년 나이: {age + 1}세")
print(f"이름 길이: {len(name)}자")
```

> 💡 **결론**: f-string이 가장 읽기 쉽고 편리합니다. 이것만 기억하세요!

---

### [예제 3-6] f-string 고급 활용

```python
# 1. 정렬
name = "파이썬"
print(f"|{name:<10}|")   # 왼쪽 정렬 (10칸)
print(f"|{name:>10}|")   # 오른쪽 정렬
print(f"|{name:^10}|")   # 가운데 정렬
print(f"|{name:=^10}|")  # 가운데 정렬 + '='로 채우기
print(f"|{name:*>10}|")  # 오른쪽 정렬 + '*'로 채우기

# 2. 숫자 포맷
price = 1234567
print(f"\n가격: {price:,}원")         # 1,234,567원 (천 단위 콤마)
print(f"가격: {price:>15,}원")       # 오른쪽 정렬 + 콤마
print(f"가격: ₩{price:,.0f}")       # 통화 형식

# 3. 퍼센트
ratio = 0.856
print(f"\n비율: {ratio:.1%}")         # 85.6%
print(f"비율: {ratio:.0%}")          # 86%

# 4. 진법 변환
num = 255
print(f"\n10진법: {num}")
print(f"2진법:  {num:b}")    # 11111111
print(f"8진법:  {num:o}")    # 377
print(f"16진법: {num:x}")    # ff
print(f"16진법: {num:X}")    # FF

# 5. 별 찍기 활용
for i in range(1, 6):
    print(f"{'★' * i:>10}")    # 오른쪽 정렬
```

---

### [예제 3-7] 문자열 메서드 — 변환

```python
text = "Hello, Python World!"

# 대소문자 변환
print(f"원본:   '{text}'")
print(f"대문자: '{text.upper()}'")     # HELLO, PYTHON WORLD!
print(f"소문자: '{text.lower()}'")     # hello, python world!
print(f"제목체: '{text.title()}'")     # Hello, Python World!
print(f"첫글자: '{text.capitalize()}'") # Hello, python world!
print(f"반전:   '{text.swapcase()}'")  # hELLO, pYTHON wORLD!

# 공백 제거
messy = "   파이썬   "
print(f"\n원본:       '[{messy}]'")
print(f"양쪽 제거:  '[{messy.strip()}]'")
print(f"왼쪽 제거:  '[{messy.lstrip()}]'")
print(f"오른쪽 제거: '[{messy.rstrip()}]'")

# 특정 문자 제거도 가능
dashes = "---hello---"
print(f"\n대시 제거: '{dashes.strip('-')}'")   # hello
```

---

### [예제 3-8] 문자열 메서드 — 검색

```python
msg = "파이썬은 재미있고 파이썬은 쉽다"

# find(): 첫 번째 위치 반환 (없으면 -1)
print(f"'파이썬' 첫 위치: {msg.find('파이썬')}")     # 0
print(f"'파이썬' 마지막 위치: {msg.rfind('파이썬')}")  # 9
print(f"'자바' 위치: {msg.find('자바')}")              # -1 (없음)

# index(): find와 같지만, 없으면 에러 발생!
# msg.index("자바")   # ❌ ValueError!

# count(): 등장 횟수
print(f"'파이썬' 횟수: {msg.count('파이썬')}")    # 2
print(f"'은' 횟수: {msg.count('은')}")            # 2

# in 연산자 (포함 여부)
print(f"\n'파이썬' in msg: {'파이썬' in msg}")    # True
print(f"'자바' in msg: {'자바' in msg}")          # False
print(f"'자바' not in msg: {'자바' not in msg}")  # True

# startswith / endswith
filename = "report_2024.pdf"
print(f"\n'{filename}':")
print(f"  'report'로 시작? {filename.startswith('report')}")   # True
print(f"  '.pdf'로 끝? {filename.endswith('.pdf')}")            # True
print(f"  '.xlsx'로 끝? {filename.endswith('.xlsx')}")          # False
```

---

### [예제 3-9] 문자열 메서드 — 치환, 분리, 결합

```python
# === replace(): 치환 ===
msg = "I like Java and Java is great"
new_msg = msg.replace("Java", "Python")
print(f"치환: '{new_msg}'")

# 첫 번째만 치환
first_only = msg.replace("Java", "Python", 1)
print(f"첫 번째만: '{first_only}'")

# === split(): 분리 → 리스트 ===
csv_data = "사과,바나나,딸기,포도,수박"
fruits = csv_data.split(",")
print(f"\nCSV 분리: {fruits}")

sentence = "파이썬은 정말 재미있는 프로그래밍 언어입니다"
words = sentence.split()     # 공백 기준 분리
print(f"단어 분리: {words}")
print(f"단어 수: {len(words)}개")

# maxsplit: 최대 분리 횟수
data = "이름:나이:직업:도시"
print(f"2번만 분리: {data.split(':', 2)}")  # ['이름', '나이', '직업:도시']

# === join(): 결합 ===
items = ['빵', '우유', '계란', '치즈']
result = ", ".join(items)
print(f"\n장보기 목록: {result}")

# 경로 만들기
path_parts = ["home", "user", "documents", "file.txt"]
path = "/".join(path_parts)
print(f"경로: {path}")

# 숫자 리스트를 문자열로
numbers = [1, 2, 3, 4, 5]
num_str = "-".join(str(n) for n in numbers)
print(f"숫자 결합: {num_str}")
```

---

### [예제 3-10] 문자열 메서드 — 판별 메서드

```python
# 문자열의 성질을 True/False로 확인

# isdigit(): 숫자로만 구성?
print("'12345'.isdigit():", "12345".isdigit())       # True
print("'12.34'.isdigit():", "12.34".isdigit())       # False (점은 숫자 아님)
print("'hello'.isdigit():", "hello".isdigit())       # False

# isalpha(): 문자로만 구성?
print("\n'hello'.isalpha():", "hello".isalpha())     # True
print("'파이썬'.isalpha():", "파이썬".isalpha())     # True
print("'hello1'.isalpha():", "hello1".isalpha())     # False

# isalnum(): 문자 또는 숫자로만 구성?
print("\n'hello123'.isalnum():", "hello123".isalnum()) # True
print("'hello 123'.isalnum():", "hello 123".isalnum()) # False (공백)

# isspace(): 공백으로만 구성?
print("\n'   '.isspace():", "   ".isspace())         # True
print("'\\t\\n'.isspace():", "\t\n".isspace())       # True

# isupper() / islower(): 대문자/소문자?
print("\n'HELLO'.isupper():", "HELLO".isupper())     # True
print("'hello'.islower():", "hello".islower())       # True

# === 실전 활용: 입력값 검증 ===
print("\n=== 입력값 검증 ===")
test_inputs = ["12345", "abc", "abc123", "010-1234", "   "]
for inp in test_inputs:
    print(f"  '{inp}' → 숫자:{inp.isdigit()}, 문자:{inp.isalpha()}, 알파벳+숫자:{inp.isalnum()}")
```

---

## 🏆 도전 과제

### [도전 1] 이메일 유효성 검사기

```python
# 이메일 주소를 입력받아 간단한 유효성 검사

email = input("이메일 주소를 입력하세요: ")

# 검사 조건
has_at = "@" in email
has_dot = "." in email
no_space = " " not in email
long_enough = len(email) >= 5

if has_at and has_dot and no_space and long_enough:
    # @ 기준으로 분리
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]

    print(f"\n✅ 유효한 이메일 형식!")
    print(f"  사용자명: {username}")
    print(f"  도메인: {domain}")
    print(f"  전체 길이: {len(email)}자")
else:
    print("\n❌ 유효하지 않은 이메일 형식!")
    if not has_at:
        print("  → '@'이 없습니다")
    if not has_dot:
        print("  → '.'이 없습니다")
    if not no_space:
        print("  → 공백이 포함되어 있습니다")
    if not long_enough:
        print("  → 너무 짧습니다 (5자 이상)")
```

### [도전 2] 문자열 통계 프로그램

```python
# 입력받은 문자열의 다양한 통계를 분석

text = input("문자열을 입력하세요: ")

# 분석
total = len(text)
spaces = text.count(" ")
uppers = sum(1 for c in text if c.isupper())
lowers = sum(1 for c in text if c.islower())
digits = sum(1 for c in text if c.isdigit())
others = total - spaces - uppers - lowers - digits

print(f"\n📊 문자열 통계")
print(f"  전체 길이: {total}자")
print(f"  공백: {spaces}개")
print(f"  대문자: {uppers}개")
print(f"  소문자: {lowers}개")
print(f"  숫자: {digits}개")
print(f"  특수문자: {others}개")
print(f"  단어 수: {len(text.split())}개")
```

---

## 📝 3차시 요약

| 배운 것 | 설명 | 예시 |
|---------|------|------|
| 인덱싱 | 특정 위치의 글자 | `"Hello"[0]` → `'H'` |
| 음수 인덱싱 | 뒤에서부터 | `"Hello"[-1]` → `'o'` |
| 슬라이싱 | 부분 문자열 | `"Hello"[1:4]` → `'ell'` |
| 역순 슬라이싱 | 뒤집기 | `"Hello"[::-1]` → `'olleH'` |
| f-string | 문자열 포매팅 | `f"나이: {age}"` |
| `upper()/lower()` | 대소문자 변환 | `"hi".upper()` → `"HI"` |
| `strip()` | 공백 제거 | `" hi ".strip()` → `"hi"` |
| `replace()` | 치환 | `"ab".replace("a","x")` → `"xb"` |
| `split()` | 분리 | `"a,b".split(",")` → `['a','b']` |
| `join()` | 결합 | `"-".join(['a','b'])` → `"a-b"` |
| `find()` | 검색 | `"hello".find("ll")` → `2` |
| `count()` | 횟수 | `"hello".count("l")` → `2` |

### 다음 시간 예고
> 4차시에서는 **리스트와 튜플**을 배웁니다. 여러 개의 값을 하나로 묶어서 관리하는 방법을 배워요! 📋
