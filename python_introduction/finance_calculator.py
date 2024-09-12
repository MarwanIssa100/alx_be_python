monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")
monthly_savings = int(monthly_income) - int(monthly_expenses)
print("Your monthly savings are: $", monthly_savings)
projectedSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your projected savings after one year , with interest, is: $", int(projectedSavings))