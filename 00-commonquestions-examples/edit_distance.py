def levenshtein_distance(str1, str2):
    '''
    Function to evaluate the differences between two strings:
    min number of single-char edits required to change one word to another.
    '''
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    distances = range(len(str1) + 1)

    for index_str2, char_str2 in enumerate(str2):
        distances_ = [index_str2 + 1]
        for index_str1, char_str1 in enumerate(str1):
            if char_str1 == char_str2:
                distances_.append(distances[index_str1])
            else:
                distances_.append(1 + min((distances[index_str1],
                                           distances[index_str1 + 1], distances_[-1])))
        distances = distances_

    return distances[-1]

if __name__ == "__main__":
    print(levenshtein_distance("hippo", "happy"))
