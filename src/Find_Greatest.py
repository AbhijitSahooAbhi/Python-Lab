

def find_greatest(num1, num2, num3):

  greatest = num1
  if num2 > greatest:
    greatest = num2
  if num3 > greatest:
    greatest = num3
  return greatest


greatest_number = find_greatest(261, 228, 115)
print("The greatest number is:", greatest_number)
