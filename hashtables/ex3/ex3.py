def intersection(arrays):
    cache = {}

    for i in range(len(arrays)):
        for x in arrays[i]:
            if x not in cache:
                cache[x] = 1
            else:
                cache[x] += 1

    result = []
    for key, value in cache.items():
        if value >= len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
