__auth__ = 'lee'

''' 时间复杂度为 O(n)的 top2 方法'''
print('===============================================')
def find_sec_num(arr):
    max = arr[0]
    sec_num = 0
    for i in range(len(arr)):
        if arr[i] > max:
            sec_num = max
            max = arr[i]
        elif arr[i] > sec_num and arr[i] < max:
            sec_num = arr[i]
    return sec_num
arr = [66,11,44,13,42,5555,1131,53,21]
print(find_sec_num(arr))
def foo(nd):
    max = nd[0]
    sec = 0
    for i in range(len(nd)):
        if nd[i] > max:
            sec = max
            max = nd[i]
        elif nd[i] < max and nd[i] > sec:
            sec = nd[i] 
    return sec
arr = [66,11,44,13,42,5555,11,53,21]
print(foo(arr))
