def multiplication_table():
    try:
        number_for_multiplication = int(input("Please enter a number\n"))
        upper_limit = int(input("Enter the range up to which you want the table (e.g., 10 for 1-10)\n"))
        
        for i in range(1, upper_limit + 1):
            result = i * number_for_multiplication
            print(f"{i} * {number_for_multiplication} = {result}")
    except ValueError:
        print("Please enter a valid number.")

multiplication_table()
