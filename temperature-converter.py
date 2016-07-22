# The following code allows users to convert temperature from Celsius to
# Fahrenheit and vise-versa.

print("")
unit = str(input("Will you be converting a Celsius or Fahrenheit value [C/F]? ")).lower()
value = int(input("Enter the value you would like to convert: "))
print("")

if unit == "c":
    fahrenheit = round(value*1.8 + 32, 2)
    print(value, "C is equal to ", fahrenheit, "F." )
elif unit == "f":
    celsius = round((value - 32)/1.8, 2)
    print(value, "F is equal to ", celsius, "C." )
else:
    print("Invalid input.")
