# 📌 12차시: HTML & Flask 웹 개발 입문

| 항목 | 내용 |
|:---:|------|
| **주제** | 웹 동작 원리(HTTP), HTML 기초, Flask 설치, 첫 웹 서버 실행, 라우팅 |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 11차시 (모듈, pip, 예외 처리) |
| **목표** | Flask를 이용해 내 컴퓨터를 웹 서버로 동작시키고 브라우저로 접속할 수 있다 |

---

## 🎯 학습 목표

1. 웹 브라우저(클라이언트)와 웹 서버의 요청(Request) & 응답(Response) 원리를 이해한다.
2. 웹 페이지의 뼈대를 만드는 HTML 기본 태그의 역할을 안다.
3. 파이썬 마이크로 웹 프레임워크인 **Flask**를 설치하고 실행할 수 있다.
4. `@app.route()` 데코레이터를 이용해 다양한 URL 주소(라우트)를 생성하고 동적 인수를 전달할 수 있다.

---

## 📖 강의 내용 (25분)

### 1. 웹(Web)은 어떻게 동작할까요?

> 💡 **비유**: 식당에서의 주문과 음식 서빙 🍽️  
> 1. 손님(웹 브라우저 / 클라이언트)이 메뉴판을 보고 주문서를 보냅니다 → **요청 (Request)**  
> 2. 주방(웹 서버 / Flask)이 주문을 확인하고 요리를 만듭니다 → **비즈니스 로직 처리**  
> 3. 완성된 요리(HTML, 데이터)를 손님 식탁에 올려놓습니다 → **응답 (Response)**

우리가 주소창에 `http://localhost:5000`을 치는 것은 "내 컴퓨터(localhost)의 5000번 주방에 페이지를 달라고 요청하는 것"입니다.

---

### 2. 웹 페이지의 뼈대: HTML 초스피드 요약

브라우저는 파이썬 코드를 직접 해석하지 못하며, **HTML(글자와 구조)**을 화면에 렌더링합니다.

```html
<!-- 가장 핵심적인 HTML 기본 태그들 -->
<h1>제목 (가장 큰 글자)</h1>
<h2>소제목</h2>
<p>본문 문단 (Paragraph) 글자입니다.</p>
<a href="https://google.com">구글로 이동하는 링크</a>
<ul>
    <li>목록 1</li>
    <li>목록 2</li>
</ul>
<hr> <!-- 가로 구분선 -->
```

---

### 3. Flask란 무엇인가?

- 파이썬으로 웹 서버를 만들 수 있게 해주는 **마이크로(Micro) 웹 프레임워크**입니다.
- 복잡한 설정 없이 코드 5줄로 웹 서버를 띄울 수 있어서 초보자에게 가장 친화적입니다.

#### 설치하기 (터미널)
```bash
pip install flask
```

---

### 4. 세상에서 가장 쉬운 Flask 첫 프로그램 (`app.py`)

```python
from flask import Flask

# Flask 애플리케이션 객체 생성
app = Flask(__name__)

# 라우팅(Routing): 사용자가 '/' 주소로 들어왔을 때 실행할 함수 지정
@app.route("/")
def home():
    return "<h1>안녕하세요! 파이썬 Flask 웹 서버입니다! 🚀</h1>"

# 직접 실행될 때 웹 서버 구동 (포트 기본 5000)
if __name__ == "__main__":
    app.run(debug=True)
```

> 💡 **실행 방법**:
> 터미널에서 `python app.py`를 실행한 후 브라우저를 열고 `http://127.0.0.1:5000`에 접속합니다!  
> `debug=True` 모드에서는 파이썬 코드를 수정하고 저장하면 서버가 자동으로 새로고침됩니다.

---

### 5. URL 라우팅과 동적 변수 (`<변수명>`)

주소에 따라 다른 함수가 실행되게 하거나, 주소창에 적힌 값을 파이썬 변수로 받아올 수 있습니다.

```python
# 1) 고정 라우트
@app.route("/about")
def about():
    return "<p>이 사이트는 초보자 파이썬 코스 실습용 사이트입니다.</p>"

# 2) 동적 라우트 (URL의 일부를 변수로 수신)
@app.route("/hello/<name>")
def hello_user(name):
    return f"<h2>반갑습니다, <strong>{name}</strong>님!</h2>"
```

---

## 💻 실습 예제 (25분)

### [예제 12-1] 기본 HTML 문자열 반환
- **실생활 시나리오**: 카페 매장 안내 웹 페이지

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def cafe_home():
    html_content = """
    <h1>☕ 파이썬 카페에 오신 것을 환영합니다!</h1>
    <p>오늘의 추천 메뉴: <strong>바닐라 빈 라떼</strong></p>
    <ul>
        <li>영업시간: 08:00 ~ 21:00</li>
        <li>위치: 서울시 강남구 테헤란로 123</li>
    </ul>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)
```

---

### [예제 12-2] 다중 페이지 라우팅 (홈 / 소개 / 메뉴)
- **실생활 시나리오**: 여러 메뉴 탭이 있는 미니 웹사이트

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>🏠 홈페이지</h1>
    <nav>
        <a href='/about'>소개</a> | 
        <a href='/menu'>메뉴판</a>
    </nav>
    <p>홈페이지 메인 화면입니다.</p>
    """

@app.route("/about")
def about():
    return """
    <h1>📖 회사 소개</h1>
    <p>우리는 누구나 쉽게 코딩을 배울 수 있도록 돕습니다.</p>
    <a href='/'>← 홈으로 돌아가기</a>
    """

@app.route("/menu")
def menu():
    return """
    <h1>📋 카페 메뉴판</h1>
    <ol>
        <li>아메리카노 - 4,000원</li>
        <li>카페라떼 - 4,500원</li>
        <li>초코쿠키 - 2,500원</li>
    </ol>
    <a href='/'>← 홈으로 돌아가기</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
```

---

### [예제 12-3] 동적 라우팅 — 사용자 맞춤 프로필
- **실생활 시나리오**: SNS처럼 사용자 아이디 주소로 접속 시 프로필 안내

```python
from flask import Flask

app = Flask(__name__)

@app.route("/user/<username>")
def show_user_profile(username):
    return f"""
    <h1>👤 {username}님의 프로필 페이지</h1>
    <p>환영합니다! {username}님은 현재 온라인 상태입니다.</p>
    """

# 숫자형 변수도 받을 수 있음 (<int:변수명>)
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"<h3>📝 제 {post_id}번 게시글 내용을 표시합니다.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
```

---

### [예제 12-4] 웹 계산기 라우트
- **실생활 시나리오**: URL 주소로 숫자를 넘겨 덧셈 결과 반환 (`/add/10/20`)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/add/<int:num1>/<int:num2>")
def add_numbers(num1, num2):
    result = num1 + num2
    return f"""
    <h2>계산 결과</h2>
    <p>{num1} + {num2} = <strong>{result}</strong></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
```

---

### [예제 12-5] 인라인 CSS로 스타일이 적용된 예쁜 카드
- **실생활 시나리오**: 세련된 카드 UI를 브라우저에 표시

```python
from flask import Flask

app = Flask(__name__)

@app.route("/card")
def card():
    return """
    <div style="
        width: 320px;
        margin: 50px auto;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        font-family: sans-serif;
        text-align: center;
        background: #fdfdfd;
    ">
        <h2 style="color: #2c3e50; margin-bottom: 8px;">김파이 (Python Dev)</h2>
        <p style="color: #7f8c8d; font-size: 14px;">청년 성인 파이썬 풀스택 과정 수료</p>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 16px 0;">
        <p style="font-size: 14px; line-height: 1.6;">
            💻 주특기: Python, Flask, Web Scraping<br>
            📧 이메일: kim_python@example.com
        </p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🏆 도전 과제: 나만의 디지털 명함 웹사이트

Flask 앱을 만들어 아래 기능을 구현하세요.
1. `/`: 메인 페이지 (내 이름, 간단한 직업 소개 및 링크 버튼들)
2. `/skills`: 내가 다룰 수 있는 기술 목록 (Python, HTML, Git 등)을 리스트로 표시
3. `/contact`: 내 이메일과 전화번호 안내

각 페이지마다 홈으로 돌아갈 수 있는 `<a href='/'>홈으로</a>` 링크를 포함하세요.

---

## 📝 핵심 요약 정리

1. **클라이언트-서버 모델**: 사용자가 주소를 입력해 요청(Request)하면, 웹 서버가 HTML/데이터를 응답(Response).
2. **HTML 기본 태그**: `<h1>`~`<h6>`(제목), `<p>`(문단), `<a>`(링크), `<ul>`/`<li>`(목록).
3. **Flask 초기화 및 실행**:
   - `app = Flask(__name__)`
   - `app.run(debug=True)`
4. **`@app.route('/경로')`**: 특정 URL 주소와 파이썬 처리 함수를 매핑(라우팅).
5. **동적 라우팅**: `/user/<username>`, `/item/<int:item_id>` 형태로 주소의 값을 변수로 받아 처리.
