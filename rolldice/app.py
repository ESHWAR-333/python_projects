import random
def main():
    x='y'
    while(x=='y'):
        n=int(random.randint(1,6))
        if n==1:
            print("===========")
            print("|         |")
            print("|    O    |")
            print("|         |")
            print("===========")
        elif n==2:
            print("===========")
            print("|         |")
            print("| 0     0 |")
            print("|         |")
            print("===========")
        elif n==3:
            print("===========")
            print("|    0    |")
            print("|    0    |")
            print("|    0    |")
            print("===========")
        elif n==4:
            print("===========")
            print("| 0     0 |")
            print("|         |")
            print("| 0     0 |")
            print("===========")
        elif n==5:
            print("===========")
            print("| 0     0 |")
            print("|    0    |")
            print("| 0     0 |")
            print("===========")    
        else:
            print("===========")
            print("| 0     0 |")
            print("| 0     0 |")
            print("| 0     0 |")
            print("===========")
        print('Enter the Y to roll the dice')
        X=input()
if __name__=='__main__':
    main()