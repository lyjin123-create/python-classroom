from flask import Flask

# [예제 12-2] Flask 기본 다중 페이지 및 동적 라우팅 예제
# 실행: python ex12_02_flask_routes.py 후 웹 브라우저에서 http://127.0.0.1:5000 접속

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🌐 파이썬 Flask 웹 애플리케이션</h1>
    <p>웹 개발의 첫걸음에 오신 것을 환영합니다!</p>
    <ul>
        <li><a href='/about'>소개 페이지</a></li>
        <li><a href='/user/홍길동'>홍길동 프로필</a></li>
        <li><a href='/user/김파이'>김파이 프로필</a></li>
    </ul>
    """

@app.route("/about")
def about():
    return """
    <h2>📖 서비스 소개</h2>
    <p>파이썬 Flask로 만든 초간단 웹 서버입니다.</p>
    <a href='/'>← 홈으로 돌아가기</a>
    """

@app.route("/user/<username>")
def user_profile(username):
    return f"""
    <h2>👤 {username}님의 회원 페이지</h2>
    <p>환영합니다, {username}님!</p>
    <a href='/'>← 홈으로 돌아가기</a>
    """

if __name__ == "__main__":
    print("🚀 Flask 웹 서버를 시작합니다...")
    print("👉 브라우저 주소창에 http://127.0.0.1:5000 을 입력하세요!")
    app.run(debug=True)
