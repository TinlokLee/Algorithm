num = int(input('Please enter a number:')) 
if num < 0 :
    print('-1')
low = 0
hight = num 
mid = (low+hight)/2.0
sign = mid 
while mid**2 != num:
    if mid**2 >num:
        hight=mid
    else:
        low = mid 
    mid = (low+hight)/2.0
    if sign == mid:
        break
print(mid)

# def binary_search(alist, item):
#     n = len(alist)
#     start = 0
#     end = n-1
#     while start <= end:
#         mid = (start + end) // 2
#         if item == alist[mid]:
#             return True
#         elif item < alist[mid]:
#             end = mid - 1
#         elif item > alist[mid]:
#             start = mid + 1
#     return False

# def binary_search2(alist, item):
#     n = len(alist)
#     if n == 0:
#         return False
#     mid = n // 2
#     if item == alist[mid]:
#         return True
#     elif item < alist[mid]:
#         return binary_search2(alist[:mid], item)
#     else:
#         return binary_search2(alist[mid+1:], item)


# if __name__ == '__mian__':
#     l1 = [22,23,44,64,77,43,76,444,25,54]
#     print(binary_search2(l1,22))