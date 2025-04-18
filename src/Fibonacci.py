# prompt: print nth no of Fibonacci Series

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            print(b)
        return b

number = int(input("Enter the value of n: "))
print(f"The {number}th Fibonacci number is: {fibonacci(number)}")
