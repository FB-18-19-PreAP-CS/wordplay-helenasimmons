import re

def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)
         
def has_no_e(word):
    '''
    >>> has_no_e('texas')
    False
    >>> has_no_e('longhorn')
    True
    >>> has_no_e('UTEP')
    False
    '''
    if 'e' in word.lower():
        return False
    else:
        return True
    
def no_e():
    count_no_e = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if has_no_e(word) == True:
                    count_no_e += 1
    a = count_no_e / 113809
    b = a * 100
    print(f'{b:.3F}%')
    
def avoids(word, str):
    '''
    >>> avoids('Texas', 'tpr')
    False
    >>> avoids('Texas', 'bcd')
    True
    >>> avoids('LONGHORNS', 'lgh')
    False
    >>> avoids('longhorns', 'LGH')
    False
    '''
    for letters in word:
        if letters in word:
            return False
        else:
            return True
    
#    for i in range(len(str)):      
#        if str in word:
#            return False
#        else:
#            return True
    
##    for letters in word.lower():
##            return False
##        else:
##            return True
    
def count_avoids():
    pass

def uses():
    pass

#def read_file():
#    
#    with open("island.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():
#                if 'the' in word.lower():
#                    count_the += 1
#        print(count_the)
#    with open("words.txt") as file:
#        count = 0
#        for line in file:
#            for word in line.strip().split():
#                count += 1
#        print(count)


if __name__ == "__main__":
    avoids('Texas', 'tpr')
#    import doctest
#    doctest.testmod()