/**
 * 파이썬 마스터 클래스룸 클라이언트 로직 (Vanilla JS)
 */

document.addEventListener("DOMContentLoaded", () => {
    // --- 상태 관리 (State) ---
    let curriculum = [];
    let currentLessonId = 1;
    let completedLessons = JSON.parse(localStorage.getItem("completed_lessons") || "[]");
    let currentQuiz = null;
    let selectedOptionIndex = null;
    let currentLessonData = null;

    // --- DOM 요소 참조 ---
    const curriculumNav = document.getElementById("curriculumNav");
    const currentLessonTitle = document.getElementById("currentLessonTitle");
    const currentDayChip = document.getElementById("currentDayChip");
    const markdownViewer = document.getElementById("markdownViewer");
    const btnToggleComplete = document.getElementById("btnToggleComplete");
    const completeBtnText = document.getElementById("completeBtnText");
    const totalPercent = document.getElementById("totalPercent");
    const totalProgressBar = document.getElementById("totalProgressBar");
    const completedCountText = document.getElementById("completedCountText");
    const btnResetProgress = document.getElementById("btnResetProgress");
    const btnThemeToggle = document.getElementById("btnThemeToggle");
    const mobileToggleBtn = document.getElementById("mobileToggleBtn");
    const sidebar = document.getElementById("sidebar");

    // 탭 요소
    const tabBtns = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");
    const examplesCountBadge = document.getElementById("examplesCountBadge");

    // 플레이그라운드 요소
    const codeEditor = document.getElementById("codeEditor");
    const exampleSelector = document.getElementById("exampleSelector");
    const btnRunCode = document.getElementById("btnRunCode");
    const btnResetCode = document.getElementById("btnResetCode");
    const btnClearConsole = document.getElementById("btnClearConsole");
    const consoleOutput = document.getElementById("consoleOutput");
    const runStatusBadge = document.getElementById("runStatusBadge");

    // 퀴즈 요소
    const quizQuestion = document.getElementById("quizQuestion");
    const quizOptions = document.getElementById("quizOptions");
    const quizFeedback = document.getElementById("quizFeedback");
    const feedbackTitle = document.getElementById("feedbackTitle");
    const feedbackDesc = document.getElementById("feedbackDesc");
    const btnSubmitQuiz = document.getElementById("btnSubmitQuiz");

    // 페이저 요소
    const btnPrevLesson = document.getElementById("btnPrevLesson");
    const btnNextLesson = document.getElementById("btnNextLesson");
    const pagerInfo = document.getElementById("pagerInfo");

    // --- 1. 테마 초기화 ---
    const savedTheme = localStorage.getItem("preferred_theme") || "light";
    if (savedTheme === "dark") {
        document.body.classList.add("theme-dark");
    }

    btnThemeToggle.addEventListener("click", () => {
        document.body.classList.toggle("theme-dark");
        const isDark = document.body.classList.contains("theme-dark");
        localStorage.setItem("preferred_theme", isDark ? "dark" : "light");
    });

    // 모바일 사이드바 토글
    mobileToggleBtn.addEventListener("click", () => {
        sidebar.classList.toggle("open");
    });

    // --- 2. 커리큘럼 데이터 로딩 ---
    fetchCurriculum();
    fetchAllExamples();

    async function fetchCurriculum() {
        try {
            const res = await fetch("/api/curriculum");
            curriculum = await res.json();
            renderSidebar();
            updateProgress();

            // 저장된 마지막 학습 차시 불러오기
            const lastLessonId = parseInt(localStorage.getItem("last_active_lesson") || "1", 10);
            loadLesson(lastLessonId);
        } catch (err) {
            console.error("커리큘럼 로드 실패:", err);
            markdownViewer.innerHTML = `<p style="color:red;">커리큘럼을 불러오는데 실패했습니다.</p>`;
        }
    }

    // --- 3. 사이드바 아코디언 렌더링 ---
    function renderSidebar() {
        curriculumNav.innerHTML = "";

        curriculum.forEach((dayGroup) => {
            const dayDiv = document.createElement("div");
            dayDiv.className = "day-group open";
            dayDiv.dataset.day = dayGroup.day;

            // Day Header
            const headerBtn = document.createElement("button");
            headerBtn.className = "day-header";
            headerBtn.innerHTML = `
                <span>${dayGroup.dayTitle}</span>
                <span class="arrow-icon">▶</span>
            `;
            headerBtn.addEventListener("click", () => {
                dayDiv.classList.toggle("open");
            });

            // Lesson List
            const listUl = document.createElement("ul");
            listUl.className = "lesson-list";

            dayGroup.lessons.forEach((lesson) => {
                const li = document.createElement("li");

                const itemBtn = document.createElement("button");
                itemBtn.className = `lesson-item-btn ${lesson.id === currentLessonId ? "active" : ""}`;
                itemBtn.dataset.lessonId = lesson.id;

                const isChecked = completedLessons.includes(lesson.id);

                itemBtn.innerHTML = `
                    <div class="lesson-item-left">
                        <span class="lesson-icon">${lesson.icon}</span>
                        <span class="lesson-name">${lesson.title}</span>
                    </div>
                    <div class="lesson-checkbox ${isChecked ? "checked" : ""}" data-id="${lesson.id}" title="완료 체크">
                        ${isChecked ? "✓" : ""}
                    </div>
                `;

                // 차시 클릭 이벤트
                itemBtn.addEventListener("click", (e) => {
                    if (e.target.classList.contains("lesson-checkbox")) {
                        // 체크박스 클릭 토글
                        toggleLessonComplete(lesson.id);
                        e.stopPropagation();
                        return;
                    }
                    loadLesson(lesson.id);
                    if (window.innerWidth <= 900) {
                        sidebar.classList.remove("open");
                    }
                });

                li.appendChild(itemBtn);
                listUl.appendChild(li);
            });

            dayDiv.appendChild(headerBtn);
            dayDiv.appendChild(listUl);
            curriculumNav.appendChild(dayDiv);
        });
    }

    // --- 4. 차시 상세 로딩 및 렌더링 ---
    async function loadLesson(lessonId) {
        currentLessonId = lessonId;
        localStorage.setItem("last_active_lesson", lessonId);

        // 사이드바 활성 상태 갱신
        document.querySelectorAll(".lesson-item-btn").forEach((btn) => {
            btn.classList.toggle("active", parseInt(btn.dataset.lessonId, 10) === lessonId);
        });

        markdownViewer.innerHTML = `<div class="loading-spinner">차시 내용을 불러오는 중...</div>`;

        try {
            const res = await fetch(`/api/lesson/${lessonId}`);
            if (!res.ok) throw new Error("차시 데이터 조회 실패");
            const data = await res.json();
            currentLessonData = data;

            // 상단 타이틀 갱신
            currentDayChip.textContent = data.dayTitle.split(":")[0];
            currentLessonTitle.textContent = data.title;

            // 완료 버튼 상태 갱신
            updateCompleteButtonState();

            // 마크다운 렌더링
            renderMarkdown(data.content);

            // 예제 목록 갱신
            setupExamples(data.examples);

            // 퀴즈 갱신
            setupQuiz(data.quiz);

            // 페이저 갱신
            updatePager();

        } catch (err) {
            console.error("차시 로드 오류:", err);
            markdownViewer.innerHTML = `<p style="color:red;">차시를 불러올 수 없습니다: ${err.message}</p>`;
        }
    }

    // 마크다운 렌더링 및 코드 블록 확장
    function renderMarkdown(mdText) {
        const html = marked.parse(mdText);
        markdownViewer.innerHTML = html;

        // 마크다운 내 pre 블록에 '복사' 및 '실습실로 보내기' 버튼 자동 주입
        markdownViewer.querySelectorAll("pre").forEach((preBlock) => {
            const btnGroup = document.createElement("div");
            btnGroup.className = "pre-btn-group";

            const sendBtn = document.createElement("button");
            sendBtn.className = "code-action-btn send";
            sendBtn.textContent = "💻 실습실로";
            sendBtn.title = "이 코드를 실습실로 가져가기";
            sendBtn.addEventListener("click", () => {
                const codeText = preBlock.querySelector("code")?.innerText || preBlock.innerText;
                codeEditor.value = codeText.trim();
                document.querySelector('.tab-btn[data-tab="playgroundTab"]').click();
            });

            const copyBtn = document.createElement("button");
            copyBtn.className = "code-action-btn copy";
            copyBtn.textContent = "📋 복사";
            copyBtn.title = "코드 클립보드 복사";
            copyBtn.addEventListener("click", () => {
                const codeText = preBlock.querySelector("code")?.innerText || preBlock.innerText;
                navigator.clipboard.writeText(codeText);
                copyBtn.textContent = "✅ 완료!";
                setTimeout(() => { copyBtn.textContent = "📋 복사"; }, 2000);
            });

            btnGroup.appendChild(sendBtn);
            btnGroup.appendChild(copyBtn);
            preBlock.appendChild(btnGroup);
        });
    }

    // 전체 예제 캐시
    let allCurriculumExamples = [];

    async function fetchAllExamples() {
        try {
            const res = await fetch("/api/all_examples");
            allCurriculumExamples = await res.json();
            // 현재 차시 셀렉터 다시 갱신
            if (currentLessonData) {
                setupExamples(currentLessonData.examples);
            }
        } catch (e) {
            console.error("전체 예제 로딩 오류:", e);
        }
    }

    // 예제 목록 바인딩 (현재 차시 예제 + 전체 커리큘럼 예제 통합)
    function setupExamples(examples) {
        exampleSelector.innerHTML = `<option value="">-- 실습 예제 불러오기 (현재 차시 ${examples.length}개) --</option>`;
        examplesCountBadge.textContent = examples.length;

        // 1. 현재 차시 실습 예제 그룹
        if (examples.length > 0) {
            const currGroup = document.createElement("optgroup");
            currGroup.label = `📌 현재 차시 실습 예제 (${examples.length}개)`;
            examples.forEach((ex, idx) => {
                const opt = document.createElement("option");
                opt.value = `curr_${idx}`;
                opt.textContent = `${idx + 1}. ${ex.filename}`;
                currGroup.appendChild(opt);
            });
            exampleSelector.appendChild(currGroup);
        }

        // 2. 전체 커리큘럼 실습 예제 탐색 그룹
        if (allCurriculumExamples.length > 0) {
            allCurriculumExamples.forEach((dayItem) => {
                dayItem.lessons.forEach((l) => {
                    // 현재 차시가 아닌 다른 차시들만 그룹으로 추가
                    if (l.id !== currentLessonId && l.examples && l.examples.length > 0) {
                        const otherGroup = document.createElement("optgroup");
                        otherGroup.label = `📚 ${l.title} (${l.examples.length}개)`;
                        l.examples.forEach((ex, exIdx) => {
                            const opt = document.createElement("option");
                            opt.value = `all_${dayItem.day}_${l.id}_${exIdx}`;
                            opt.textContent = `${exIdx + 1}. ${ex.filename}`;
                            otherGroup.appendChild(opt);
                        });
                        exampleSelector.appendChild(otherGroup);
                    }
                });
            });
        }

        // 첫 번째 예제 자동 채움 (에디터가 비어있을 때)
        if (examples.length > 0 && (!codeEditor.value.trim() || codeEditor.value.includes("Hello, Python World!"))) {
            codeEditor.value = examples[0].code;
            exampleSelector.value = "curr_0";
        }
    }

    // 예제 선택 시 에디터에 로드
    exampleSelector.addEventListener("change", () => {
        const val = exampleSelector.value;
        if (!val) return;

        if (val.startsWith("curr_")) {
            const idx = parseInt(val.replace("curr_", ""), 10);
            if (currentLessonData && currentLessonData.examples[idx]) {
                codeEditor.value = currentLessonData.examples[idx].code;
            }
        } else if (val.startsWith("all_")) {
            const parts = val.split("_");
            const dayNum = parseInt(parts[1], 10);
            const lessonId = parseInt(parts[2], 10);
            const exIdx = parseInt(parts[3], 10);

            const dayObj = allCurriculumExamples.find((d) => d.day === dayNum);
            if (dayObj) {
                const lessonObj = dayObj.lessons.find((l) => l.id === lessonId);
                if (lessonObj && lessonObj.examples[exIdx]) {
                    codeEditor.value = lessonObj.examples[exIdx].code;
                }
            }
        }
    });

    // --- 5. 탭 전환 기능 ---
    tabBtns.forEach((btn) => {
        btn.addEventListener("click", () => {
            tabBtns.forEach((b) => b.classList.remove("active"));
            tabContents.forEach((c) => c.classList.remove("active"));

            btn.classList.add("active");
            const targetId = btn.dataset.tab;
            document.getElementById(targetId).classList.add("active");
        });
    });

    // --- 6. 코드 실행 (Playground) ---
    btnRunCode.addEventListener("click", executePythonCode);

    // Ctrl + Enter 단축키 지원
    codeEditor.addEventListener("keydown", (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
            e.preventDefault();
            executePythonCode();
        }
    });

    async function executePythonCode() {
        const code = codeEditor.value.trim();
        if (!code) {
            alert("실행할 파이썬 코드를 작성해주세요.");
            return;
        }

        runStatusBadge.textContent = "실행 중...";
        runStatusBadge.className = "status-indicator";
        consoleOutput.textContent = "⏳ 파이썬 인터프리터 실행 중...";

        try {
            const res = await fetch("/api/run", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ code: code })
            });

            const result = await res.json();
            consoleOutput.textContent = result.output;

            if (result.success) {
                runStatusBadge.textContent = "성공 ✓";
                runStatusBadge.className = "status-indicator success";
            } else {
                runStatusBadge.textContent = "에러 / 주의 ⚠️";
                runStatusBadge.className = "status-indicator error";
            }
        } catch (err) {
            consoleOutput.textContent = `서버 통신 에러: ${err.message}`;
            runStatusBadge.textContent = "통신 에러";
            runStatusBadge.className = "status-indicator error";
        }
    }

    btnResetCode.addEventListener("click", () => {
        if (confirm("에디터 코드를 지우시겠습니까?")) {
            codeEditor.value = "";
        }
    });

    btnClearConsole.addEventListener("click", () => {
        consoleOutput.textContent = "# 콘솔 출력이 초기화되었습니다.";
        runStatusBadge.textContent = "대기 중";
        runStatusBadge.className = "status-indicator";
    });

    // --- 7. 퀴즈 기능 ---
    function setupQuiz(quiz) {
        currentQuiz = quiz;
        selectedOptionIndex = null;
        quizFeedback.style.display = "none";
        btnSubmitQuiz.disabled = true;

        if (!quiz) {
            quizQuestion.textContent = "이 차시에는 등록된 퀴즈가 없습니다.";
            quizOptions.innerHTML = "";
            return;
        }

        quizQuestion.textContent = quiz.question;
        quizOptions.innerHTML = "";

        quiz.options.forEach((optText, idx) => {
            const optBtn = document.createElement("button");
            optBtn.className = "quiz-option-btn";
            optBtn.textContent = `${idx + 1}. ${optText}`;

            optBtn.addEventListener("click", () => {
                document.querySelectorAll(".quiz-option-btn").forEach((b) => b.classList.remove("selected"));
                optBtn.classList.add("selected");
                selectedOptionIndex = idx;
                btnSubmitQuiz.disabled = false;
            });

            quizOptions.appendChild(optBtn);
        });
    }

    btnSubmitQuiz.addEventListener("click", () => {
        if (!currentQuiz || selectedOptionIndex === null) return;

        const isCorrect = (selectedOptionIndex === currentQuiz.answer);
        const optionButtons = document.querySelectorAll(".quiz-option-btn");

        optionButtons.forEach((btn, idx) => {
            btn.disabled = true;
            if (idx === currentQuiz.answer) {
                btn.classList.add("correct");
            } else if (idx === selectedOptionIndex && !isCorrect) {
                btn.classList.add("wrong");
            }
        });

        quizFeedback.style.display = "block";
        if (isCorrect) {
            quizFeedback.className = "quiz-feedback success";
            feedbackTitle.textContent = "🎉 정답입니다! 완벽히 이해하셨네요.";
        } else {
            quizFeedback.className = "quiz-feedback error";
            feedbackTitle.textContent = "❌ 아쉽습니다! 다시 복습해보세요.";
        }
        feedbackDesc.textContent = currentQuiz.explanation;
        btnSubmitQuiz.disabled = true;

        // 정답을 맞추면 자동으로 해당 차시 완료 처리
        if (isCorrect && !completedLessons.includes(currentLessonId)) {
            toggleLessonComplete(currentLessonId);
        }
    });

    // --- 8. 진도율 관리 (LocalStorage) ---
    btnToggleComplete.addEventListener("click", () => {
        toggleLessonComplete(currentLessonId);
    });

    function toggleLessonComplete(lessonId) {
        const index = completedLessons.indexOf(lessonId);
        if (index > -1) {
            completedLessons.splice(index, 1);
        } else {
            completedLessons.push(lessonId);
        }

        localStorage.setItem("completed_lessons", JSON.stringify(completedLessons));
        updateProgress();
        updateCompleteButtonState();

        // 사이드바 체크박스 상태 동기화
        const checkbox = document.querySelector(`.lesson-checkbox[data-id="${lessonId}"]`);
        if (checkbox) {
            const isChecked = completedLessons.includes(lessonId);
            checkbox.classList.toggle("checked", isChecked);
            checkbox.textContent = isChecked ? "✓" : "";
        }
    }

    function updateCompleteButtonState() {
        const isDone = completedLessons.includes(currentLessonId);
        btnToggleComplete.classList.toggle("completed", isDone);
        completeBtnText.textContent = isDone ? "학습 완료됨 ✓" : "학습 완료로 표시";
    }

    function updateProgress() {
        const total = 16; // 15차시 + 부록 1차시 = 16
        const count = completedLessons.length;
        const percent = Math.min(100, Math.round((count / total) * 100));

        totalPercent.textContent = `${percent}%`;
        totalProgressBar.style.width = `${percent}%`;
        completedCountText.textContent = `${count} / ${total} 차시 완료`;
    }

    btnResetProgress.addEventListener("click", () => {
        if (confirm("모든 학습 진도를 초기화하시겠습니까?")) {
            completedLessons = [];
            localStorage.setItem("completed_lessons", "[]");
            updateProgress();
            updateCompleteButtonState();
            renderSidebar();
        }
    });

    // --- 9. 하단 페이저 (이전/다음 차시 이동) ---
    btnPrevLesson.addEventListener("click", () => {
        if (currentLessonId > 1) {
            loadLesson(currentLessonId - 1);
        }
    });

    btnNextLesson.addEventListener("click", () => {
        if (currentLessonId < 16) {
            loadLesson(currentLessonId + 1);
        }
    });

    function updatePager() {
        btnPrevLesson.disabled = (currentLessonId <= 1);
        btnNextLesson.disabled = (currentLessonId >= 16);
        pagerInfo.textContent = `${currentLessonId} / 16 차시`;
    }
});
