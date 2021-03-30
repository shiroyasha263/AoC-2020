File = open(".\Day_7\Input.txt",'r')

arr = File.readlines()

data = [s.replace('\n',' ') for s in arr]

data = [s.split('contain') for s in arr]

dic = {}

for lis in data:
    key , value = lis[0],lis[1]
    dic[key] = value

def get(dic , check):
    ans = 0
    check = check + ' bags '
    for ch in dic[check].split(','):
        if ch.split(' ')[1].isdigit():
            ans = ans + int(ch.split(' ')[1]) + int(ch.split(' ')[1])*get(dic,ch.split(' ')[2] + ' ' + ch.split(' ')[3])
    return ans

print(get(dic,'shiny gold'))

File.close()