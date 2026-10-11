# 📌 10차시: 클래스와 객체지향 프로그래밍 (OOP)

| 항목 | 내용 |
|:---:|------|
| **주제** | 클래스, 객체(인스턴스), `__init__`, `self`, 메서드, 상속 기초 |
| **시간** | 50분 (강의 25분 + 실습 25분) |
| **선수 지식** | 9차시 (함수 심화) |
| **목표** | 클래스로 현실 세계의 사물과 기능을 모델링하여 객체로 활용할 수 있다 |

---

## 🎯 학습 목표

1. 객체지향 프로그래밍(OOP)의 핵심 개념과 필요성을 이해한다.
2. 클래스(Class)와 객체(Object/Instance)의 관계를 명확히 구분한다.
3. 생성자 `__init__`과 `self`의 역할을 이해하고 인스턴스 속성을 초기화할 수 있다.
4. 클래스 내에 메서드(동작)를 정의하고 호출할 수 있다.
5. 상속(Inheritance)의 기본 개념과 코드 재사용의 이점을 익힌다.

---

## 📖 강의 내용 (25분)

### 1. 클래스와 객체란?

> 💡 **비유**:
> - **클래스(Class)**: **"붕어빵 틀"** 또는 **"자동차 설계도"** 📐 (틀 자체는 먹거나 탈 수 없음)
> - **객체 / 인스턴스(Object / Instance)**: 틀에서 찍어낸 **"실제 붕어빵"** 또는 **"실제 자동차"** 🚗 (직접 조작 가능!)

프로그래밍에서 복잡해지는 데이터(변수)와 동작(함수)을 **하나의 의미 있는 단위로 묶어 관리**하는 도구입니다.

---

### 2. 클래스 기본 구조와 `__init__`, `self`

```python
class Dog:
    # 1) 생성자 (Constructor): 객체가 태어날 때 처음 자동으로 실행되는 특별한 함수
    def __init__(self, name, age):
        # self: "지금 생성되고 있는 바로 그 객체 자신"을 가리키는 이름표
        self.name = name  # 인스턴스 변수 (속성)
        self.age = age

    # 2) 메서드 (Method): 클래스 안에 들어있는 함수 (객체의 행동)
    def bark(self):
        print(f"{self.name}(이)가 멍멍! 짖습니다.")

# 객체 생성 (틀에서 찍어내기)
my_dog = Dog("초코", 3)
your_dog = Dog("보리", 2)

print(my_dog.name)   # "초코"
my_dog.bark()        # "초코(이)가 멍멍! 짖습니다."

print(your_dog.name) # "보리"
your_dog.bark()      # "보리(이)가 멍멍! 짖습니다."
```

---

### 3. `__str__` 스페셜 메서드

객체를 `print(객체)` 했을 때 `<__main__.Dog object at 0x...>` 대신 사람이 읽기 편한 문자열로 보여주게 만듭니다.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def __str__(self):
        return f"🐕 [반려견] 이름: {self.name}, 견종: {self.breed}"

d = Dog("해피", "말티즈")
print(d)  # 🐕 [반려견] 이름: 해피, 견종: 말티즈
```

---

### 4. 상속 (Inheritance) 기초 — "부모의 능력을 물려받기"

이미 잘 만들어진 부모 클래스의 변수와 메서드를 그대로 물려받고, 필요한 기능만 추가하거나 바꿀 수 있습니다.

```python
# 부모 클래스 (기본 동물)
class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name}(이)가 냠냠 밥을 먹습니다.")

# 자식 클래스 (Dog는 Animal을 상속받음)
class Cat(Animal):
    def meow(self):
        print(f"{self.name}: 야옹~ 🐱")

cat = Cat("나비")
cat.eat()   # 부모에게 물려받은 메서드 사용!
cat.meow()  # 자식 고유의 메서드 사용!
```

---

## 💻 실습 예제 (25분)

### [예제 10-1] 간단한 계산기 클래스
- **실생활 시나리오**: 여러 사람이 각자의 계산기 화면을 독립적으로 사용하는 상황

```python
class Calculator:
    def __init__(self, owner):
        self.owner = owner
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def reset(self):
        self.result = 0

# 철수 계산기와 영희 계산기는 서로의 결과에 전혀 영향을 주지 않음!
cal1 = Calculator("철수")
cal2 = Calculator("영희")

cal1.add(10)
cal1.add(5)
print(f"{cal1.owner}의 계산기: {cal1.result}")  # 15

cal2.add(100)
print(f"{cal2.owner}의 계산기: {cal2.result}")  # 100
```

---

### [예제 10-2] 은행 계좌 클래스 (입금·출금·잔액 확인)
- **실생활 시나리오**: 계좌 개설, 입금, 출금 한도 검사

```python
class BankAccount:
    def __init__(self, account_no, owner, initial_balance=0):
        self.account_no = account_no
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("⚠️ 0원 이하의 금액은 입금할 수 없습니다.")
            return
        self.balance += amount
        print(f"💰 [{self.owner}] +{amount:,}원 입금 완료 (현재 잔액: {self.balance:,}원)")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"❌ 잔액 부족! (현재 잔액: {self.balance:,}원, 출금 시도: {amount:,}원)")
            return False
        self.balance -= amount
        print(f"💸 [{self.owner}] -{amount:,}원 출금 완료 (현재 잔액: {self.balance:,}원)")
        return True

acc = BankAccount("110-123-456789", "김파이", 10000)
acc.deposit(30000)
acc.withdraw(50000)  # 잔액 부족
acc.withdraw(15000)  # 성공
```

---

### [예제 10-3] 학생 성적 관리 클래스 (`__str__` 활용)
- **실생활 시나리오**: 학생의 국/영/수 점수를 묶어 평균과 총점을 산출

```python
class Student:
    def __init__(self, student_id, name, kor, eng, math):
        self.student_id = student_id
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def get_average(self):
        return (self.kor + self.eng + self.math) / 3

    def __str__(self):
        avg = self.get_average()
        return f"🎓 [{self.student_id}] {self.name} | 평균: {avg:.1f}점"

s1 = Student("202601", "이영희", 95, 88, 92)
s2 = Student("202602", "박민수", 78, 82, 80)

print(s1)
print(s2)
```

---

### [예제 10-4] 쇼핑 카트와 상품 클래스 (객체 간의 상호작용)
- **실생활 시나리오**: `Product` 객체들을 `ShoppingCart` 객체에 담아 총액 계산

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, qty=1):
        self.items.append({"product": product, "qty": qty})
        print(f"🛒 장바구니 담김: {product.name} x {qty}개")

    def get_total_price(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["qty"]
        return total

    def print_cart(self):
        print("\n--- 🛍️ 장바구니 내역 ---")
        for item in self.items:
            p = item["product"]
            q = item["qty"]
            print(f"- {p.name} ({p.price:,}원) x {q}개 = {p.price * q:,}원")
        print(f"💳 총 결제 예정액: {self.get_total_price():,}원")
        print("-----------------------")

# 사용
p1 = Product("무선 키보드", 45000)
p2 = Product("게이밍 마우스", 32000)

cart = ShoppingCart()
cart.add_product(p1, 1)
cart.add_product(p2, 2)
cart.print_cart()
```

---

### [예제 10-5] 상속 실전: 일반 직원 vs 관리자(매니저)
- **실생활 시나리오**: 일반 직원 기본급 + 매니저 보너스 수당

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_total_pay(self):
        return self.base_salary

    def print_info(self):
        print(f"👤 직원: {self.name} | 급여: {self.get_total_pay():,}원")

class Manager(Employee):
    def __init__(self, name, base_salary, team_bonus):
        super().__init__(name, base_salary)  # 부모의 __init__ 호출
        self.team_bonus = team_bonus

    def get_total_pay(self):
        # 메서드 오버라이딩(덮어쓰기): 기본급 + 팀 보너스
        return self.base_salary + self.team_bonus

staff = Employee("김사원", 3000000)
mgr = Manager("이팀장", 4500000, 1000000)

staff.print_info()
mgr.print_info()
```

---

## 🏆 도전 과제: 계좌 이체 시스템

`BankAccount` 클래스에 다른 계좌로 돈을 송금하는 `transfer` 메서드를 추가하세요.
- 매개변수: `target_account`, `amount`
- 내 잔액이 충분할 때만 내 계좌에서 출금되고 대상 계좌에 입금되어야 합니다.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        """상대방 계좌로 송금"""
        if self.withdraw(amount):
            target_account.deposit(amount)
            print(f"💸 [송금 성공] {self.owner} → {target_account.owner}: {amount:,}원")
            print(f"   내 잔액: {self.balance:,}원 | 상대 잔액: {target_account.balance:,}원")
        else:
            print(f"❌ [송금 실패] {self.owner}님의 잔액이 부족합니다. (현재: {self.balance:,}원)")

# 테스트
acc_a = BankAccount("홍길동", 50000)
acc_b = BankAccount("김철수", 10000)

acc_a.transfer(acc_b, 30000)  # 성공
acc_a.transfer(acc_b, 50000)  # 잔액 부족 실패
```

---

## 📝 핵심 요약 정리

1. **클래스(Class)**: 데이터(속성)와 기능(메서드)을 정의한 틀.
2. **인스턴스(Instance)**: 클래스로부터 생성된 실제 객체.
3. **`__init__(self, ...)`**: 객체 생성 시 최초 자동 호출되는 생성자 함수.
4. **`self`**: 현재 메서드를 호출한 바로 그 인스턴스 자신을 가리키는 첫 번째 매개변수.
5. **상속(Inheritance)**: 부모 클래스의 기능을 자식이 물려받아 확장(`super()`)하거나 재정의(오버라이딩).
