arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    ]

for i in range(1, len(arr)):
    for j in range (0, len(arr[i])):
        b = arr[0][j] + arr[i][j]
        print(b)

        # print(arr[0][0] + arr[0][1] + arr[0][2] + arr[0][3] + arr[0][4])
        # print(arr[1][0] + arr[1][1] + arr[1][2] + arr[1][3] + arr[1][4])