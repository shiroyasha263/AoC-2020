File = open('.\Day_6\Input.txt','r')

arr = File.read()

data = arr.split('\n\n')

data = [s.replace('\n',' ') for s in data]

data = [s.split(' ') for s in data]

ans = 0

for lis in data:
    for ch in lis[0]:
        flag = 0
        for st in lis:
            if ch not in st:
                flag = 1
        if flag == 0:
            ans = ans + 1

print(ans)

File.close()