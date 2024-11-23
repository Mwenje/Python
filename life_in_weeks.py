def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    return print(f"You have {weeks_left} weeks left.")


your_age = int(input("Enter your age: "))
life_in_weeks(your_age)
