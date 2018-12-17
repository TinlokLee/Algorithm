# 冒泡排序

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
    冒泡排序：
    重复遍历待排序列，一次比较两个相邻元素（A-Z0-9）按升序排，直到没有需要交换的元素
    时间复制度 O（n）
'''

#  选择排序
def selection_sort(nd):
    n = len(nd)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if nd[j] < nd[min_index]:
                min_index = j
    if min_index != i:
        nd[i], nd[min_index] = nd[min_index], nd[i]

'''
    选择排序：
    待排序列取最大（小）元素，放在序列起始位置，再从序列中选最值，放末尾，依此类推
    数据移动排序
    时间复制度O（n2）
'''

#　插入排序
def insert_sort(nd):
    for i in range(1, len(nd)):
        for j in range(i, 0, -1):
            if nd[j] < nd[j-1]:
                nd[j], nd[j-1] = nd[j-1], nd[j]

'''
    插入排序：
    有序序列，从后向前扫描，找到相应位置并插入
    时间复制度O(n)
'''

# 快速排序
def quick_sort(nd):
    if len(nd) == 0: return
        tem = nd[0]
        for i in range(len(nd)-1):
            less = quick_sort([i for i in nd[1:] if tem < i])
            gerter = quick_sort([i for i in nd[1:] if tem > i])
    return less + [tem] + gerter
    

