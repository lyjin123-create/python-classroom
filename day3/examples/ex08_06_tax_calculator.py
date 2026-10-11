# [예제 8-6] 세금 및 실수령액 계산 함수 (다중 반환)

def calc_freelancer_pay(gross_pay):
    """급여에서 3.3% 사업소득세와 실수령액 계산"""
    tax_rate = 0.033
    tax = int(gross_pay * tax_rate)
    net_pay = gross_pay - tax
    return tax, net_pay

# 테스트
contracts = [500000, 1200000, 2500000]

print("📊 프리랜서 3.3% 원천징수 계산표")
print("=" * 45)
print(f"{'계약금액':>12} | {'세금(3.3%)':>10} | {'실수령액':>12}")
print("-" * 45)

for pay in contracts:
    tax, net = calc_freelancer_pay(pay)
    print(f"{pay:>11,}원 | {tax:>9,}원 | {net:>11,}원")
print("=" * 45)
