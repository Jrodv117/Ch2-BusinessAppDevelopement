#Julian Rodriguez-Vera
#Tip Percentage Calculator
#08/28/2022
#A simple tip percentage calculator.

cost_of_meal = float(input('Enter Cost of Meal: '))
tip_percent = float(input('Enter Tip Percent: '))

tip = cost_of_meal * (tip_percent / 100)

formatted_tip = float("{:.2f}".format(tip))

print(f'Tip amount: {formatted_tip}')


formatted_tip += cost_of_meal

print(f'Total amount: {formatted_tip}')