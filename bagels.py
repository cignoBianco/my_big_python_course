import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
	print('''Bagels is a deductive logic game.

		I am thinkng of a {}-digit number with no repeated digits.
		Try to guess what is it. Here are some clues"
		When I say:     That means:
		    Pico          One digit is correct but in the wrong position.
		    Fermi         One digit is correct and in the right position.
		    Bagels        No digit is correct.

		F.ex., if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))

	while True:
		secret_number = get_secret_number()
		print('I have thought up a number.')
		print(' You have {} guesses to get it'.format(MAX_GUESSES))

		passed_guesses = 1
		while passed_guesses <= MAX_GUESSES:
			guess = ''
			while len(guess) != NUM_DIGITS:
				print('Guess #{}: '.format(passed_guesses))
				guess = str(raw_input('> '))

			clues = get_clues(guess, secret_number)
			print(clues)
			passed_guesses += 1

			if guess == secret_number:
				break;
			if passed_guesses > MAX_GUESSES:
				print('You ran out of guesses.')
				print('The answer was {}.'.format(secret_number))

		print('Do you want to play again? (1/0)')
		if input('> ') != 1:
			break

	print('Thanks for playing!')

def get_secret_number():
	numbers = list('0123456789')
	random.shuffle(numbers)

	secret_number = ''
	for i in range(NUM_DIGITS):
		secret_number += str(numbers[i])
	return secret_number

def get_clues(guess, secret_number):
	if guess == secret_number:
		return 'You got it!'

	clues = []

	for i in range(len(str(guess))):
		if (guess[i] == secret_number[i]):
			clues.append('Fermi')
		elif guess[i] in secret_number:
			clues.append('Pico')

	if len(clues) == 0:
		return 'Bagels'
	else:
		clues.sort()
		return ' '.join(clues)

	
main()

