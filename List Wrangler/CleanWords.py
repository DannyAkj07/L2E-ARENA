def clean_words(words):
    # new_words = []
    # for item in words:
    #     item = item.strip().lower()
    #     if item == "":
    #         continue
    #     new_words.append(item)
    
    new_words = [item.lower().strip() for item in words if item.strip()]
    return new_words

print(clean_words([" ","Hello",""]))