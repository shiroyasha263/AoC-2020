File = open(".\Day_4\Input.txt",'r')

arr = File.read()

data = arr.split('\n\n')

data = [s.replace('\n',' ') for s in data]

data = [s.split(' ') for s in data]

ans = 0

for pasp in data:
    dic = {}
    flag = 1
    for inf in pasp:
        key,value = inf.split(':')
        dic[key] = value
    if 'byr' in dic:
        flag = flag + 1
    if 'iyr' in dic:
        flag = flag + 1
    if 'eyr' in dic:
        flag = flag + 1
    if 'hgt' in dic:
        flag = flag + 1
    if 'hcl' in dic:
        flag = flag + 1
    if 'ecl' in dic:
        flag = flag + 1
    if 'pid' in dic:
        flag = flag + 1
    if flag == 8:
        ans = ans + 1


print(ans)