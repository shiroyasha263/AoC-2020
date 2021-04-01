with open('.\Day_13\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

timeS = int(arr[0])

BusId = []

for s in arr[1].split(','):
    if s != 'x':
        BusId.append(int(s))

def calc():
    for i in range(timeS, timeS + max(BusId) + 1):
        for x in BusId:
            if i%x == 0:
                return (i-timeS)*x

print(calc())