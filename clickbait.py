import random

OBJECT_PRONOUNCE = ('Her', 'Him', 'Them')
POSSESIVE_PRONOUNS = ('Her', 'His', 'Their')
PERSONAL_PRONOUNS = ('She', 'He', 'They')
STATES = ('California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan')
NOUNS = ('Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic')
PLACES = ('House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker')
WHEN = ('Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week')
CLICKBAIT_TYPES = ('AreMillennialsKilling', 'WhatYouDontKnow',
                   'BigCompaniesHateHer', 'YouWontBelieve', 'DontWantYouToKnow',
                   'GiftIdea', 'ReasonsWhy', 'JobAutomated')

def main():
    print('''Our website needs to trick people into looking at ads!
Enter the number of clickbait headlines to generate:''')
    count = 0
    while not count.isdecimal() or count <= 0:
        count = input('> ')
        
    headers = generate_headers(count)
    for (header in headers):
        print(header)

def geneate_headers(count):
    result = ()
    for i in range(1, count):
        

        

main()
