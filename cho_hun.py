import random

def main():
    print('''
        In this traditional Japanese dice game, two dice are rolled in a bamboo
        cup by the dealer sitting on the floor. The player must guess
        if the dice total to an even (cho) or odd (han) number.
    ''')

    cho_hun()

def cho_hun():
    user_money = 5000
    bet = ''

    while user_money > 0:
        print('You have {} yen. How much do you bet? (or QUIT)'.format(user_money))
        bet = input('> ')
        if bet.upper() == 'QUIT':
            break
        elif int(bet) > user_money:
            continue
        bet = int(bet)
        
        print('''The dealer swirls the cup and you hear the rattle of dice. The dealer slams the cup on the floor, still covering the dice and asks for your bet.''')
        first_dice_value = roll_the_dice()
        second_dice_value = roll_the_dice()
        dices_sum = first_dice_value + second_dice_value
        
        print('\nCHO (even) or HAN (odd)?')
        preposition = input('> ')

        print('The dealer lifts the cup to reveal:')
        print('____ ____')
        print('|{} | |{} |'.format(first_dice_value, second_dice_value))
        print('____ ____')

        if dices_sum % 2 == 0 and preposition.upper() == 'CHO' or dices_sum % 2 != 0 and preposition.upper() == 'HAN':
            win = bet * 2
            print('You won! You take {} yen!'.format(win))
            fee = bet / 10
            print('The house collects a {} yen fee.'.format(fee))
            user_money += (win - fee)
        else:
            print('Wrong!\n You lost {} yen.'.format(bet))
            user_money -= bet

        print('Now your balance is: {} yen.'.format(user_money))    
        
    print('Thank you for playing!')

def roll_the_dice():
    return random.randrange(1, 6)

main()
