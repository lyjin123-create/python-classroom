# 📌 14차시: CRUD 웹앱 완성 (할 일 관리 Todo 앱)

| 항목 | 내용 |
|:---:|------|
| **주제** | CRUD 개념, 데이터 모델링, JSON 영구 저장, `redirect()` & `url_for()`, 완성형 웹앱 |
| **시간** | 50분 (강의 20분 + 실습 30분) |
| **선수 지식** | 13차시 (Flask 템플릿, 폼, POST) |
| **목표** | 일상에서 유용하게 쓸 수 있는 할 일 관리(Todo) 웹앱의 CRUD 전체 기능을 완성한다 |

---

## 🎯 학습 목표

1. 웹 서비스 개발의 핵심인 **CRUD (Create, Read, Update, Delete)** 사이클을 이해한다.
2. 할 일 데이터를 식별하기 위한 고유 `id`와 데이터 구조를 설계할 수 있다.
3. 폼 제출 후 페이지를 안전하게 이동시키는 `redirect(url_for(...))` 패턴을 익힌다.
4. 추가, 조회, 완료 체크(토글), 삭제 기능을 모두 갖춘 실제 웹 애플리케이션을 완성한다.

---

## 📖 강의 내용 (20분)

### 1. CRUD(크루드)란 무엇인가?

모든 웹 서비스(인스타그램, 배달의민족, 유튜브, 노션)의 95% 이상은 다음 4가지 동작으로 이루어집니다.

| 용어 | 명칭 | Todo 앱에서의 역할 | HTTP 방식 |
|:---:|:---:|------|:---:|
| **C** | **Create** (생성) | 새로운 할 일 작성 및 등록 | `POST` |
| **R** | **Read** (읽기/조회) | 등록된 할 일 목록 화면에 표시 | `GET` |
| **U** | **Update** (수정) | 할 일을 '완료' 상태로 체크/해제 | `POST` |
| **D** | **Delete** (삭제) | 완료되었거나 취소된 할 일 제거 | `POST` |

---

### 2. URL 라우팅 및 데이터 구조 설계

#### 데이터 구조 (딕셔너리 리스트)
```python
todos = [
    {"id": 1, "title": "파이썬 교안 복습하기", "done": False},
    {"id": 2, "title": "퇴근 후 30분 조깅", "done": True}
]
```

#### 라우트 설계
1. `GET /`: 전체 할 일 목록 보기 (Read)
2. `POST /add`: 폼에서 입력받아 새 할 일 추가 (Create)
3. `POST /toggle/<int:todo_id>`: 완료 여부(`done`)를 True↔False 뒤집기 (Update)
4. `POST /delete/<int:todo_id>`: 해당 id의 할 일 목록에서 제거 (Delete)

---

### 3. `redirect()`와 `url_for()`의 중요성

폼을 `POST`로 제출한 뒤 단순히 같은 HTML을 렌더링하면, 사용자가 브라우저에서 '새로고침(F5)'을 누를 때마다 **"양식 재전송" 경고와 함께 할 일이 중복 등록**되는 버그가 발생합니다.  
이를 방지하는 웹 표준 디자인 패턴이 **PRG (Post-Redirect-Get)** 패턴입니다.

```python
from flask import redirect, url_for

# 데이터를 처리한 뒤 바로 목록 페이지('/')로 브라우저를 이동시킴
return redirect(url_for("index"))
```

---

## 💻 단계별 실습 (30분)

### 1단계: 백엔드 로직 (`app.py`)

```python
from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DATA_FILE = "todos.json"

# --- 데이터 읽기/쓰기 헬퍼 함수 ---
def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


# 1. READ (할 일 목록 보기)
@app.route("/")
def index():
    todos = load_todos()
    return render_template("index.html", todos=todos)


# 2. CREATE (할 일 추가)
@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title", "").strip()
    if title:
        todos = load_todos()
        # 새 ID 발급: 기존 최대 ID + 1
        new_id = max([t["id"] for t in todos], default=0) + 1
        todos.append({
            "id": new_id,
            "title": title,
            "done": False
        })
        save_todos(todos)
    return redirect(url_for("index"))


# 3. UPDATE (완료 상태 토글)
@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    save_todos(todos)
    return redirect(url_for("index"))


# 4. DELETE (할 일 삭제)
@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    todos = load_todos()
    todos = [todo for todo in todos if todo["id"] != todo_id]
    save_todos(todos)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
```

---

### 2단계: 프론트엔드 화면 (`templates/index.html`)

깔끔하고 현대적인 반응형 UI 디자인을 적용한 템플릿입니다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>스마트 할 일 관리 (Todo App)</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: #f0f2f5; display: flex; justify-content: center; padding: 40px 16px; }
        .container { background: #ffffff; width: 100%; max-width: 520px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.06); padding: 28px; }
        h1 { color: #1e293b; font-size: 24px; font-weight: 700; margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }
        
        .add-form { display: flex; gap: 8px; margin-bottom: 24px; }
        .add-input { flex: 1; padding: 12px 16px; border: 1px solid #cbd5e1; border-radius: 10px; font-size: 15px; outline: none; transition: border 0.2s; }
        .add-input:focus { border-color: #3b82f6; }
        .btn-add { background: #3b82f6; color: white; border: none; padding: 12px 20px; border-radius: 10px; font-weight: 600; cursor: pointer; transition: background 0.2s; }
        .btn-add:hover { background: #2563eb; }
        
        .todo-list { list-style: none; display: flex; flex-direction: column; gap: 10px; }
        .todo-item { display: flex; align-items: center; justify-content: space-between; padding: 14px 16px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; }
        .todo-content { display: flex; align-items: center; gap: 12px; flex: 1; }
        
        .todo-title { font-size: 15px; color: #334155; }
        .todo-title.completed { text-decoration: line-through; color: #94a3b8; }
        
        .btn-toggle { background: #e2e8f0; border: none; padding: 6px 12px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; color: #475569; }
        .btn-toggle.done { background: #dcfce7; color: #15803d; }
        .btn-delete { background: #fee2e2; border: none; padding: 6px 10px; border-radius: 6px; cursor: pointer; color: #b91c1c; font-size: 13px; margin-left: 6px; }
        .btn-delete:hover { background: #fca5a5; }

        .empty-state { text-align: center; color: #94a3b8; padding: 30px 0; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>✅ 나의 할 일 관리</h1>
        
        <!-- 할 일 추가 폼 (CREATE) -->
        <form class="add-form" action="/add" method="POST">
            <input class="add-input" type="text" name="title" placeholder="새로운 할 일을 입력하세요..." required autofocus>
            <button class="btn-add" type="submit">추가</button>
        </form>

        <!-- 할 일 목록 (READ) -->
        <ul class="todo-list">
            {% for todo in todos %}
                <li class="todo-item">
                    <div class="todo-content">
                        <!-- 완료 토글 (UPDATE) -->
                        <form action="/toggle/{{ todo.id }}" method="POST" style="margin: 0;">
                            <button type="submit" class="btn-toggle {% if todo.done %}done{% endif %}">
                                {% if todo.done %}완료됨 ✓{% else %}진행중 ⏳{% endif %}
                            </button>
                        </form>
                        <span class="todo-title {% if todo.done %}completed{% endif %}">{{ todo.title }}</span>
                    </div>

                    <!-- 삭제 (DELETE) -->
                    <form action="/delete/{{ todo.id }}" method="POST" style="margin: 0;">
                        <button type="submit" class="btn-delete" onclick="return confirm('정말 삭제할까요?');">삭제</button>
                    </form>
                </li>
            {% else %}
                <div class="empty-state">등록된 할 일이 없습니다. 오늘 할 일을 등록해보세요! 🎯</div>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

---

## 🏆 도전 과제: 우선순위 및 카테고리 태그 추가

1. 추가 폼에 우선순위 드롭다운(`<select name="priority">`)을 넣어 `[높음/보통/낮음]` 중 하나를 선택할 수 있게 확장해보세요.
2. 각 할 일 옆에 우선순위에 따른 색상 뱃지(예: 높음은 빨간색, 보통은 노란색, 낮음은 회색)를 표시해보세요.

---

## 📝 핵심 요약 정리

1. **CRUD**: 웹 개발의 근본 4대 연산 (Create, Read, Update, Delete).
2. **JSON 파일 영구 저장**: 서버가 재부팅되어도 데이터가 유실되지 않도록 `json.dump()`와 `json.load()` 활용.
3. **PRG 패턴**: 데이터를 생성/수정/삭제한 후에는 반드시 `redirect(url_for(...))`를 호출하여 브라우저의 양식 재전송 버그를 방지.
4. **동적 URL 식별자**: `/toggle/<int:todo_id>`처럼 고유 ID를 전달받아 특정 대상을 정확하게 갱신/삭제.
