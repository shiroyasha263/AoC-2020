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
    if 'byr' in dic and (int(dic['byr']) >= 1920 and int(dic['byr']) <= 2002):
        flag = flag + 1
    if 'iyr' in dic and (int(dic['iyr']) >= 2010 and int(dic['iyr']) <= 2020):
        flag = flag + 1
    if 'eyr' in dic and (int(dic['eyr']) >= 2020 and int(dic['eyr']) <= 2030):
        flag = flag + 1
    if 'hgt' in dic:
        if dic['hgt'][-1] == 'n' and (int(dic['hgt'].split('i')[0]) >= 59 and int(dic['hgt'].split('i')[0]) <= 73):
            flag = flag + 1
        elif dic['hgt'][-1] == 'm' and (int(dic['hgt'].split('c')[0]) >= 150 and int(dic['hgt'].split('c')[0]) <= 193):
            flag = flag + 1
    if 'hcl' in dic and len(dic['hcl'][1:]) == 6 and dic['hcl'][1:].isalnum():
        flag = flag + 1
    if 'ecl' in dic and (dic['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']):
        flag = flag + 1
    if 'pid' in dic and (len(dic['pid']) == 9) and dic['pid'].isdecimal():
        flag = flag + 1
    if flag == 8:
        ans = ans + 1


print(ans)