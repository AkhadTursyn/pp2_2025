def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_list([1, 2, 3, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
