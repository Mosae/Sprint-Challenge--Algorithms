'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # if word < 0 return 0
    # else travers through the word to find t and h next to each other
    # call the function again
    w = len(word)
    counter = word.count('th')
    if word == '':
        return 0
    elif counter:
        return counter
    else:
        return count_th(word[1:w - 1])
