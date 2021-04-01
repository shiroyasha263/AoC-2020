with open('.\Day_12\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

print(arr)

wayp = {'V':1,"H":10}

dic = {'V':0,'H':0,'F':1}

direc = {0:'N',1:'E',2:'S',3:'W'}

def mov(com):
    if com[0] == 'N':
        wayp['V'] = wayp['V'] + int(com[1:])
    
    elif com[0] == 'E':
        wayp['H'] = wayp['H'] + int(com[1:])
   
    elif com[0] == 'W':
        wayp['H'] = wayp['H'] - int(com[1:])
    
    elif com[0] == 'S':
        wayp['V'] = wayp['V'] - int(com[1:])
    
    elif com[0] == 'F':
        dic['V'] = dic['V'] + int(com[1:])*wayp['V']
        dic['H'] = dic['H'] + int(com[1:])*wayp['H']
    
    elif com[0] == 'R':
        if int(com[1:]) == 90:
            temp = wayp['H']
            wayp['H'] = wayp['V']
            wayp['V'] = -1*temp
        elif int(com[1:]) == 180:
            wayp['H'] = -1*wayp['H']
            wayp['V'] = -1*wayp['V']
        elif int(com[1:]) == 270:
            temp = wayp['V']
            wayp['V'] = wayp['H']
            wayp['H'] = -1*temp
        
    elif com[0] == 'L':
        if int(com[1:]) == 90:
            temp = wayp['V']
            wayp['V'] = wayp['H']
            wayp['H'] = -1*temp 
        elif int(com[1:]) == 180:
            wayp['H'] = -1*wayp['H']
            wayp['V'] = -1*wayp['V']
        elif int(com[1:]) == 270:
            temp = wayp['H']
            wayp['H'] = wayp['V']
            wayp['V'] = -1*temp

for com in arr:
    mov(com)

print(abs(dic['V']) + abs(dic['H']))