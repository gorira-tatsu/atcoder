a_and_b = [int(x) for x in input().split()]
a = a_and_b[0]
b = a_and_b[1]

if (a*b) % 2 == 0:
    print('Even')
else:
    print('Odd')
