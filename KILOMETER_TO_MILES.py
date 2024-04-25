# 1 kilometer = 0.621371 miles
import sys

def convert():
    try:
        kilometers = float(input("\nENTER THE DISTANCE IN KILOMETERS(KM)\n>>> "))
    except Exception:
        print(f"\nWRONG INPUT...PLEASE ENTER ONLY NUMBERS")
        return convert()
    
    conversion = kilometers * 0.621371

    print(f"THE VALUE OF {kilometers} IN MILES: {conversion}")

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


#DO BOTH ON THE SAME PAGE