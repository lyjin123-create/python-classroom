# 📌 부록: API·웹 크롤링 & 클라우드 배포 맛보기

| 항목 | 내용 |
|:---:|------|
| **주제** | 외부 REST API 연동, `requests` 라이브러리, BeautifulSoup 웹 크롤링, 클라우드 배포 |
| **시간** | 50분 (강의 20분 + 실습 30분) |
| **선수 지식** | 15차시 전체 |
| **목표** | 인터넷 상의 방대한 오픈 데이터를 수집하고, 내가 만든 웹앱을 세상에 공개하는 방법을 체험한다 |

---

## 🎯 학습 목표

1. **REST API**의 기본 개념을 알고, `requests` 라이브러리로 날씨/환율 데이터를 받아온다.
2. **웹 크롤링(Web Crawling)**의 원리를 이해하고, BeautifulSoup으로 웹 페이지의 텍스트를 추출한다.
3. 내 로컬 컴퓨터에서만 돌던 Flask 앱을 전 세계 누구나 접속할 수 있도록 **클라우드에 무료 배포**하는 흐름을 안다.

---

## 📖 1. REST API와 requests 라이브러리

### API란 무엇인가요?
> 💡 **비유**: 레스토랑의 **"주문 키오스크"** 또는 **"웨이터"** 👨‍🍳  
> 우리가 다른 회사의 데이터베이스에 직접 들어갈 수는 없지만, 그 회사가 열어둔 공식 창구(API)로 "서울의 오늘 날씨 알려줘"라고 요청하면 정해진 규격(JSON)으로 답변을 전달해 줍니다.

```bash
# 필수 라이브러리 설치
pip install requests beautifulsoup4
```

```python
import requests

# 인터넷 상의 무료 가상 API (게시글 조회)
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# JSON 데이터 파이썬 딕셔너리로 변환
data = response.json()
print("글 제목:", data["title"])
```

---

## 📖 2. 웹 크롤링과 스크래핑 기초

API를 제공하지 않는 일반 웹 페이지에서 원하는 정보(뉴스 헤드라인, 주가 등)를 자동으로 긁어오는 기술입니다.

```python
import requests
from bs4 import BeautifulSoup

# 대상 웹 페이지 HTML 가져오기
url = "https://example.com"
res = requests.get(url)

# HTML 파싱 객체 생성
soup = BeautifulSoup(res.text, "html.parser")

# h1 태그의 글자만 쏙 추출
title = soup.find("h1").get_text()
print("웹페이지 제목:", title)
```

> ⚠️ **크롤링 주의사항**:
> 1. 웹사이트의 `robots.txt` 정책을 반드시 준수해야 합니다.
> 2. 너무 빠른 속도로 반복 요청을 보내면 서버에 부하를 주거나 IP가 차단될 수 있으므로 `time.sleep(1)` 등을 적용합니다.

---

## 📖 3. 클라우드 배포 (Deployment)의 원리

내 컴퓨터에서 실행한 `http://127.0.0.1:5000`은 내 컴퓨터에서만 접속할 수 있습니다.  
친구들에게 링크를 공유하거나 포트폴리오로 제출하려면 **24시간 켜져 있는 클라우드 컴퓨터에 배포**해야 합니다.

### 대표적인 무료/초보자 친화적 호스팅 플랫폼
1. **PythonAnywhere (추천)**: 파이썬 Flask/Django에 특화된 직관적인 무료 웹 호스팅 (`내아이디.pythonanywhere.com` 주소 무료 제공).
2. **Render**: GitHub 저장소와 연동하여 커밋 시 자동 빌드 & 배포 지원.
3. **Railway**: 간편한 컨테이너 기반 클라우드 서비스.

#### PythonAnywhere 배포 기본 4단계
1. [pythonanywhere.com](https://www.pythonanywhere.com) 회원가입
2. 'Files' 탭에서 `app.py`, `templates/`, `static/` 파일 업로드
3. 'Web' 탭에서 'Add a new web app' 클릭 후 Flask 선택
4. 생성된 무료 도메인으로 접속하여 동작 확인!

---

## 💻 실습 예제 (30분)

### [예제 부-1] 실시간 환율 조회 프로그램
- **실생활 시나리오**: 오픈 API를 호출하여 달러/엔화 실시간 환율 가져오기

```python
import requests

def get_exchange_rate():
    # 무료 오픈 환율 API
    url = "https://open.er-api.com/v6/latest/USD"
    res = requests.get(url)
    
    if res.status_code == 200:
        data = res.json()
        rates = data.get("rates", {})
        krw = rates.get("KRW")
        jpy = rates.get("JPY")
        eur = rates.get("EUR")
        
        print("💵 [실시간 주요 환율 (기준: 1 USD)]")
        print("=" * 35)
        print(f"대한민국 원 (KRW): {krw:,.2f}원")
        print(f"일본 엔 (JPY): {jpy:,.2f}엔")
        print(f"유럽 유로 (EUR): {eur:,.2f}유로")
        print("=" * 35)
    else:
        print("환율 정보를 가져오는데 실패했습니다.")

get_exchange_rate()
```

---

### [예제 부-2] 웹 크롤링 — 파이썬 공식 사이트 최신 소식 수집
- **실생활 시나리오**: 파이썬 공식 홈페이지(python.org)의 최신 뉴스 제목 긁어오기

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.python.org"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

# 최신 뉴스 위젯 영역 탐색
news_section = soup.find("div", class_="blog-widget")
if news_section:
    print("📢 [Python.org 최신 블로그 소식]")
    print("=" * 45)
    items = news_section.find_all("li")
    for idx, item in enumerate(items, 1):
        title = item.find("a").get_text()
        date = item.find("time").get_text()
        print(f"{idx}. [{date}] {title}")
    print("=" * 45)
```

---

## 📝 핵심 요약 정리

1. **`requests`**: 사람이 읽기 쉬운 파이썬 대표 HTTP 라이브러리로 `get(url).json()`을 통해 API 데이터를 손쉽게 다룸.
2. **`BeautifulSoup`**: HTML 문서에서 원하는 태그(`find`, `find_all`)와 클래스/아이디를 찾아 텍스트를 추출.
3. **배포(Deploy)**: 로컬 개발 환경(`localhost`)을 벗어나 24시간 가동되는 클라우드 서버에 서비스를 업로드하여 누구나 접근할 수 있게 만드는 과정.
