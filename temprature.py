unit = input("Is the temprature in Celcius of Fahrenheit just type (C/F): ")
temp = int(input("Enter the temprature: "))
if(unit == "C"):
    result = int((temp*1.8)+32)
    unit = "Fahrenheit"
    print(f"{temp} Degree in {unit} is: {result}")
elif(unit == "F"):
    result = int((temp-32)/1.8)
    unit = "Celcius"
    (print(f"{temp} Degree in {unit} is: {result}"))
else:
    print(f"{unit} is not Valid")