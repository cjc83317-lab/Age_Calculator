from datetime import date

def calculate_age(birthdate,target_date):
    age = target_date.year - birthdate.year

    if (target_date.year ,target_date.day) < (birthdate.year, birthdate.day):
        age -= 1

    return age

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day: "))
birthdate = date(year, month, day)


target_year = int(input("Enter the target year: "))
target_month = int(input("Enter the target month (1-12): "))
target_day = int(input("Enter the target day: "))
target_date = date(target_year, target_month, target_day)

print("Your age on", target_date, "will be:", calculate_age(birthdate, target_date))
       


