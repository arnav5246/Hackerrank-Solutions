# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for _ in range(n):
    num1, num2 = input().split()
    
    try:
        print(int(int(num1) / int(num2)))
    except ZeroDivisionError as e:
        print(f"Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")
