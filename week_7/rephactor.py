def highest_values(arr, n):
    result = []
    
    for i in range(n):
        highest = 0
        highest_idx = -1
        for k in range(len(arr)):
            if arr[k] > highest:
                highest = arr[k]
                highest_idx = k
        result.insert(0, highest)
        arr.pop(highest_idx)
    return result

arr = [83, 35, 61, 12, 29]

print(highest_values(arr, 5))