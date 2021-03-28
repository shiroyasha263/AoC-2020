File = open('.\Day_2\Input.txt', 'r')

arr = File.readlines()

arr = [s.split('\n')[0] for s in arr]

chck = 0

for x in arr:
    lower = int(x.split('-',1)[0])
    upper = int(x.split('-',1)[1].split(' ',1)[0])
    char = x.split(' ')[1].split(':')[0]
    code = x.split(': ')[1]
    flag = 0
    for ch in code:
        if(ch == char):
            flag = flag + 1
    if flag <= upper and flag >= lower:
        chck = chck + 1

print(chck)

File.close()