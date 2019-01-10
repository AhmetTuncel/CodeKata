def duplicate_count(text):
    text = text.lower()
    textSet = set()
    return len({i for i in text if i in textSet or textSet.add(i) is not None})