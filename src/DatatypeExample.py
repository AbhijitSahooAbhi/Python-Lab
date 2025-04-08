# Program to read and print values of variables of different data types

# Reading values
integer_var = int(input("Enter an integer value: "))
float_var = float(input("Enter a float value: "))
string_var = input("Enter a string value: ")
boolean_var = input("Enter a boolean value (True/False): ").capitalize() == 'True'

# Printing values
print("Integer value:", integer_var)
print("Float value:", float_var)
print("String value:", string_var)
print("Boolean value:", boolean_var)