def quick_sort(nd):
    less,greater = [],[]
    mid = len(nd) // 2
    mid_num = nd.pop(mid)
    for i in nd:
        if i < mid_num:
            less.append(i)
            less = quick_sort(less)
        elif i > mid_num:
            greater.append(i)
            greater = quick_sort(greater)
        elif i == mid_num:
            less.append(mid_num)
    list = less + [mid_num] + greater
    return list

nd = [99,2,33,54,54,33,55,78]
print(quick_sort(nd))
