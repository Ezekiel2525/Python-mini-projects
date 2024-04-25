import sys

def calculator():
    try:
        num1 = float(input("\nENTER THE FIRST NUMBER\n>>>> "))
        num2 = float(input("\nENTER THE SECOND NUMBER\n>>>> "))
    except Exception:
        print("NOT A VALID NUMBER!!!...PLEASE ENTER ONLY NUMBERS")
        return calculator()

    operations = input("""\nENTER...
                1 FOR ADDITION\n
                2 FOR SUBTRACTION\n
                3 FOR MULTIPLICATION\n
                4 FOR DIVISION\n
                >>>> """)
    
    if operations == "1":
        addition = num1 + num2
        print(f"\nsum of {num1} + {num2} = {addition:.2f}")
    elif operations == "2":
        subtraction = num1 - num2
        print(f"\ndifference of {num1} - {num2} = {subtraction:.2f}")
    elif operations == "3":
        multiplication = num1 * num2
        print(f"\nmultiplication of {num1} * {num2} = {multiplication:.2f}")
    elif operations == "4":
        if num1 == 0 or num2 == 0:
            print(f"\nERROR! DIVISION BY ZERO IS NOT ALLOWED")
            return calculator()
        else:
            division = num1 / num2
            print(f"\ndivision of {num1} / {num2} = {division:.2f}")
    else:
        print("\nWRONG INPUT...PLEASE ENTER 1, 2, 3, OR 4")
        return calculator()
    
    print("\nDO YOU WANT TO PERFORM ANOTHER OPERATION? ")

    while True:
        Another_operation = input(f"\nENTER Y FOR YES OR Q TO QUIT\n>>> ").strip().upper()
        if Another_operation.upper() not in ['Y', 'Q']:
            print("WRONG INPUT!...PLEASE ENTER Y OR Q")
            continue
        else:
            break
    if Another_operation.upper() == "Y":
        return calculator() 
    else:
        sys.exit()
    
if __name__ == "__main__":    
    start = calculator()
    start()
            
           


