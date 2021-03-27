arr = [] 

txtfile = open("Day_1.txt", "r")
arr = txtfile.readlines()

arr = [int(i.split('\n')[0]) for i in arr]

for x in arr:
    for y in arr:
        for z in arr:
            if (x + y + z == 2020):
                ans = x*y*z

print(ans)