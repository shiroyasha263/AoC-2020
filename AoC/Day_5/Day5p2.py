File = open(".\Day_5\Input.txt",'r')

arr = File.readlines()

maxi = 0

seatId = []

for seat in arr:
    lowv = 0
    highv = 127
    lowh = 0
    highh = 7
    for i in range(7):
        if(seat[i] == 'F'):
            highv = (highv + lowv)//2
        elif(seat[i] == 'B'):
            lowv = (highv + lowv)//2 + 1
    for i in range(3):
        if(seat[i+7] == 'R'):
            lowh = (lowh + highh)//2 + 1
        elif(seat[i+7] == 'L'):
            highh = (lowh + highh)//2
    seatId.append(highv*8 + highh)

for i in range(87,850):
    if i not in seatId:
        ans = i

print(ans)