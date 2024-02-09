# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

N = int(input())
columns = namedtuple('student', input())
marks_sum = 0

for n in range(N):
    marks_sum += int(columns(*input().split()).MARKS)

print(marks_sum / N)
