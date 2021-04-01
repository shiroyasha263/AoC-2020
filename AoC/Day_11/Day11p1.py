with open('.\Day_11\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

lenx = len(arr[0])
leny = len(arr)

def check(i,j):
    check = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if(i + x >= 0 and i + x < leny)and (j + y >= 0 and j + y < lenx) and (not(x == 0 and y == 0)):
                if arr[i+x][j+y] == '#':
                    check = check + 1
    return check

def roun(arr):
    new = []
    for i in range(leny):
        new.append('')
        for j in range(lenx):
            count = check(i,j)
            if arr[i][j] == 'L':
                if count == 0:
                    new[i] = new[i] + '#'
                else:
                    new[i] = new[i] + 'L'
            elif arr[i][j] == '#':
                if count >= 4:
                    new[i] = new[i] + 'L'
                else:
                    new[i] = new[i] + '#'
            else:
                new[i] = new[i] + '.'
    return new

i = 1

while i:
    temp = roun(arr)
    if arr == temp:
        i = 0
    else:
        arr = temp

flag = 0

for s in arr:
    for ch in s:
        if ch == '#':
            flag = flag + 1

print(flag)