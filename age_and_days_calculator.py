from datetime import datetime

print('''
  ____      _            _       _          _
 / ___|__ _| | ___ _   _| | __ _| |_ ___   / \   __ _  ___
| |   / _` | |/ __| | | | |/ _` | __/ _ \ / _ \ / _` |/ _ \ 
| |__| (_| | | (__| |_| | | (_| | ||  __// ___ \ (_| |  __/
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/_/   \_\__, |\___|
                                                |___/
    _              _ ____
   / \   _ __   __| |  _ \  __ _ _   _ ___
  / _ \ | '_ \ / _` | | | |/ _` | | | / __|
 / ___ \| | | | (_| | |_| | (_| | |_| \__ \ 
/_/   \_\_| |_|\__,_|____/ \__,_|\__, |___/
                                 |___/\n''')
     
user_year = int(input("What year you were born?: "))
birth_date = int(input("What day is your birth day?: "))

date_today = datetime.today()
current_year = datetime.now()
str_year = current_year.strftime("%Y")
str_date = date_today.strftime("%d")
age = int(str_year)-user_year
day_difference = int(str_date)-birth_date
days = int(age*365)+day_difference+int(str_date)
months = int(days/31)

if (user_year % 400 == 0) and (user_year % 100 == 0):
    days += 1

elif (user_year % 4 == 0) and (user_year % 100 != 0):
    days += 1

if user_year <= 1000:
    print("\nYear Invalid, enter a year ex. 2008")
    
elif user_year >= int(str_year):
    print("\nYear cannot be subtracted to current year, ex. 2008")

elif birth_date >= 32:
    print("\nInvalid Date of birth, enter a date ex. 31")

else:
    print("\nYour age is:", age)
    print("\nAnd you were alive for:")
    print(age,"Years")
    print(months,"Months")
    print(days,"Days")
    print("\nNot so sure? about",days,'''Days, open your calculator
app and divide the days by 365 which is the total days every single
year, if its return your age with decimal numbers it means your actually living''',days,"Days")


    

