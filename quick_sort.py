def quickSort(li):
    arr = []
    low = 0
    high = len(li) - 1
    if low < high:
        mid = partition(li, low, high)
        if low < mid - 1:
            arr.append(low)
            arr.append(mid - 1)
        if mid + 1 < high:
            arr.append(mid + 1)
            arr.append(high)
        while arr:
            r = arr.pop()
            l = arr.pop()
            mid = partition(li, l, r)
            if l < mid - 1:
                arr.append(l)
                arr.append(mid - 1)
            if mid + 1 < r:
                arr.append(mid + 1)
                arr.append(r)
    return li

a = quickSort([3,1,6,4,9,5,7,8])
print(a)