#guess game
import random
h=10
a=random.randint(1,h)
g=int(input('Enter your guess:'))
if g==a:
    print('Holy Shit ... congrats')
else:
    if g<a:
        print('Please guess higher')
    else :
        print('Please guess lower')
    g=int(input())
    if g==a:
        print('Congrats')
    else:
        print('Sorry please try again.. \nThe answer is {}'.format(a))

