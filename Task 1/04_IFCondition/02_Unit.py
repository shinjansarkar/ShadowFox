#Write a program to determine which country a city belongs to. Given
#list of cities per country

city_to_country ={

"Australia":["Sydney", "Melbourne", "Brisbane", "Perth"],
"UAE" :["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
"India" : ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}
city_name=input("Enter a city name:")
for  country,cities in city_to_country.items():
    if city_name in cities:
        print(f"{city_name} is in {country}")
        break

else:
    print("City not found")





