import random

# [예제 6-6] 가위바위보 게임

print("✊✌️🖐️ 가위바위보 게임!")
print("=" * 25)

choices = ["가위", "바위", "보"]

print("1. 가위  2. 바위  3. 보")
user_choice = int(input("선택하세요 (1/2/3): "))

if user_choice < 1 or user_choice > 3:
    print("❌ 1, 2, 3 중에서 선택하세요!")
else:
    user = choices[user_choice - 1]
    computer = random.choice(choices)

    print(f"\n🧑 나: {user}")
    print(f"🤖 컴퓨터: {computer}")
    print()

    if user == computer:
        print("🤝 비겼습니다!")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        print("🎉 이겼습니다! 축하해요!")
    else:
        print("😢 졌습니다... 다시 도전하세요!")
