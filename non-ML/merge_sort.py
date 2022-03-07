def merging(left, right):
    new_list = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            new_list.append(right.pop(0))
        else:
            new_list.append(left.pop(0))
    if len(left) > 0:
        for i in left:
            new_list.append(i)
    if len(right) > 0:
        for i in right:
            new_list.append(i)
    return new_list


def merge_sort(some_list):
    sorted_list = []
    if len(some_list) == 1:
        sorted_list = some_list
    else:
        left = merge_sort(some_list[: (len(some_list) // 2)])
        right = merge_sort(some_list[(len(some_list) // 2) :])
        sorted_list = merging(left, right)
    return sorted_list


bing = [4, 1, 3, 2, 6, 3, 18, 2, 9, 7, 3, 1, 2.5, -9]
bong = merge_sort(bing)
print(bong)
