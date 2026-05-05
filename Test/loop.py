arr = [1,2,3,4,90]

max = 0
for i in range(0, len(arr)):
    if arr[i] >= max:
        max = arr[i]
print(max)