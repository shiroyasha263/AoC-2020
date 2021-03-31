File = open('.\Day_9\Input.txt','r')

arr = File.readlines()

arr = [int(s.replace('\n','')) for s in arr]

Pl = 25

def sums(ind, Pl, arr):
    lis = []
    for i in range(ind-Pl,ind):
        for j in range(i+1,ind):
            lis.append(int(arr[i]) + int(arr[j]))
    return lis

for i in range(Pl,len(arr)):
    if int(arr[i]) not in sums(i, Pl, arr):
        print(int(arr[i]))

File.close()