n1=int(input('enter first no'))
n2=int(input('enter second no'))

opertor = input('enter operator "+", "-" , "*" , "/"  :->')

if n1 ==45 & n2==3 & opertor=='*':
    print("555")
elif n1 == 56 and n2 == 9 and opertor == '+':
        print("77")
elif n1 == 56 and n2 == 6 and opertor == '/':
        print("4")
elif(opertor=='+'):
    print('Addition of your no is: ',n1+n2)
elif(opertor=='-'):
    print('subtraction of your no is: ',n1-n2)
elif (opertor=='*'):
    print('multiplication of your no is: ',n1*n2)
else:
    print('division of your no is: ',n1/n2)