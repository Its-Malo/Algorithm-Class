list = [50,84,28,73,18,22]

for i in range(len(list)):
    value = i
    
    for j in range(i+1 ,len(list)):
        if list[value] >= list[j]:
            value = j
    
    list[i], list[value] = list[value], list[i]

print(list)