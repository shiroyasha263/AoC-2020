File = open('.\Day_6\Input.txt','r')

arr = File.read()

data = arr.split('\n\n')

data = [s.replace('\n',' ') for s in data]

ans = 0

for string in data:
    uniq = []
    for ch in string:
        if ch not in uniq and ch != ' ':
            uniq.append(ch)
    ans = ans + len(uniq)

print(ans)

File.close()