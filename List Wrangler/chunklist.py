def chunk_list(items,size):
    if size < 1:
        return "Invalid size"
    chunks = []
    for i in range(0,len(items),size):
        chunk = items[i:i + size]
        chunks.append(chunk)
    return chunks

print(chunk_list([1,2,3,4,5], 2))
