import time

# [예제 7-1] 카운트다운 타이머 (while문)

sec = 5
print("🚀 로켓 발사 카운트다운 시작!")
print("=" * 30)

while sec > 0:
    print(f"{sec}초 전...")
    time.sleep(1)  # 1초 대기
    sec -= 1

print("🎉 부아아앙! 발사 성공! 🚀")
