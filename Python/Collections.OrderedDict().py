# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N = int(input())
items_dict = OrderedDict()

for n in range(N):
    entry = input().split()
    name = ' '.join(entry[:-1])
    price = int(entry[-1])
    
    if name in items_dict:
        items_dict[name] += price
    else:
        items_dict[name] = price

for item in items_dict.items():
    print(*item)
