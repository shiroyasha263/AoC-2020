with open('.\Day_13\Input.txt','r') as File:
    arr = [s.replace('\n','') for s in File.readlines()]

timeS = int(arr[0])

BusId = []

offset = {}

t = 0

for s in arr[1].split(','):
    if s != 'x':
        BusId.append(int(s))
        offset[int(s)] = t
    t = t + 1

def calc(first,Off,k,ans = 0):
    q = 0
    while True:
        if (first*q + Off)%BusId[k] == 0:
            ans = ans + first*q
            if k+1 < len(BusId):
                return calc(first*BusId[k], ans + offset[BusId[k+1]], k+1,ans)
            else:
                return ans
            break
        q = q + 1

print(calc(BusId[0],offset[BusId[1]],1))