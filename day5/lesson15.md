# 📌 15차시: 미니 프로젝트 완성 & 종합 회고

| 항목 | 내용 |
|:---:|------|
| **주제** | Todo 웹앱 기능 확장, 코드 리팩터링, 프로젝트 공유·발표, 5일간의 종합 회고 |
| **시간** | 50분 (프로젝트 개선 30분 + 발표 및 피드백 15분 + 총정리 5분) |
| **선수 지식** | 14차시 (CRUD 웹앱 완성) |
| **목표** | 나만의 아이디어를 담은 기능을 추가하여 포트폴리오 첫 웹앱을 완성하고, 배운 내용을 정리한다 |

---

## 🎯 학습 목표

1. 14차시의 기본 Todo 앱을 바탕으로 사용자 맞춤형 추가 기능을 기획하고 구현할 수 있다.
2. 예외 처리, 코드 가독성, UI/UX 관점에서 완성도를 높인다.
3. 자신이 만든 결과물을 동료들에게 시연하고 피드백을 주고받는다.
4. Day 1부터 Day 5까지 배운 파이썬 핵심 기술 스택을 총정리하고 다음 학습 로드맵을 수립한다.

---

## 🚀 프로젝트 개선 미션 (30분)

원하는 미션을 1~2개 선택하여 나만의 차별화된 Todo 앱을 만들어보세요!

| 난이도 | 선택 미션 | 세부 설명 | 활용 지식 |
|:---:|-----------|-----------|-----------|
| ⭐ | **카테고리 분류** | 업무, 개인, 공부 등 태그 선택 기능 | `<select>`, 딕셔너리 키 |
| ⭐ | **다크 모드 지원** | 깔끔한 어두운 테마 CSS 전환 | CSS 색상 변수, 레이아웃 |
| ⭐⭐ | **마감일 & D-Day** | 날짜 입력받아 남은 일수 계산 | `<input type="date">`, `datetime` |
| ⭐⭐ | **필터링 & 검색** | '전체 / 진행중 / 완료됨' 탭 구분 | 쿼리스트링, 리스트 컴프리헨션 |
| ⭐⭐⭐ | **진행률 프로그레스 바** | "전체 5개 중 3개 완료 (60%)" 시각화 | Jinja2 계산, CSS 게이지 바 |

---

### 💡 미션 구현 힌트 코드

#### 1) 달성률(진행률) 통계 표시
```python
# app.py
todos = load_todos()
total_count = len(todos)
completed_count = len([t for t in todos if t["done"]])
progress_percent = int((completed_count / total_count) * 100) if total_count > 0 else 0

return render_template("index.html", todos=todos, total=total_count, done_cnt=completed_count, rate=progress_percent)
```

```html
<!-- templates/index.html -->
<div style="background: #e2e8f0; border-radius: 8px; overflow: hidden; height: 16px; margin-bottom: 20px;">
    <div style="background: #10b981; height: 100%; width: {{ rate }}%; transition: width 0.3s;"></div>
</div>
<p style="font-size: 13px; color: #64748b; margin-bottom: 16px;">
    진행 현황: {{ done_cnt }}/{{ total }}건 완료 ({{ rate }}%)
</p>
```

---

## 🎤 프로젝트 발표 & 상호 피드백 (15분)

### 1. 2분 스피치 템플릿
- **자기소개**: "안녕하세요, [이름]입니다."
- **추가한 기능**: "저는 기본 기능 외에 [   ] 기능을 추가했습니다."
- **어려웠던 점 & 해결**: "[   ] 부분에서 에러가 났지만, [   ] 방식을 적용해 해결했습니다."
- **느낀 점**: "직접 웹 화면이 뜨는 것을 보니 코딩에 자신감이 생겼습니다."

### 2. 피어 리뷰 (동료 칭찬 문화)
- 잘된 점 1가지 (예: "버튼 색상과 디자인이 정말 깔끔해요!")
- 아이디어 제안 1가지 (예: "중요한 일에 별표(즐겨찾기) 기능이 들어가면 더 좋을 것 같아요!")

---

## 🗺️ 5일간의 파이썬 마스터 여정 총정리

```
[Day 1] 프로그래밍 기초 ──> print, 변수(int/float/str), f-string 문자열 슬라이싱
    │
[Day 2] 데이터 구조 & 분기 ──> 리스트([]), 딕셔너리({}), if-elif-else 조건 판단
    │
[Day 3] 자동화 & 모듈화 ──> for/while 반복문, def 함수, return, 파일 I/O
    │
[Day 4] 설계 & 웹 입문 ──> 클래스(OOP), 모듈(import), 예외 처리, Flask 첫 서버
    │
[Day 5] 풀스택 프로젝트 ──> Jinja2 템플릿, HTML 폼, CRUD 웹앱 완성!
```

---

## 🧭 앞으로의 학습 로드맵 (Next Steps)

파이썬 기초와 웹 프레임워크의 뼈대를 완성하셨습니다. 이제 여러분의 관심사에 따라 다음 길을 걸어가실 수 있습니다!

1. **웹 백엔드 개발자 코스**
   - **FastAPI / Django**: 더 큰 규모의 API 서버 및 엔터프라이즈 프레임워크 학습
   - **데이터베이스 (SQL / SQLite / PostgreSQL)**: 파일 대신 정식 DB에 저장하기
2. **데이터 분석 & 시각화 코스**
   - **Pandas**: 엑셀 데이터 수백만 줄을 1초 만에 분석
   - **Matplotlib / Seaborn**: 차트, 그래프 시각화
3. **업무 자동화 & 인공지능 (AI) 코스**
   - **Selenium / BeautifulSoup**: 웹 크롤링 및 엑셀 자동화 매크로
   - **OpenAI API / LangChain**: ChatGPT를 내 파이썬 프로그램에 연결하기

> 🎓 **수료를 축하합니다!**  
> 이제 여러분은 단순한 컴퓨터 사용자가 아니라, **필요한 프로그램을 직접 만들 수 있는 창작자(Maker)**입니다.
