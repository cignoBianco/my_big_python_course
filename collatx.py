print('''The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:
1. if n - even, next -> n / 2
2. if n - odd, next -> n * 3 + 1
3. if n = 1, stop, otherwise repeat.\n''')

print('Enter a starting number (greater than 0):')
while True:
    number = input('> ')
    if not number.isdecimal():
        print('enter a valid number')
        conitinue
    elif int(number) < 0:
        print('enter a number greater than 0')
    else:
        number = int(number)
        break;

result = [number]
while number != 1:
    number = number / 2 if number % 2 == 0 else  number * 3 + 1
    result.append(number)

print(result)
