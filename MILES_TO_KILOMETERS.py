# 0.621371 miles = 1 kilometers
# 1miles = 1.609344497892563
import sys

def convert():
    try:
        miles = float(input("\nENTER THE DISTANCE IN MILES\n>>>> "))
    except Exception:
        print("\nWRONG INPUT!...PLEASE ENTER ONLY NUMBERS")
        return convert()
    
    conversion = miles * 1.609344497892563

    print(f"THE VALUE OF {miles} IN KILOMETERS: {conversion}")

    print("\nWANT TO PERFORM ANOTHER OPERATION?")

    while True:
        operation = input(f"ENTER Y FOR YES OR N FOR NO\n>>>> ").strip().upper()
        if operation not in ['Y', 'N']:
            continue
        else:
            break

    if operation.upper() == 'Y':
        return convert()
    else:
        sys.exit()

if __name__ == '__main__':
    start = convert()
    start()


    