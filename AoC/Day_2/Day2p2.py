File = open('.\Day_2\Input.txt', 'r')

arr = File.readlines()

arr = [s.split('\n')[0] for s in arr]

flag = 0

for x in arr:
    indxL = int(x.split('-',1)[0])
    indxU = int(x.split('-',1)[1].split(' ',1)[0])
    char = x.split(' ')[1].split(':')[0]
    code = x.split(': ')[1]
    if (char != code[indxL-1] and char == code[indxU-1]) or (char == code[indxL-1] and char != code[indxU-1]):
        flag = flag + 1

print(flag)

File.close()