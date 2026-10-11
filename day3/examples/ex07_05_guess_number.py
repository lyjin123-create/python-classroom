import random

# [예제 7-5] 숫자 맞추기 UP/DOWN 게임 (break + random)

target = random.randint(1, 100)
count = 0

print("🎮 1부터 100 사이의 숫자를 맞춰보세요!")
print("=" * 30)

while True:
    try:
        guess = int(input("숫자를 입력하세요: "))
    except ValueError:
        print("⚠️ 숫자만 입력해주세요.")
        continue

    count += 1
    
    if guess < target:
        print("⬆️ UP! 더 큰 숫자입니다.")
    elif guess > target:
        print("⬇️ DOWN! 더 작은 숫자입니다.")
    else:
        print(f"🎯 정답입니다! 정답은 {target}이었습니다.")
        print(f"👏 총 {count}번 만에 맞추셨습니다!")
        break
