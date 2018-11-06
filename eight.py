def eight():
    num = input('What is the number? ')
    for i in range(1000000):
        num = str(num).zfill(6)
        if num[2: ] == num[5:1:-1]:
            num = int(num)
            num += 1
            num = str(num)            
            if num[1:] == num[5:0:-1]:
                num = int(num)
                num += 1
                num = str(num)
                if num[1:] == num[4:1:-1]:
                    num = int(num)
                    num += 1
                    num = str(num)
                    if num[:] == num[5:0:-1]:
                        print(num)
        
if __name__ == "__main__":
    eight()