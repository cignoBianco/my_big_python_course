import datetime

MONTHES = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December')
WEEK_DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def main():
    print('Calendar maker!')
    calendar_maker()

def calendar_maker():
    user_year = get_year()
    user_month = get_month()
    
    calendar = get_calendar_for(user_year, user_month)
    print(calendar)
    
    calendar_name = 'calendar_{}_{}.txt'.format(user_month, user_year)
    with open(calendar_name, 'w') as fileObj:
        fileObj.write(calendar)
    print('The calendear was saved to {}.'.format(calendar_name))

def get_calendar_for(year, month):
    cal_text = ''

    cal_text += (' ' * 34) + MONTHES[month - 1] + ' ' + str(year) + '\n..'
    for week_day in WEEK_DAYS:
        cal_text += '...' + week_day
    cal_text += '.....\n'

    week_separator = ('+----------' * 7) + '+\n'
    blank_row = ('|          ' * 7) + '|\n'

    current_date = datetime.date(year, month, 1)

    while current_date.weekday() != 0:
        current_date -= datetime.timedelta(days = 1)

    while True:
        cal_text += week_separator

        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days = 1)

        day_number_row += '|\n'
        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        if current_date.month != month:
            break

    cal_text += week_separator
    return cal_text
    

def get_year():
    print('Enter the year for the calendar:')
    while True:
        year = input('> ')
        if year.isdecimal() and int(year) > 0:
            return int(year)

        print('Please enter a numeric year')
        continue

def get_month():
    print('Enter the month for the calendar, 1-12:')
    while True:
        month = input('> ')
        if month.isdecimal() and 0 < int(month) < 13:
            return int(month)

        print('Plesae enter the numeric value')
        continue

main()
