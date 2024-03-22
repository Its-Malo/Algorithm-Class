list = [7,2,89,15,47,89]

def quicksort(a):

    if len(a) <= 1:
        return a
    
    pivot = a[len(a) // 2]
    left = []
    right = []
    middle = []

    for i in a:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        elif i == pivot:
            middle.append(i)
            
    return quicksort(left) + middle + quicksort(right)

print(quicksort(list))