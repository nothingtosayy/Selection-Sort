def SelectionSort(sequence):
    for i in range(len(sequence)):
        min_index = i
        for j in range(i+1, len(sequence)):
            if sequence[min_index] > sequence[j]:
                min_index = j
            else:
                min_index = min_index
        sequence[min_index], sequence[i] = sequence[i], sequence[min_index]
        
    return sequence
    
print(SelectionSort(sequence=[5,2,3,4,6,1,3,2,6,5,4,7,6,9,8,8,3,9]))
