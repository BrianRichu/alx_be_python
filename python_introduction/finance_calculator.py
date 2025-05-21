monthlyincome = int(input("Enter your monthly income:"))
total_expenses = int(input("Enter your total monthly expenses:"))
monthlysavings = monthlyincome - total_expenses
projected_savings = (monthlysavings * 12 + (monthlysavings * 12 * 0.05))

print("your monthly savings are $",monthlysavings)
print("Projected savings after one year, with interest, is $",projected_savings)
