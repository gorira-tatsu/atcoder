import sys

n_and_y = input()
n = int(n_and_y.split()[0])
y = int(n_and_y.split()[1])
money_list = []
# 10000yen 0, 5000yen 1, 1000 2

for i in range(n+1):
    for j in range(n+1):
        k = n - (i+j)
        if y == i*10000 + j*5000 + k*1000 and k>=0:
            money_list = [i, j, k]
            for l in range(3):
                print(money_list[l], end=' ')
            sys.exit()
        else:
            money_list = "-1 -1 -1"

print(money_list)