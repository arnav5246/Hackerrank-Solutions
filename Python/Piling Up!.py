# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n = int(input())
    cubes = list(map(int, input().split()))
    last = 10**10
    
    for i in range(n):
        if cubes[0] > cubes[-1]:
            if cubes[0] > last:
                print('No')
                break
            last = cubes[0]
            del cubes[0]
        else:
            if cubes[-1] > last:
                print('No')
                break
            last = cubes[-1]
            del cubes[-1]
        if len(cubes) == 0:
            print('Yes')
