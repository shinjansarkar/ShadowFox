#Write a program to check if two cities belong to the same country.
#Ask the user to enter two cities and print whether they belong to the
#same country or not.

city_to_country ={

"Australia":["Sydney", "Melbourne", "Brisbane", "Perth"],
"UAE" :["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
"India" : ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

first_city=input("Enter first city:")
second_city=input("Enter second city:")

for country,cities in city_to_country.items():
    if first_city in cities and second_city in cities:
        print(f"Both cities in {country}")
        break

else:
    print("They dont belong to the same country")