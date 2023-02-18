import random

OBJECT_PRONOUNCE = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
CLICKBAIT_TYPES = ['AreMillennialsKilling', 'WhatYouDontKnow',
                   'BigCompaniesHateHer', 'YouWontBelieve', 'DontWantYouToKnow',
                   'GiftIdea', 'ReasonsWhy']

def main():
    print('''Our website needs to trick people into looking at ads!
Enter the number of clickbait headlines to generate:''')
    while True:
        count = input('> ')
        if not count.isdecimal():
            print('not valid data')
        elif int(count) <= 0:
            print('not valid data')
        else: 
            count = int(count)
            break
        
    headers = generate_headers(count)
    for header in headers:
        print(header)

def generate_headers(count):
    result = []
    for i in range(0, count):
        clickbait_type = random.choice(CLICKBAIT_TYPES)

        if clickbait_type == 'AreMillennialsKilling':
            headline = generate_are_millennials_killing()
            result.append(headline)
        elif clickbait_type == 'WhatYouDontKnow':
            headline = generate_what_you_dont_know()
            result.append(headline)
        elif clickbait_type == 'BigCompaniesHateHer':
            headline = generate_big_companies_hate_her()
            result.append(headline)
        elif clickbait_type == 'YouWontBelieve':
            headline = generate_you_wont_believe()
            result.append(headline)
        elif clickbait_type == 'DontWantYouToKnow':
            headline = generate_dont_want_you_to_know()
            result.append(headline)
        elif clickbait_type == 'GiftIdea':
            headline = generate_gift_idea()
            result.append(headline)
        elif clickbait_type == 'ReasonsWhy':
            headline = generate_reasons_why()
            result.append(headline)

    return result

def generate_are_millennials_killing():
    noun = random.choice(NOUNS)
    return 'Are Millenials Kill the {} Industry?'.format(noun)

def generate_what_you_dont_know():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, plural_noun, when)

def generate_big_companies_hate_her():
    pronoun = random.choice(OBJECT_PRONOUNCE)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)

def generate_you_wont_believe():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Belive What This {} {} Found in {} {}'.format(state, noun, pronoun, place)

def generate_dont_want_you_to_know():
    plural_noun = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You Know About {}'.format(plural_noun, plural_noun2)

def generate_gift_idea():
    pronoun = random.choince(OBJECT_PRONOUNCE)
    noun = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Gift Idea for {}: {} {}'.format(pronoun, noun, noun2)

def generate_reasons_why():
    num = random.randint(3, random.randin(5, 100))
    surprizing_num = random(3, num)
    nouns = random.choice(NOUNS)
    return '{} Reasons Why {} Are More Interesting Than You Think ( Number {} Will Surprise You!)'.format(num, nouns, surprizing_num)

main()
