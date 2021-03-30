File = open(".\Day_7\Input.txt",'r')

arr = File.readlines()

data = [s.replace('\n',' ') for s in arr]

data = [s.split('contain') for s in arr]

cont = ['shiny gold bag']


def check(cont):
    flag = 0
    for lis in data:
        for sec in cont:
            if sec in lis[1] and lis[0][:-2] not in cont:
                cont.append(lis[0][:-2])
                flag = flag + 1
    if flag == 0:
        return cont
    else:
        check(cont)

check(cont)

print(len(cont)-1)

File.close()