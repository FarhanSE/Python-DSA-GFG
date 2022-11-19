def getMinMax(a, n):
    min = a[0]
    max = a[0]

    if n > 1:
        for i in range(1, n):
            if a[i] > max:
                max = a[i]
            elif a[i] < min:
                min = a[i]

    return max, min


result = getMinMax([12,3,5,7,5,6,1,10],8)
print(result)