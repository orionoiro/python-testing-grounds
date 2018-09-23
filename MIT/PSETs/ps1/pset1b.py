
total_cost = int(input('Enter the cost of your dream home: '))
annual_salary = int(input('Enter your starting annual salary: '))
semi_annual_raise = (int(input('Enter the semi­annual raise, as a decimal: ')))/100
portion_saved = (int(input('Enter the percent of your salary to save, as a decimal: ')))/100
portion_down_payment = 0.25
r = 0.04
current_savings = 0

savings_per_month = annual_salary/12 * portion_saved
number_of_months = 0

while current_savings < total_cost * portion_down_payment:
    if number_of_months != 0 and number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        savings_per_month = annual_salary / 12 * portion_saved
    current_savings += savings_per_month + r/12 * current_savings
    number_of_months += 1
print('number of months:', number_of_months)
