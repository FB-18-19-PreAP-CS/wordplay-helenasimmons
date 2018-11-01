import re

def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)
                    
def has_no_e(word):
    if 'e' in word:
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
    print(f'{a * 100}%')
    
def avoids(word, str):
    pass

def count_avoids():
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
    no_e()