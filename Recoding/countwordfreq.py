def word_frequency(sentence: str) -> dict:
    word_count = {}
    sentence = sentence.lower().split()
    for word in sentence:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


print(word_frequency("the quick brown fox jumps over the lazy dog"))
print(word_frequency("Apple apple APPLE"))
