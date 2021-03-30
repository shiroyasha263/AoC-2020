File = open('.\Day_8\Input.txt','r')

arr = File.readlines()

arr = [s.replace('\n','') for s in arr]

for j in range(len(arr)):
    dic = {}

    for k in range(len(arr)):
        dic[k] = True
    
    
    if arr[j].split(' ')[0] == 'nop':
        arr[j] = arr[j].replace('nop','jmp')
    elif arr[j].split(' ')[0] == 'jmp':
        arr[j] = arr[j].replace('jmp','nop')
    i = 0
    acc = 0
    while i < (len(arr)) and i >= 0:
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
            i = -1
    if i >= len(arr):
        break;
    else:
        if arr[j].split(' ')[0] == 'nop':
            arr[j] = arr[j].replace('nop','jmp')
        elif arr[j].split(' ')[0] == 'jmp':
            arr[j] = arr[j].replace('jmp','nop')

print(acc)

File.close()