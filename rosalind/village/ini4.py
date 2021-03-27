a = 4870
b = 9580
result = 0

for i in range(a, b):
    if not i % 2 == 0:
        result += i

print(result)