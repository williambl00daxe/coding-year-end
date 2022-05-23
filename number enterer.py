#number input thing
for number in range (4):


    lit=input('enter a number')
    if lit.upper=='Q':
        str(lit)
        break

    n=int(lit)


    if n<5:
        print('small number')

    elif n<10:
            print('medium number')
    else:
        print('large number')



print('done')



