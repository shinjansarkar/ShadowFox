my_expenses = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}
partner_expenses = {
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}

my_total_expense=sum(my_expenses.values())
partner_total_expense=sum(partner_expenses.values())

print(my_total_expense)
print(partner_total_expense)

higher = abs(my_total_expense - partner_total_expense)

if my_total_expense>partner_total_expense:

     print("I spent more money",higher)

elif my_total_expense==partner_total_expense:
     print("Both spent same money")

else:
     print("partner spent more money",higher)

difference=0
for catagory in my_expenses:
    difference=abs(my_expenses[catagory]-partner_expenses[catagory])
    


