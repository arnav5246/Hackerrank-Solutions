n = int(input())
s = set(map(int, input().split()))
ncomms = int(input())
commlist = []
for i in range(ncomms):
    nestlist = input().split()
    commlist.append(nestlist)
for i in commlist:
    if i[0] == 'pop':
        s.pop()
    elif i[0] == 'discard':
        s.discard(int(i[1]))
    elif i[0] == 'remove':
        s.remove(int(i[1]))
print(sum(s))