# [예제 8-8] 카페 주문 및 결제 시스템 (함수 모듈화 & 조합)

MENU = {
    "아메리카노": 4000,
    "카페라떼": 4500,
    "바닐라라떼": 5000,
    "치즈케이크": 6000
}

def get_item_price(item_name, qty):
    """메뉴 가격과 수량으로 소계 계산"""
    price = MENU.get(item_name, 0)
    return price * qty

def apply_membership(total, is_member):
    """멤버십 회원 10% 할인"""
    if is_member:
        discount = int(total * 0.1)
        return total - discount, discount
    return total, 0

def print_receipt(customer_name, items, is_member=False):
    """영수증 출력"""
    print("\n" + "=" * 35)
    print("        ☕ 스타파이썬 영수증")
    print(f" 고객명: {customer_name}")
    print("-" * 35)
    
    total = 0
    for name, qty in items:
        subtotal = get_item_price(name, qty)
        total += subtotal
        print(f" {name:<10} {qty:>2}개 {subtotal:>10,}원")
        
    print("-" * 35)
    final_price, discount = apply_membership(total, is_member)
    print(f" 주문 금액:{total:>22,}원")
    if is_member:
        print(f" 멤버십할인(10%):{-discount:>17,}원")
    print(f" 최종 결제액:{final_price:>20,}원")
    print("=" * 35)

# 주문 실행 테스트
my_orders = [("아메리카노", 2), ("치즈케이크", 1)]
print_receipt("홍길동", my_orders, is_member=True)
