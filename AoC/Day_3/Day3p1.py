File = open('.\Day_3\Input.txt', 'r')

arr = File.readlines()

arr = [s.split('\n')[0] for s in arr]

x = 0
flag = 0
for y in arr:
    if y[x] == '#':
        flag = flag + 1
    x = (x + 3)%len(y)

print(flag)

File.close()