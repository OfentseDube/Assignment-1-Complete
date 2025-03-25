def calculator():
    print("Simple Calculator")
    print("----------------")
    
    try:
        # Get input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        # Validate operation
        if operation not in ['+', '-', '*', '/']:
            print("Error: Invalid operation. Please use +, -, *, or /")
            return
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        else:  # division
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        
        # Display result
        print(f"\n{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
