#Toss a Coin by HitMonkey69

import random
import pyfiglet

banner = pyfiglet.figlet_format('Toss a Coin')
print(banner)

print('Select 1 to toss') 
print('')
print('Select 2 to quit')
print('')

while True:
    
    usr = int(input('Enter your choice here:'))
    print('')
    
    if usr == 1:
        computer = random.randint(1,2)

        if computer == 1:
            heads = pyfiglet.figlet_format('Heads')
            print(heads)

        elif computer == 2:
            tails = pyfiglet.figlet_format('Tails')
            print(tails)
        
    
    elif usr == 2:
        banner2 = pyfiglet.figlet_format('Bye.')
        print(banner2)
        break


    else:
        print('Wrong input. Pease select again')
        