def dedupe_preserve_order(items):
    new_items = []
    for item in items:
        if item not in new_items:
            new_items.append(item)
#  OR   new_items = list(set(items))
    return new_items

print(dedupe_preserve_order([1,2,1,3,2]))