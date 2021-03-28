File = open('.\Day_3\Input.txt', 'r')

arr = File.readlines()

arr = [s.split('\n')[0] for s in arr]

flag = [0,0,0,0,0]
disx = [1,3,5,7,1]
disy = [1,1,1,1,2]

i = 0
while(i < len(flag)):
    x = 0
    y = 0
    while(y < len(arr)):
        if arr[y][x] == '#':
            flag[i] = flag[i] + 1
        x = (x + disx[i])%len(arr[0])
        y = y + disy[i]
    i = i + 1

ans = 1

for k in flag:
    ans = ans*k

print(ans)

File.close()