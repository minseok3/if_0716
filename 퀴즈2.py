
num_list = [[100,200],[400,800],[1000,1400]]

for i in num_list:
    sum = 0
    for e in i:
        sum = sum + e
        average = sum/len(i)
    print(average)