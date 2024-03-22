def bubbleSort(a):
    n= len(a)

    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        
        if (swapped == False):
            break

a = [15,9,24,71,2,12]

bubbleSort(a)

print("sorted array :")

for i in range(len(a)):
    print(a[i], end= " ")