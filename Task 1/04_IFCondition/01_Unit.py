#Write a program to determine the BMI Category based on user input.
#Ask the user to:
height=float(input("Enter Height="))
weight=float(input("Enter Weight="))

bmi=weight/height**2

if bmi>=30:
    print("Obesity")
elif 25<= bmi <=30:
    print("Overweight")
elif 18.5<=bmi<=25:
    print("Normal")
else:
    print("Underweight")
