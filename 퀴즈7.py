import random
i = 0
result = []
while i < 6:
    i = i + 1
    a = random.randint(1,45)
    if a in result:
        print("중복값")
    else:
        result.append(a)
print(result)