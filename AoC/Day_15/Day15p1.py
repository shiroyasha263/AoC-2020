with open('.\Day_15\Input.txt','r') as File:
    arr = File.read().split(',')

arr = [int(s) for s in arr]

dic = {}

def init(no, pos):
    if no in dic:
        dic[no][1] = dic[no][0]
        dic[no][0] = pos
    else:
        dic[no] = [pos,0]

for i in range(len(arr)):
    init(arr[i],i+1)

temp = arr[len(arr)-1]

for i in range(len(arr),2020):
    if dic[temp][1] == 0:
        temp = 0
        init(temp,i+1)
    else:
        temp = (dic[temp][0] - dic[temp][1])
        init(temp,i+1)

print(temp)