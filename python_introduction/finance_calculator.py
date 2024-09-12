monthlyIncome = input("Enter your monthly income: ")
monthlyExpenses = input("Enter your monthly expenses: ")
savings = int(monthlyIncome) - int(monthlyExpenses)
print("Your monthly savings are: $", savings)
projectedSavings = savings * 12 + (savings * 12 * 0.05)

print("Your projected savings after one year , with interest, is: $", int(projectedSavings))