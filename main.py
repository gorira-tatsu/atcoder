n = int(input())
a = [int(i) for i in input().split()]
possible_count = 0

while True:
    ok = True
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
        else:
            ok = False
            break
    if not ok:
        break
    possible_count = possible_count + 1
print(possible_count)
