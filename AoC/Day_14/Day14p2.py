with open('.\Day_14\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

res = {}

def calc(index,mask):
    binV = ''
    index = bin(index).replace('0b','')
    for i in range(36-len(index)):
        binV = binV + '0'
    index = binV + index
    result = '' 
    for i in range(36):
        if mask[i] == 'X':
            result = result + 'X'
        elif mask[i] == '1':
            result = result + '1'
        else:
            result = result + index[i]
    return result

def asin(result,value):
    if 'X' in result:
        temp = result.replace('X','0',1)
        asin(temp,value)
        temp = result.replace('X','1',1)
        asin(temp,value)
    else:
        res[result] = value

for data in arr:
    if 'mask' in data:
        mask = data.split(' = ')[1]
    elif 'mem' in data:
        asin(calc(int(data.split('[')[1].split(']')[0]),mask),int(data.split(' = ')[1]))

ans = 0

for key in res:
    ans = ans + res[key]

print(ans)