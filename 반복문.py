# 구구단 3단 출력
i = int(input("숫자를 입력하세요:"))
count = 0
while count < 9:
    count = count + 1
    r = i * count
    print(i, "X",count ,"=", r)

# for index in range(1,10):
#     number = 3*index
#     print("3 x", index,"=", number)
