import random

x = int(input("Podaj ilosc losowych liczb: "))

numbers = []
for i in range(x):
    numbers.append(random.randrange(101))
print(" ")
print(f"Przed sortem: {numbers}")

for i in range(x - 1):
    for j in range(x - i - 1):
        if(numbers[j] > numbers[j + 1]):
            temp = numbers[j + 1]
            numbers[j + 1] = numbers[j]
            numbers[j] = temp

print(f"Po sorcie: {numbers}")
print(" ")
