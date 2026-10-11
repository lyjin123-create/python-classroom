# [예제 6-1] 비교·논리 연산자 연습

# === 비교 연산자 ===
x, y = 10, 20

print(f"x={x}, y={y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= 10: {x >= 10}")
print(f"x <= 5: {x <= 5}")

print(f"\n'apple' == 'apple': {'apple' == 'apple'}")
print(f"'Apple' == 'apple': {'Apple' == 'apple'}")

# === 논리 연산자 ===
age = 25
has_id = True

print(f"\nage={age}, has_id={has_id}")
print(f"age >= 19 and has_id: {age >= 19 and has_id}")
print(f"age >= 19 or has_id: {age >= 19 or has_id}")
print(f"not has_id: {not has_id}")

score = 85
print(f"\nscore={score}")
print(f"80 <= score < 90: {80 <= score < 90}")
