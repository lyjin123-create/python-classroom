# 📌 13차시: Flask 템플릿 & 폼 (Jinja2 & Form)

| 항목 | 내용 |
|:---:|------|
| **주제** | Jinja2 템플릿 문법, 템플릿 상속, HTML `<form>`, GET vs POST, `request.form` |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 12차시 (Flask 입문) |
| **목표** | Jinja2 템플릿으로 화면과 로직을 분리하고, 폼 입력을 받아 동적 웹 페이지를 만든다 |

---

## 🎯 학습 목표

1. 파이썬 코드 안에 지저분하게 HTML 문자열을 넣는 대신 `render_template()`으로 분리하는 이유를 이해한다.
2. Jinja2 문법(`{{ 변수 }}`, `{% for %}`, `{% if %}`)을 활용해 동적 HTML을 생성할 수 있다.
3. 템플릿 상속(`base.html`, `{% extends %}`)으로 공통 네비게이션과 디자인 레이아웃을 재사용한다.
4. HTML `<form>` 태그와 POST 요청을 통해 사용자 입력 데이터를 Flask 서버로 전달받아 처리할 수 있다.

---

## 📖 강의 내용 (25분)

### 1. 템플릿(Template) 엔진과 Jinja2

파이썬 코드 안에 수십 줄의 HTML 태그를 문자열로 적으면 코드가 너무 복잡해집니다.  
따라서 HTML 전용 파일(`templates/` 폴더)을 따로 두고, 파이썬에서 **데이터(변수)만 쏙쏙 넘겨서 끼워 맞추는 방식**을 사용합니다.

```
프로젝트/
├── app.py
└── templates/        ← 반드시 templates 이름이어야 Flask가 찾음!
    └── index.html
```

#### Jinja2 3대 핵심 문법
1. **`{{ 변수명 }}`**: 파이썬에서 넘겨준 변수 값을 그 자리에 출력
2. **`{% for item in items %} ... {% endfor %}`**: 반복문으로 HTML 태그 반복 생성
3. **`{% if 조건 %} ... {% else %} ... {% endif %}`**: 조건에 따라 HTML 보이기/숨기기

---

### 2. `render_template()` 사용법

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    user = "김파이"
    skills = ["Python", "Flask", "HTML", "CSS"]
    return render_template("index.html", name=user, skill_list=skills)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>홈페이지</title></head>
<body>
    <h1>안녕하세요, {{ name }}님! 👋</h1>
    <h3>보유 기술 목록:</h3>
    <ul>
        {% for s in skill_list %}
            <li>{{ s }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

### 3. 템플릿 상속 (Template Inheritance)

헤더(로고, 메뉴), 푸터(저작권 표시) 등 모든 페이지마다 반복되는 공통 레이아웃을 `base.html` 하나로 통일합니다.

```html
<!-- templates/base.html (공통 틀) -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% block title %}기본 제목{% endblock %}</title>
    <style>
        body { font-family: sans-serif; margin: 30px; }
        nav { background: #333; padding: 12px; border-radius: 8px; }
        nav a { color: white; margin-right: 15px; text-decoration: none; }
    </style>
</head>
<body>
    <nav>
        <a href="/">홈</a>
        <a href="/guestbook">방명록</a>
    </nav>
    
    <main style="margin-top: 20px;">
        <!-- 각 페이지가 채워 넣을 구멍 -->
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

---

### 4. HTML 폼(Form)과 GET vs POST

사용자가 키보드로 입력한 텍스트나 체크박스 데이터를 서버로 보낼 때 `<form>`을 사용합니다.

| 구분 | GET 방식 | POST 방식 |
|:---:|------|------|
| **전송 방식** | URL 주소 뒤에 파라미터가 노출됨 (`?query=검색어`) | HTTP 요청 바디(Body)에 숨겨서 안전하게 전송 |
| **주 용도** | 페이지 조회, 검색, 단순 링크 이동 | 데이터 생성, 비밀번호 제출, 글 작성/수정/삭제 |

```html
<!-- 폼 작성 -->
<form action="/submit" method="POST">
    <input type="text" name="author" placeholder="작성자 이름">
    <input type="text" name="message" placeholder="남길 말씀">
    <button type="submit">등록</button>
</form>
```

```python
# Flask에서 폼 데이터 받기
from flask import request

@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form.get("author")
    msg = request.form.get("message")
    return f"{name}님의 글: '{msg}' 등록 완료!"
```

---

## 💻 실습 예제 (25분)

### [예제 13-1] Jinja2 if문과 for문 실습
- **실생활 시나리오**: 온라인 쇼핑몰 장바구니 품목과 품절 상태 표시

```html
<!-- templates/cart.html -->
<h2>🛒 내 장바구니</h2>
{% if not items %}
    <p>장바구니가 비어 있습니다.</p>
{% else %}
    <ul>
        {% for item in items %}
            <li>
                {{ item.name }} - {{ item.price:, }}원
                {% if item.stock == 0 %}
                    <span style="color: red; font-weight: bold;">[품절]</span>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
{% endif %}
```

---

### [예제 13-2] 단일 라우트에서 GET / POST 모두 처리하기
- **실생활 시나리오**: 로그인 페이지 (처음 접속 시 폼 보여주기, 제출 시 검증)

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        user_pw = request.form.get("user_pw")
        
        if user_id == "admin" and user_pw == "1234":
            return f"<h1>🎉 환영합니다, {user_id} 관리자님!</h1>"
        else:
            return "<h1>❌ 아이디 또는 비밀번호가 틀렸습니다. <a href='/login'>다시 시도</a></h1>"
            
    # GET 요청일 때는 폼 HTML 화면 렌더링
    return """
    <h2>🔑 로그인</h2>
    <form method="POST">
        <p><input type="text" name="user_id" placeholder="아이디"></p>
        <p><input type="password" name="user_pw" placeholder="비밀번호"></p>
        <p><button type="submit">로그인하기</button></p>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🏆 도전 과제: 메모/방명록 등록 웹앱

사용자가 작성자 이름과 메시지를 입력하면, 지금까지 등록된 모든 방명록 목록 아래에 새 메시지가 계속 쌓여서 표시되는 웹 페이지를 만들어보세요.
- 방명록 목록은 파이썬 리스트에 저장합니다: `entries = []`
- `request.method == "POST"`일 때 폼에서 받은 이름과 내용을 딕셔너리로 만들어 리스트에 `.append()`합니다.
- `render_template()`에 리스트를 전달하여 화면에 보여줍니다.

---

## 📝 핵심 요약 정리

1. **Jinja2**: HTML과 파이썬 데이터를 우아하게 연결하는 템플릿 엔진.
2. **`{{ }}` vs `{% %}`**: `{{ }}`는 단순 출력, `{% %}`는 제어문(if, for, extends 등).
3. **템플릿 상속**: `base.html`에 `{% block content %}`를 지정하고, 하위 페이지에서 `{% extends "base.html" %}`로 확장.
4. **HTML 폼과 POST**: 중요한 데이터나 데이터 변경 작업은 반드시 `method="POST"`를 사용하고, Flask에서는 `request.form.get("키")`로 수신.
