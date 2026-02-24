x = int(input("Введите число X: "))
chetnye_count = 0
nechetnye_count = 0

for i in range(1, x + 1):
    if i % 2 == 0:
        chetnye_count += 1
    else:
        nechetnye_count += 1

print(f"Чётных: {chetnye_count}")
print(f"Нечётных: {nechetnye_count}")