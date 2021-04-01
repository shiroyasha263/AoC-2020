with open('.\Day_11\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

lenx = len(arr[0])
leny = len(arr)

def check(i,j):
    check = 0
    for y in range(j+1,lenx):
        if arr[i][y] == '#':
            check = check + 1
            break
        elif arr[i][y] == 'L':
            break

    for y in range(j-1,-1,-1):
        if arr[i][y] == '#':
            check = check + 1
            break
        elif arr[i][y] == 'L':
            break

    for x in range(i+1,leny):
        if arr[x][j] == '#':
            check = check + 1
            break
        elif arr[x][j] == 'L':
            break

    for x in range(i-1,-1,-1):
        if arr[x][j] == '#':
            check = check + 1
            break
        elif arr[x][j] == 'L':
            break

    for x in range(1,min(leny - i,lenx - j)):
        if arr[i+x][j+x] == '#':
            check = check + 1
            break
        elif arr[i+x][j+x] == 'L':
            break

    for x in range(1,min(i+1,j+1)):
        if arr[i-x][j-x] == '#':
            check = check + 1
            break
        elif arr[i-x][j-x] == 'L':
            break

    for x in range(1,min(lenx - j,i+1)):
        if arr[i-x][j+x] == '#':
            check = check + 1
            break
        elif arr[i-x][j+x] == 'L':
            break

    for x in range(1,min(j+1,leny - i)):
        if arr[i+x][j-x] == '#':
            check = check + 1
            break
        elif arr[i+x][j-x] == 'L':
            break

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
                if count >= 5:
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