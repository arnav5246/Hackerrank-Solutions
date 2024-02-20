n = int(input())
arr = []
for i in range(n):
    arr.append(input())
    
Dict = {}

for i in range(0,len(arr)):
    if(arr[i] in Dict ):
        Dict[arr[i]] += 1
    else:
        Dict[arr[i]] = 1
                
        
print(len(Dict.keys()))
print(*(Dict.values()), sep=" ") 