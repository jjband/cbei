
ll = []
rl = []

n,m = map(int, input().split())
#n개의 줄에 m개의 ㅣ원소

for _ in range(n):
    t = list(map(int, input().split()))
    ll.append(t)

for l in ll:
    r = list(map(int, input().split()))
    for i in zip(l,r):
        print(sum(i), end=" ")
    print()