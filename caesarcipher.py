SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('Do you want to (e)ncrypt or (d)ecript?')
    crypto_type = input('> ')
    result = crypt(crypto_type)
    print(result)

def crypt(crypto_type):
    print('Please enter the key (0 to 25) to use.')
    key_bias = int(input('> '))
    
    print('Enter the message to encrypt.')
    message = input('> ').upper()

    result = ''
    for letter in message:
        if letter in SYMBOLS:
            num = SYMBOLS.find(letter)
            num = num + key_bias if crypto_type == 'e' else num - key_bias
            if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)
            elif num < 0:
                num = num + len(SYMBOLS)
            result = result + SYMBOLS[num]
        else:
            result = result + letter
    return result
