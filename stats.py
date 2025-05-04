def count_words(text):
    count = len(text.split())
    return count


def count_characters(text):
    result = {}
    
    for char in text:
        lowered = char.lower()
        result[lowered] = result.get(lowered, 0) + 1
    
    return result


def sort_on(dict):
    return dict['num']


def sort_characters(char_dict):
    result = []

    for key, value in char_dict.items():
        result.append({'char': key, 'num': value})
    
    result.sort(reverse=True, key=sort_on)

    return result
