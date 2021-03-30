File = open('.\Day_8\Input.txt','r')

arr = File.readlines()

arr = [s.replace('\n','') for s in arr]

i = 0
acc = 0

dic = {}

for j in range(len(arr)):
    dic[j] = True

while i < (len(arr)):
    if dic[i]:
        dic[i] = False
        if arr[i].split(' ')[0] == 'nop':
            i = i + 1
            continue
        if arr[i].split(' ')[0] == 'jmp':
            i = i + int(arr[i].split(' ')[1])
            continue
        if arr[i].split(' ')[0] == 'acc':
            acc = acc + int(arr[i].split(' ')[1])
            i = i + 1
            continue
    else:
        break

print(acc)

File.close()