import os
import sys
import subprocess
import tempfile
import json
from flask import Flask, render_template, jsonify, request

# Windows 콘솔 UnicodeEncodeError 방지
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

app = Flask(__name__)

# 기본 경로 설정 (Jpy 루트 디렉터리)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 차시별 메타데이터 매핑
CURRICULUM = [
    {
        "day": 1,
        "dayTitle": "1일차: 파이썬 첫걸음 & 데이터 타입",
        "lessons": [
            {"id": 1, "title": "1차시: 파이썬 소개 & 환경 설정", "file": "day1/lesson01.md", "icon": "🐍", "time": "50분", "examples": ["ex01_03_escape.py"]},
            {"id": 2, "title": "2차시: 변수와 자료형", "file": "day1/lesson02.md", "icon": "📦", "time": "50분", "examples": []},
            {"id": 3, "title": "3차시: 문자열 다루기 심화", "file": "day1/lesson03.md", "icon": "✂️", "time": "50분", "examples": []}
        ]
    },
    {
        "day": 2,
        "dayTitle": "2일차: 자료구조와 조건문",
        "lessons": [
            {"id": 4, "title": "4차시: 리스트와 튜플", "file": "day2/lesson04.md", "icon": "📋", "time": "50분", "examples": ["ex04_01_list_basic.py", "ex04_02_list_modify.py"]},
            {"id": 5, "title": "5차시: 딕셔너리와 집합", "file": "day2/lesson05.md", "icon": "📖", "time": "50분", "examples": ["ex05_01_dict_basic.py"]},
            {"id": 6, "title": "6차시: 불 자료형과 조건문", "file": "day2/lesson06.md", "icon": "🔀", "time": "50분", "examples": ["ex06_01_comparison.py", "ex06_06_rps_game.py"]}
        ]
    },
    {
        "day": 3,
        "dayTitle": "3일차: 반복문과 함수",
        "lessons": [
            {"id": 7, "title": "7차시: 반복문 (Loops)", "file": "day3/lesson07.md", "icon": "🔄", "time": "50분", "examples": ["ex07_01_countdown.py", "ex07_05_guess_number.py"]},
            {"id": 8, "title": "8차시: 함수 기초 (Functions)", "file": "day3/lesson08.md", "icon": "🧩", "time": "50분", "examples": ["ex08_06_tax_calculator.py", "ex08_08_cafe_order.py"]},
            {"id": 9, "title": "9차시: 함수 심화 & 파일 I/O", "file": "day3/lesson09.md", "icon": "💾", "time": "50분", "examples": ["ex09_08_csv_sales.py"]}
        ]
    },
    {
        "day": 4,
        "dayTitle": "4일차: 객체지향 & 웹 개발 시작",
        "lessons": [
            {"id": 10, "title": "10차시: 클래스와 객체지향", "file": "day4/lesson10.md", "icon": "🏗️", "time": "50분", "examples": ["ex10_02_bank_account.py"]},
            {"id": 11, "title": "11차시: 모듈 & 예외 처리", "file": "day4/lesson11.md", "icon": "🛡️", "time": "50분", "examples": ["ex11_01_lotto.py"]},
            {"id": 12, "title": "12차시: HTML & Flask 입문", "file": "day4/lesson12.md", "icon": "🌐", "time": "50분", "examples": ["ex12_02_flask_routes.py"]}
        ]
    },
    {
        "day": 5,
        "dayTitle": "5일차: 웹앱 완성 & 종합 프로젝트",
        "lessons": [
            {"id": 13, "title": "13차시: Flask 템플릿 & 폼", "file": "day5/lesson13.md", "icon": "📝", "time": "50분", "examples": ["ex13_02_login_form.py"]},
            {"id": 14, "title": "14차시: CRUD 웹앱 완성", "file": "day5/lesson14.md", "icon": "⚡", "time": "50분", "examples": []},
            {"id": 15, "title": "15차시: 미니 프로젝트 & 회고", "file": "day5/lesson15.md", "icon": "🏆", "time": "50분", "examples": []}
        ]
    },
    {
        "day": 6,
        "dayTitle": "부록: 심화 확장 & 프로젝트",
        "lessons": [
            {"id": 16, "title": "부록: API·크롤링·배포 맛보기", "file": "appendix/lesson_extra.md", "icon": "🚀", "time": "50분", "examples": ["ex_extra_exchange.py"]}
        ]
    }
]

# 차시별 퀴즈 은행
QUIZZES = {
    1: {"question": "파이썬에서 화면에 글자를 출력할 때 사용하는 기본 함수는?", "options": ["echo()", "print()", "printf()", "console.log()"], "answer": 1, "explanation": "파이썬에서는 print() 함수를 사용해 콘솔에 출력합니다."},
    2: {"question": "input() 함수로 사용자 입력을 받으면 반환되는 기본 자료형은?", "options": ["int (정수)", "float (실수)", "str (문자열)", "bool (참/거짓)"], "answer": 2, "explanation": "input()은 사용자가 숫자를 쳐도 항상 문자열(str)로 반환하므로 int() 등으로 형변환해야 합니다."},
    3: {"question": "문자열 text = 'Python'에서 text[0:2] 슬라이싱의 결과는?", "options": ["'Py'", "'Pyt'", "'y'", "'yth'"], "answer": 0, "explanation": "슬라이싱 [시작:끝]은 끝 인덱스를 '포함하지 않으므로' 0번(P)과 1번(y)만 추출되어 'Py'가 됩니다."},
    4: {"question": "리스트와 튜플의 가장 핵심적인 차이점은?", "options": ["리스트는 대괄호 [], 튜플은 소괄호 ()를 사용한다", "리스트는 값을 수정할 수 있지만, 튜플은 수정할 수 없다", "튜플이 리스트보다 메모리를 적게 쓴다", "위 3가지 모두 맞다"], "answer": 3, "explanation": "문법적 표기, 불변성(Immutable), 메모리 효율성 모두 리스트와 튜플의 올바른 차이점입니다."},
    5: {"question": "딕셔너리에서 키(Key)에 해당하는 값을 가져올 때, 키가 없어도 에러 없이 기본값을 돌려주는 메서드는?", "options": [".get()", ".pop()", ".keys()", ".find()"], "answer": 0, "explanation": "dict.get(key, default)를 쓰면 키가 존재하지 않아도 KeyError 대신 기본값을 안전하게 반환합니다."},
    6: {"question": "파이썬에서 여러 조건을 연속해서 검사할 때 쓰는 키워드는?", "options": ["else if", "elif", "elseif", "case"], "answer": 1, "explanation": "파이썬은 else if 대신 간결한 elif 키워드를 사용합니다."},
    7: {"question": "반복문 실행 중 특정 조건을 만나 즉시 반복문 루프 전체를 빠져나오게 하는 키워드는?", "options": ["continue", "break", "pass", "exit"], "answer": 1, "explanation": "break는 즉시 루프를 완전히 종료하며, continue는 이번 차례만 건너뛰고 다음 반복으로 넘어갑니다."},
    8: {"question": "함수에서 처리한 결과값을 호출한 곳으로 전달하고 함수를 끝내는 키워드는?", "options": ["give", "send", "return", "output"], "answer": 2, "explanation": "함수는 return 키워드를 사용해 결과 데이터를 돌려줍니다."},
    9: {"question": "파일을 열고 작업이 끝난 후 자동으로 f.close()를 보장해주는 가장 권장되는 파이썬 문법은?", "options": ["try-catch 문", "with 문", "for-in 문", "while 문"], "answer": 1, "explanation": "with open(...) as f: 구문은 블록을 빠져나갈 때 자동으로 리소스를 닫아줍니다."},
    10: {"question": "클래스 안에서 객체 생성 시 최초 자동 호출되는 생성자 메서드 이름은?", "options": ["__main__", "__init__", "__str__", "__new__"], "answer": 1, "explanation": "__init__(self, ...) 생성자에서 인스턴스 속성을 초기화합니다."},
    11: {"question": "파이썬에서 에러가 발생해도 프로그램이 강제 종료되지 않도록 방어하는 구문은?", "options": ["try - except", "if - else", "do - while", "switch - case"], "answer": 0, "explanation": "try - except 구문으로 예외를 안전하게 가로채 처리합니다."},
    12: {"question": "Flask에서 특정 URL 주소와 파이썬 처리 함수를 연결해주는 데코레이터는?", "options": ["@app.link()", "@app.url()", "@app.route()", "@app.page()"], "answer": 2, "explanation": "@app.route('/경로') 데코레이터로 URL 라우팅을 수행합니다."},
    13: {"question": "Jinja2 템플릿에서 파이썬 변수 값을 HTML 화면에 그대로 출력할 때 쓰는 기호는?", "options": ["{% 변수 %}", "{{ 변수 }}", "<%= 변수 %>", "${ 변수 }"], "answer": 1, "explanation": "{{ 변수 }}는 출력용이며, {% ... %}는 if나 for 같은 제어문용입니다."},
    14: {"question": "웹에서 데이터 생성(Create) 및 비밀번호 제출에 주로 사용되는 안전한 HTTP 전송 방식은?", "options": ["GET", "POST", "FETCH", "SUBMIT"], "answer": 1, "explanation": "POST는 HTTP 요청 바디에 데이터를 실어 보내 데이터 크기 제한이 없고 URL에 노출되지 않습니다."},
    15: {"question": "웹 개발 4대 핵심 연산인 'CRUD'의 약자가 올바른 것은?", "options": ["Code, Run, Update, Debug", "Create, Read, Update, Delete", "Copy, Read, Undo, Delete", "Compile, Run, Use, Deploy"], "answer": 1, "explanation": "CRUD는 Create(생성), Read(조회), Update(수정), Delete(삭제)를 뜻합니다."},
    16: {"question": "파이썬에서 HTTP API를 호출할 때 가장 널리 쓰이는 표준적인 외부 라이브러리는?", "options": ["requests", "beautifulsoup4", "flask", "django"], "answer": 0, "explanation": "requests는 사람이 읽기 쉬운 문법을 제공하는 파이썬 대표 HTTP 라이브러리입니다."}
}

@app.route("/")
def index():
    return render_template("index.html")

import re

def extract_examples_from_markdown(md_content):
    """마크다운 본문에서 [예제 ...] 및 [도전 과제] 아래의 python 코드 블록을 자동 추출"""
    examples = []
    # 패턴: ### [예제 ...] 또는 ## 🏆 도전 과제 이후의 ```python ... ``` 코드 블록 매칭
    pattern = re.compile(
        r'(###\s*\[예제\s*[^\]]+\][^\n]*|##\s*🏆\s*도전\s*과제[^\n]*)(.*?)(```python\s*\n(.*?)\n```)',
        re.DOTALL
    )
    for match in pattern.finditer(md_content):
        raw_title = match.group(1).replace('#', '').strip()
        code = match.group(4).strip()
        if code:
            examples.append({
                "filename": raw_title,
                "code": code
            })
    return examples

def get_lesson_examples(lesson_info):
    """해당 차시의 마크다운 추출 예제와 examples 폴더의 py 파일들을 모두 취합"""
    combined_examples = []

    # 1. 마크다운에서 예제 추출
    md_path = os.path.join(BASE_DIR, lesson_info["file"])
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        extracted = extract_examples_from_markdown(md_content)
        combined_examples.extend(extracted)

    # 2. examples 폴더의 독립 .py 파일들 읽기
    day_folder = lesson_info["file"].split("/")[0]
    examples_dir = os.path.join(BASE_DIR, day_folder, "examples")
    if os.path.exists(examples_dir):
        for ex_file in lesson_info.get("examples", []):
            file_path = os.path.join(examples_dir, ex_file)
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    file_code = f.read().strip()
                # 중복 방지 (이미 마크다운에 없는 파일이면 추가)
                if not any(ex["filename"] == ex_file for ex in combined_examples):
                    combined_examples.append({
                        "filename": f"[파일] {ex_file}",
                        "code": file_code
                    })

    return combined_examples

@app.route("/api/curriculum")
def get_curriculum():
    return jsonify(CURRICULUM)

@app.route("/api/all_examples")
def get_all_examples():
    """1차시부터 16차시(부록)까지 존재하는 모든 실습 예제 모음 반환"""
    all_data = []
    for day in CURRICULUM:
        day_item = {
            "day": day["day"],
            "dayTitle": day["dayTitle"],
            "lessons": []
        }
        for l in day["lessons"]:
            exs = get_lesson_examples(l)
            day_item["lessons"].append({
                "id": l["id"],
                "title": l["title"],
                "examples": exs
            })
        all_data.append(day_item)
    return jsonify(all_data)

@app.route("/api/lesson/<int:lesson_id>")
def get_lesson(lesson_id):
    # 커리큘럼에서 해당 lesson 탐색
    target_lesson = None
    target_day = None
    for day in CURRICULUM:
        for l in day["lessons"]:
            if l["id"] == lesson_id:
                target_lesson = l
                target_day = day
                break
        if target_lesson:
            break

    if not target_lesson:
        return jsonify({"error": "Lesson not found"}), 404

    # 마크다운 파일 내용 읽기
    md_path = os.path.join(BASE_DIR, target_lesson["file"])
    content = ""
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = f"# {target_lesson['title']}\n\n교안 파일을 준비 중입니다."

    # 해당 차시의 모든 예제 추출 (마크다운 예제 + 파일 예제)
    examples_data = get_lesson_examples(target_lesson)

    # 퀴즈 정보
    quiz_data = QUIZZES.get(lesson_id, None)

    return jsonify({
        "id": target_lesson["id"],
        "title": target_lesson["title"],
        "dayTitle": target_day["dayTitle"],
        "time": target_lesson["time"],
        "content": content,
        "examples": examples_data,
        "quiz": quiz_data
    })

@app.route("/api/run", methods=["POST"])
def run_code():
    """브라우저에서 제출한 파이썬 코드를 안전하게 실행하여 stdout/stderr 반환"""
    data = request.get_json() or {}
    code = data.get("code", "").strip()

    if not code:
        return jsonify({"output": "실행할 코드가 없습니다.", "success": False})

    # 안전 검사 (초보자 교육용 환경 보호: 치명적인 OS 삭제 등 방지)
    forbidden = ["rmdir", "shutil.rmtree", "format c:", "os.system"]
    for word in forbidden:
        if word in code:
            return jsonify({"output": f"⚠️ 보안 경고: '{word}' 키워드는 교육용 샌드박스에서 실행할 수 없습니다.", "success": False})

    # 임시 파일에 파이썬 코드 저장 (한글 및 윈도우 UTF-8 입출력 헤더 자동 추가)
    code_with_header = (
        "# -*- coding: utf-8 -*-\n"
        "import sys\n"
        "try:\n"
        "    sys.stdout.reconfigure(encoding='utf-8', errors='replace')\n"
        "    sys.stderr.reconfigure(encoding='utf-8', errors='replace')\n"
        "except Exception:\n"
        "    pass\n\n"
    ) + code

    with tempfile.NamedTemporaryFile("w", suffix=".py", encoding="utf-8", delete=False) as tmp_file:
        tmp_file.write(code_with_header)
        tmp_path = tmp_file.name

    try:
        # 서브프로세스 환경변수: UTF-8 강제
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env["PYTHONUTF8"] = "1"

        # 서브프로세스로 파이썬 실행 (최대 4초 타임아웃)
        res = subprocess.run(
            [sys.executable, tmp_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=4,
            encoding="utf-8",
            errors="replace",
            env=env
        )
        
        stdout_text = res.stdout if res.stdout is not None else ""
        stderr_text = res.stderr if res.stderr is not None else ""

        output = stdout_text
        if stderr_text:
            if output:
                output += "\n--- 에러 로그 ---\n"
            output += stderr_text
        
        success = (res.returncode == 0)
        if not output or not output.strip():
            output = "(실행 완료 - 출력 결과 없음)"
    except subprocess.TimeoutExpired:
        output = "⏰ 실행 시간 초과! (input() 입력 대기 중이거나 무한 루프가 발생했을 수 있습니다)"
        success = False
    except Exception as e:
        output = f"실행 중 예외 발생: {str(e)}"
        success = False
    finally:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass

    return jsonify({"output": output, "success": success})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"[Python Classroom Portal] Server Started on port {port}!")
    print(f"URL: http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
