
def string_ends(str):
  if len(str) < 2:
    return ""
  return str[0:2] + str[-2:]


input_string = input("Enter a string: ")
result = string_ends(input_string)
print("Result:", result)
