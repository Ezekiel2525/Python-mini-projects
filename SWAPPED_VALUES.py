import sys

def swap():
    a = input("\nENTER THE VALUE OF THE FIRST VARIABLE\n>>>  ")
    b = input("\nENTER THE VALUE OF THE SECOND VARIABLE\n>>> ")

    print(f"\nORIGINAL VALUES: a = {a}, b = {b}\n")
    temp = a
    a = b
    b = temp
    print(f"\nSWAPPED VALUES: a = {a}, b = {b}\n")

    print("DO YOU WANT TO PERFORM ANOTHER OPERATION?\n")

    while True:
        operation = input(f"\nENTER Y FOR YES OR Q TO QUIT\n>>> ").strip().upper()
        if operation not in ['Y', 'Q']:
            continue
        else:
            break
    if operation.upper() == 'Y':
        return swap()
    else:
        sys.exit()

if __name__ == "__main__":
    start = swap()
    start()

        









