import datetime, random

def get_bitrhdays(number_of_birthdays):
	birthdays = []
	for i in range(number_of_birthdays):
		start_of_the_year = datetime.date(2000, 1, 1); # a year in this calculation doesn't matter as long as the op is the same
		random_count_of_days = datetime.timedelta(random.randint(0, 364))
		birthday = start_of_the_year + random_count_of_days
		birthdays.append(birthday)
	return birthdays

# returns repeated birthday
def get_match(birthdays):
	if len(birthdays) == len(set(birthdays)):
		return None

	for a, first_birthday in enumerate(birthdays):
		for b, second_birthday in enumerate(birthdays[a + 1 :]):
			if (first_birthday == second_birthday):
				return first_birthday

def birthday_paradox():
	print('''Birthday paradox

		The Birthday Paradox shows us that in a group of N people, the oods
		that two of them have matching birthdays is suprisingly large.
		This program does a Monte Carlo simulation
		(that is, repeated random simulations) to explore this concept.
		''')

	MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

	while True:
		print('How many birthdays shall I generate? (p.s. max 100)')
		response = input('> ')
		if 0 < int(response) <= 100:
			number_of_birthdays = response
			break
	print()

	print('Here are', number_of_birthdays, 'birthdays:')
	birthdays = get_bitrhdays(number_of_birthdays)
	for i, birthday in enumerate(birthdays):
		month_name = MONTHS[birthday.month - 1]
		full_date = '{} {}'.format(month_name, birthday.day)
		print(full_date)

	match = get_match(birthdays)

	print('In this simulation, ')
	if match != None:
		month_name = MONTHS[match.month - 1]
		full_date = '{} {}'.format(month_name, match.day)
		print('multiple people have a birthday on', full_date)
	else:
		print('Ooops... There are no matching birthdays')

	print('Generating ', number_of_birthdays, ' random birthdays 100,000 times...')
	raw_input('Press Enter to begin...')

	print('Let\'s run another 100,000 simulations.')
	sim_match = 0
	for i in range(100000):
		if i % 10000 == 0:
			print(i, 'simulations run...')
		birthdays = get_bitrhdays(number_of_birthdays)
		if get_match(birthdays) != None:
			sim_match = sim_match + 1
	print('100,000 simulations run')
	print('sm', sim_match)
	print(round((sim_match * 100) / 100000, 2))
	probability = round((sim_match * 100) / 100000, 2)
	print('Out of 100,000 simulations of', number_of_birthdays, 'prople, there was a matching birthday in that group', sim_match, 'times.')
	print('This means that ', number_of_birthdays, 'people have a ', probability, '% chance og having a matching birthday in their group')
	print('That\'s probably more than you would think!')


birthday_paradox()
