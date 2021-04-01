with open('.\Day_12\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

print(arr)

dic = {'V':0,'H':0,'F':1}

direc = {0:'N',1:'E',2:'S',3:'W'}

def mov(com):
    if com[0] == 'N':
        dic['V'] = dic['V'] + int(com[1:])
    elif com[0] == 'E':
        dic['H'] = dic['H'] + int(com[1:])
    elif com[0] == 'W':
        dic['H'] = dic['H'] - int(com[1:])
    elif com[0] == 'S':
        dic['V'] = dic['V'] - int(com[1:])
    elif com[0] == 'F':
        mov(direc[dic[com[0]]]+com[1:])
    elif com[0] == 'R':
        dic['F'] = int((dic['F'] + int(com[1:])/90)%4)
    elif com[0] == 'L':
        dic['F'] = int((dic['F'] - int(com[1:])/90)%4)

for com in arr:
    mov(com)

print(abs(dic['V']) + abs(dic['H']))