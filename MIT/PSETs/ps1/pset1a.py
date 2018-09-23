
total_cost = int(input('enter the cost of your dream home: '))
annual_salary = int(input('enter your  annual salary: '))
portion_saved = (int(input('enter the portion of salary to be saved: ')))/100
portion_down_payment = 0.25
r = 0.04
current_savings = 0

savings_per_month = annual_salary/12 * portion_saved
number_of_months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += savings_per_month + r/12 * current_savings
    number_of_months += 1
print('number of months:', number_of_months)
