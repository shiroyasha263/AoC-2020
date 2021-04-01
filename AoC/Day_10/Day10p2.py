with open('.\Day_10\InputP.txt','r') as File:
  arr = [int(i) for i in File.readlines()]
arr.append(0)
arr.sort()

lis = {}

lis[arr[-1]] = 1

def ret(i):
    if i in lis:
        return lis[i]
    else:
        return 0

i = len(arr)-2

while i >= 0:
    lis[arr[i]] = ret(arr[i]+1) + ret(arr[i]+2) + ret(arr[i]+3)
    i = i - 1

print(lis[0])