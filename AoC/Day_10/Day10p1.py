File = open('.\Day_10\Input.txt','r')

arr = File.readlines()

arr = [int(s.replace('\n','')) for s in arr]

arr.sort()

ans = {1:1, 2:1, 3:1}

for i in range(len(arr)-1):
    diff = arr[i+1] - arr[i]
    ans[diff] = ans[diff] + 1

print(ans[3]*ans[1])

File.close()