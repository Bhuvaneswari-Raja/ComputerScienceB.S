L = [1,2,1,5]

some_num = 0

for i in L:
    for j in L:
        some_num += 2*i+j
        print("Some num =",some_num)

print(some_num)