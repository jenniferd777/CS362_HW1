arr = [[1,2,3,4,5,6], [2,3,5,10,8,12]]
max = 0
temp = 0
sum = 0
n = 10
j = 5
k = 5

while i >= 0:
    while j <= 6:
        if max < temp:
            max = temp
        temp = 0

        while k <= j:
            if sum + arr[0][i-k] <= n:
                sum = sum + arr[0][i-k]
                dens = arr[1][i-k]
                temp = temp + dens
            if sum == n:
                k = j
            else:
                k = k + 1

