arr = [] 

txtfile = open("day_1.txt", "r")
arr = txtfile.readlines()

arr = [int(i.split('\n')[0]) for i in arr]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if (arr[i] + arr[j] + arr[k] == 2020):
                ans = arr[i]*arr[j]*arr[k]

print(ans)