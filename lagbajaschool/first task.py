def extract_and_index(tuple2):
    list_values = tuple2[1]
    tuple_values = tuple2[2]
    targets = [20, 25]
    result = []

    for target in targets:
        if target in list_values:
            result.append((list_values.index(target), target))
        elif target in tuple_values:
            result.append((tuple_values.index(target), target))

    return tuple(result)


tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
print(extract_and_index(tuple2))