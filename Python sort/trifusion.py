liste = [59,17,2,11,6,9]

def trifusion(a):

    if len(a) <= 1:
        return a

    mid = len(a) // 2

    left_half = a[:mid]
    right_half = a[mid:]

    trifusion(left_half)
    trifusion(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[i]:
            a[k] = left_half[i]
            i = i+1
        else:
            a[k] = right_half[j]
            j = j+1
        k = k+1
    
    while i < len(left_half):
        a[k] = left_half[i]
        i = i+1
        k = k+1

    while j < len(right_half):
        a[k] = right_half[j]
        j = j+1
        k = k+1

print(trifusion(liste))