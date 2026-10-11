from flask import Flask, request, redirect, url_for

# [예제 13-2] 단일 라우트에서 GET(화면 렌더링)과 POST(데이터 수신) 동시 처리

app = Flask(__name__)

# 루트(/)와 /login 경로 모두 지원하여 404 에러 방지
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uid = request.form.get("user_id", "").strip()
        pw = request.form.get("user_pw", "").strip()
        
        if uid == "admin" and pw == "1234":
            return f"""
            <!DOCTYPE html>
            <html lang="ko">
            <head><meta charset="UTF-8"><title>로그인 성공</title></head>
            <body style="font-family: -apple-system, sans-serif; display: flex; justify-content: center; padding-top: 50px;">
                <div style="padding: 24px; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                    <h2 style="color: #10b981; margin-bottom: 8px;">🎉 로그인 성공!</h2>
                    <p>환영합니다, <strong>{uid}</strong> 관리자님.</p>
                    <a href="/login" style="display: inline-block; margin-top: 16px; color: #3b82f6; text-decoration: none;">← 로그아웃 / 다시 로그인</a>
                </div>
            </body>
            </html>
            """
        else:
            return f"""
            <!DOCTYPE html>
            <html lang="ko">
            <head><meta charset="UTF-8"><title>로그인 실패</title></head>
            <body style="font-family: -apple-system, sans-serif; display: flex; justify-content: center; padding-top: 50px;">
                <div style="padding: 24px; border: 1px solid #fee2e2; border-radius: 12px; background: #fff5f5; text-align: center;">
                    <h2 style="color: #ef4444; margin-bottom: 8px;">❌ 로그인 실패</h2>
                    <p style="color: #64748b;">아이디 또는 비밀번호가 올바르지 않습니다.</p>
                    <p style="font-size: 13px; color: #94a3b8;">(힌트: 아이디 admin / 비밀번호 1234)</p>
                    <a href="/login" style="display: inline-block; margin-top: 16px; color: #ef4444; font-weight: bold; text-decoration: none;">← 다시 시도하기</a>
                </div>
            </body>
            </html>
            """

    # GET 요청 시 로그인 폼 화면 반환
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>관리자 로그인</title>
    </head>
    <body style="font-family: -apple-system, sans-serif; background: #f8fafc; display: flex; justify-content: center; padding-top: 60px;">
        <div style="width: 100%; max-width: 320px; background: white; padding: 28px; border: 1px solid #e2e8f0; border-radius: 16px; box-shadow: 0 8px 16px rgba(0,0,0,0.05);">
            <h2 style="margin-top: 0; color: #1e293b; text-align: center; font-size: 20px;">🔑 관리자 로그인</h2>
            <form action="/login" method="POST" style="margin-top: 20px;">
                <div style="margin-bottom: 12px;">
                    <label style="display: block; font-size: 13px; color: #64748b; margin-bottom: 4px;">아이디</label>
                    <input type="text" name="user_id" placeholder="admin" required style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; box-sizing: border-box; outline: none;">
                </div>
                <div style="margin-bottom: 18px;">
                    <label style="display: block; font-size: 13px; color: #64748b; margin-bottom: 4px;">비밀번호</label>
                    <input type="password" name="user_pw" placeholder="1234" required style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; box-sizing: border-box; outline: none;">
                </div>
                <button type="submit" style="width: 100%; padding: 12px; background: #3b82f6; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">로그인</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    print("🚀 Flask 로그인 폼 테스트 서버 시작!")
    print("👉 브라우저에서 http://127.0.0.1:5000 또는 http://127.0.0.1:5000/login 으로 접속하세요.")
    app.run(debug=True)
