from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# 데이터 파일 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "todos.json")

def load_todos():
    """todos.json 파일에서 할 일 목록을 읽어옵니다."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_todos(todos):
    """할 일 목록을 todos.json 파일에 저장합니다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

# 1. READ: 할 일 목록 조회
@app.route("/")
def index():
    todos = load_todos()
    total = len(todos)
    done_cnt = len([t for t in todos if t.get("done")])
    rate = int((done_cnt / total) * 100) if total > 0 else 0
    return render_template("index.html", todos=todos, total=total, done_cnt=done_cnt, rate=rate)

# 2. CREATE: 할 일 추가
@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "개인")
    if title:
        todos = load_todos()
        new_id = max([t["id"] for t in todos], default=0) + 1
        todos.append({
            "id": new_id,
            "title": title,
            "category": category,
            "done": False
        })
        save_todos(todos)
    return redirect(url_for("index"))

# 3. UPDATE: 완료 여부 토글
@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    save_todos(todos)
    return redirect(url_for("index"))

# 4. DELETE: 할 일 삭제
@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    todos = load_todos()
    todos = [todo for todo in todos if todo["id"] != todo_id]
    save_todos(todos)
    return redirect(url_for("index"))

if __name__ == "__main__":
    print("🚀 할 일 관리 웹 애플리케이션 시작!")
    print("👉 브라우저에서 http://127.0.0.1:5000 으로 접속하세요.")
    app.run(debug=True)
