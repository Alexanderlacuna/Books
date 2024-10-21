# binary search 1 search divide half  check high low new high new low
def binary_search(arri, target):
    low = 0
    high = len(arri)-1
    while low <= high:
        mid = (high + low) // 2

        if arri[mid] < target:
            low = mid + 1

        elif arri[mid] > target:
            high = mid-1
        else:
            return mid

    return False


def binary_search2(arri, target):
    low = 0
    high = len(arri) - 1
    while low <= high:
        mid = (low + high)//2
        if arri[mid] < target:
            low = mid + 1
        elif arri[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


def binary_search_recursion(arri, target, low, high):
    mid = (low+high)//2

    if low > high:
        return -1
    if arri[mid] == target:
        return mid

    elif arri[mid] > target:
        return binary_search_recursion(arri, target, low, mid-1)
    else:
        return binary_search_recursion(arri, target, mid+1, high)

"""

Notes what is a binary search : it is  algorithms that  employs the techique for dividing the items
by half until a solution is found which is a target or no element
Alogrithms analysis search worst case: O(log n) since  we divide the items 2 every time
for example 8  maximum iteration 3 since 2** 3 = 8
space complexity: O(1) no space required:
1. iteration method find the mid  (low+high)//2  while low<=high: else outer return -1 (meaning no items are found),
if arri[mid] > target high = mid-1
elif arri[mid] < target low = mid+1
else: return arri[mid]

2. recursion: Note dont forget the return for value binary_search(arri, target, low), high):
"""

def binary_recursion(arri, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    if arri[mid] == target:
        return mid
    elif arri[mid] > target:
        return binary_recursion(arri, target, low, mid-1)
    else:
        return binary_recursion(arri, target, mid+1, high)


arri = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
print(binary_search_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9],
                              15,  0, len(arri)-1))


"""
ALgorithms analysis : we need to analyse the space and time complexity
can be expressed  in form  of best case, worst case,  and average acse
symptotic notation: way of expressing the cost of algorithm omega , little and Big 0

"""
