def count_words(text):
    words = len(text.split())
    return f"Found {words} total words"  

def count_char(text):
    result = {}
    for c in text.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1

    return result

def sort_dict(char_counts):
    dicts = []
    for c, num in char_counts.items():
        dicts.append({"char": c, "num": num})
    dicts.sort(key = get_num)
    dicts.reverse()
    return dicts

def get_num(d):
    return d["num"]
