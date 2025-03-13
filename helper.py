def dictionary_to_list(dict):
    result = []
    for pair in dict:
        result.append(list(pair.values()))

    return result