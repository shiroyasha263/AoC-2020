with open('.\Day_14\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

print(arr)

res = {}

def calc(value,mask):
    binV = ''
    value = bin(value).replace('0b','')
    for i in range(36-len(value)):
        binV = binV + '0'
    value = binV + value
    result = '' 
    for i in range(36):
        if mask[i] == 'X':
            result = result + value[i]
        else:
            result = result + mask[i]
    return result

for data in arr:
    if 'mask' in data:
        mask = data.split(' = ')[1]
    elif 'mem' in data:
        res[data.split('[')[1].split(']')[0]] = int(calc(int(data.split(' = ')[1]),mask),2)

ans = 0

for key in res:
    ans = ans + res[key]

print(ans)