m = [[ int(i)for i in input().split()] for i in  range(9)]


ans = m[0][0]
x = 0
y = 0
for h in range(9):
    for w in range(9):
        if ans < m[h][w]:
            ans = m[h][w]
            x = w
            y = h
print(ans)
print(y+1, x+1)