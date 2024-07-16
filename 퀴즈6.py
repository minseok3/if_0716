list1 = []
list2 = []
list3 = []
for i in range(1,101):
    if i%2 == 0:
       list1.append(i)
    if i%3 == 0:
        list2.append(i)
    if i%5 == 0:
        list3.append(i)

print("2의 배수:",list1)
print("3의 배수:",list2)
print("5의 배수:",list3)