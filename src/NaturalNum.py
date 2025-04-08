

def print_natural_numbers(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    for i in range(1, n + 1):
        print(i, end=" ")

n = int(input("Enter the value of N: "))
print_natural_numbers(n)