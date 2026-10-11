import random

# [예제 11-1] 로또 6/45 번호 추첨기 (random 모듈)

def generate_lotto():
    """1부터 45까지 숫자 중 중복 없이 6개 번호를 추첨하여 정렬"""
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

if __name__ == "__main__":
    print("🎰 [동행복권] 이번 주 로또 행운 번호 자동 추첨 5게임")
    print("=" * 45)
    for i in range(1, 6):
        game = generate_lotto()
        formatted = ", ".join(f"{num:2d}" for num in game)
        print(f"Game {i}: [ {formatted} ]")
    print("=" * 45)
    print("✨ 당첨을 기원합니다!")
