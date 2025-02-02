def safe_get(list, index):
    if index < len(list):
        return list[index]
    else:
        return None