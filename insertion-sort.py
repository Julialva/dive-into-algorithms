def insert_loc(some_list: list, to_insert: int) -> list:
    check_location = len(some_list) - 1
    insert_location = 0
    while check_location >= 0:
        if to_insert > some_list[check_location]:
            insert_location = check_location + 1
            check_location = 0
        check_location = check_location - 1
    some_list.insert(insert_location, to_insert)
    return some_list


def insertion_sort(some_list: list) -> list:
    new_list = []
    while len(some_list) > 0:
        to_insert = some_list.pop(0)
        new_list = insert_loc(new_list, to_insert)
    return new_list


s = [0, 10, 2, 3, 4, 6666, 6, 1, 2, 3, 4, 7, 7, 7, 7, 8, 12]
print(insertion_sort(s))
