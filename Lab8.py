Завдання 1

alpha = input("Insert your message: ")

omega = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
delta = [char for char in alpha if char in omega]

print("Filtered elements:", delta)
print("Counted units:", len(delta))


Завдання 2

r1 = [int(i) for i in input("Feed list alpha: ").split()]
r2 = [int(j) for j in input("Feed list beta: ").split()]

x = r1 + r2
y = sorted(set(x))

print("Final merged view:", y)


Завдання 3

raw = input("Type your full entry: ")

bucket = {}

for symbol in raw:
    if symbol not in bucket:
        bucket[symbol] = 1
    else:
        bucket[symbol] += 1

print("Multihit elements:")
for key, value in bucket.items():
    if value > 1:
        print(f"'{key}': {value}")

solo = {char for char, freq in bucket.items() if freq == 1}
print("One-timers:", solo)
