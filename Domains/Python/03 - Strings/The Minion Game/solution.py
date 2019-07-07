import itertools

def minion_game(string):
    allSubstrings = set()
    kevin = 0
    stuart = 0

    strlen = len(string)

    for i in range(strlen):
        if string[i] in 'AEIOU':
            kevin += strlen - i
        else:
            stuart += strlen - i
    
    if kevin > stuart:
        print('Kevin ' + str(kevin))
    elif stuart > kevin:
        print('Stuart ' + str(stuart))
    else:
        print('Draw')

