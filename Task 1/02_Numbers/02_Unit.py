#In a village, there is a circular pond with a radius of 84 meters.
#Calculate the area of the pond using the formula: Circle Area = π
#r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
#1.4 liters of water in a square meter, what is the total amount of
#water in the pond? Print the answer without any decimal point in
#it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
#Water per Square Meter

Radius= 84
pi=3.14
area=pi*Radius**2
water_per_square_meter=1.4
total_water=int(area+water_per_square_meter)
print("Total amount of water in pond=",total_water)