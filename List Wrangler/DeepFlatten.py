def deepflatten(items):
    flat_list = []
    for item in items:
        if isinstance(item, list):
            flat_list.extend(deepflatten(item))
        else:
            flat_list.append(item)
    return flat_list


print(deepflatten([1, [2,[5,6,2], 3], 4]))


