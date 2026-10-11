# [예제 10-2] 은행 계좌 클래스 (OOP 입문)

class BankAccount:
    def __init__(self, owner, account_num, initial_balance=0):
        self.owner = owner
        self.account_num = account_num
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("⚠️ 0원 이상 입력해야 합니다.")
            return
        self.balance += amount
        print(f"💰 [{self.owner}님] {amount:,}원 입금 완료! (잔액: {self.balance:,}원)")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"❌ [{self.owner}님] 잔액 부족! (현재 잔액: {self.balance:,}원)")
            return False
        self.balance -= amount
        print(f"💸 [{self.owner}님] {amount:,}원 출금 완료! (잔액: {self.balance:,}원)")
        return True

    def __str__(self):
        return f"🏦 [KB국민] 계좌번호: {self.account_num} | 예금주: {self.owner} | 잔액: {self.balance:,}원"

# 사용 예시
if __name__ == "__main__":
    acc = BankAccount("김철수", "123-456-7890", 10000)
    print(acc)
    acc.deposit(20000)
    acc.withdraw(50000)  # 잔액 부족
    acc.withdraw(15000)  # 성공
    print(acc)
