attempt=1
print('this game is limited to 9 attempt only')
number=18
while(attempt<=9):
    n=int(input('guess the number :'))
    if(n<number):
        
        print('you have entered wrong no which is less , please enter greater no then last time')
    elif(n>number):
        
        print('you have entered wrong no which is less , please enter lesser no then last time')
    else:
        
        if (n==number):
            print('you guess the right no , you won Hurray!!!!') 
            print('you have taken ',attempt,'attempt to won this game')
            break
        
    print(9-attempt, 'left')
    attempt=attempt+1
    
if(attempt>9):
    print("game over")