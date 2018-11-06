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
    
def avoids(word, string):
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
    for letter in word:
        for ele in string.lower():
            if ele in word.lower():
                return False
        else:
            return True
    
def count_avoids():
    count = 0
    letters = input('What are the forbidden letters? ')
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(word, letters) == True:
                    count += 1
    print(count)


def uses_only(word,string):
    '''
    Returns true if the word contains only the letters in the string.
    >>> uses_only('yes', 'sey')
    True
    >>> uses_only('watermelon', 'xyz')
    False
    >>> uses_only('three', 'rent')
    False
    >>> uses_only('yes', 'yesa')
    False
    '''
    for letter in word:
        if letter in word:
            return True
        else:
            return False

def words_with_only():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                pass

def uses_all():
    pass

def how_many_uses_all():
    pass

def is_abecedarian(word):
    '''
    >>> is_abecedarian('abcde')
    True
    >>> is_abecedarian('yes')
    False
    '''
    for i in range(len(word) - 1):
        if word[i] > word[i+1]:
            return False
        else:
            return True

            
    
def count_abecedarian():
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
    import doctest
    doctest.testmod()