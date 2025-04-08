def generate_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    generate_pyramid(rows)

