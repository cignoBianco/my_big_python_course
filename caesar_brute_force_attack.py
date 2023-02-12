LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY_DIAS_COUNT = 26

def main():
    print('Caesar Cipher Hacker')
    print('Enter the encrypter Casear cipher message to hack.')
    message = input('> ')
    hack_caesar(message)

def hack_caesar(str):
    str = str.upper()
    for i in range(KEY_DIAS_COUNT):
        result = ''
        for letter in str:
            if letter in LETTERS:
                num = LETTERS.find(letter)
                num = num + i
                if num >= len(LETTERS):
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)
                result += LETTERS[num]
            else:
                result += letter
            
        print('Key #{}: {}'.format(i, result))
        
