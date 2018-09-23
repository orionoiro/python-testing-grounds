annual_salary = int(input('Enter your starting annual salary: '))
semi_annual_raise = 0.07
r = 0.04  # annual return

portion_down_payment = 0.25
total_cost = 1000000
down_payment = total_cost * portion_down_payment
current_savings = 0
number_of_guesses = 0

left_border = 0
right_border = 10000

while down_payment - current_savings >= 100 or current_savings - down_payment >= 100:
    current_savings = 0
    number_of_months = 0
    x = (left_border + right_border) / 2
    portion_saved = x / 10000
    salary_per_month = annual_salary / 12
    savings_per_month = salary_per_month * portion_saved

    while number_of_months <= 36:
        if number_of_months != 0 and number_of_months % 6 == 0:
            salary_per_month += salary_per_month * semi_annual_raise
        if number_of_months != 0 and number_of_months % 12 == 0:
            current_savings += current_savings * r

        current_savings += savings_per_month
        number_of_months += 1

    if current_savings < down_payment:
        left_border = x
    else:
        right_border = x

    number_of_guesses += 1
print('Best savings rate:', round(portion_saved, 4), '\nSteps in bisection search:', number_of_guesses)
