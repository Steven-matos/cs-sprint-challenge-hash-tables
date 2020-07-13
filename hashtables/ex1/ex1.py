def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for i in range(len(weights)):
        if weights[i] not in cache:
            cache[weights[i]] = [i]
        else:
            cache[weights[i]].append(i)

    lists = []
    for x in cache:
        target = limit - x

        if target in cache:
            lists.append(cache[target])

    final_list = [item for sublist in lists for item in sublist]

    final_list.sort(reverse=True)

    if len(lists) < 1:
        return None
    else:
        return final_list
