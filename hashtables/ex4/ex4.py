def has_negatives(a):
    cache = {}
    result = []

    for value in a:
        if value * -1 not in cache:
            cache[value] = value
        else:
            result.append(abs(value))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
