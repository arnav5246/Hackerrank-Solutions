# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

string, k = input().split()
k = int(k)

string = list(string)
string.sort()

string_list = []
for i in range(1, k+1):
    string_list.extend(combinations(string, i))

for i in string_list:
    print("".join(list(i)))
