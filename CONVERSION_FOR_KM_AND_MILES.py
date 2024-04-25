import sys
import time

class Conversion:

    def Home(self):
        self.choice = input(f"\nENTER YOUR CHOICE OF CONVERSION...\n1 TO CONVERT KILOMETERS TO MILES\n2 TO CONVERT MILES TO KILOMETERS\n>>> ").strip()
        print("\nPROCESSING...\n")
        time.sleep(1)
        if self.choice not in ["1", "2"]:
            print(f"WRONG INPUT!...{self.choice.upper()} IS NOT VALID.\nPLEASE ENTER 1 OR 2")
            return self.Home()
        else:
            if self.choice == "1":  
                return self.convert_km()
            elif self.choice == "2":  
                return self.convert_miles()


    # 1 kilometers =  0.621371 miles   
    def convert_km(self):
        try:
            self.kilometers = float(input(f"\nENTER THE DISTANCE IN KILOMETERS\n>>> "))
        except Exception:
            print("\nPLEASE...YOU CAN ONLY ENTER NUMBERS")
            return self.convert_km()

        self.convert_factor = self.kilometers * 0.621371
        print("\nPROCESSING.......\n")   
        time.sleep(2) 
        print(f"\nTHE VALUE OF {self.kilometers} KILOMETERS IN MILES: {self.convert_factor:.2f} MILES")
        return self.Homepage()


    # 1miles = 1.609344497892563
    def convert_miles(self):
        try:
            self.miles = float(input(f"\nENTER THE DISTANCE IN MILES\n>>> "))
        except Exception:
            print("\nPLEASE YOU CAN ONLY USE NUMBERS")
            return self.convert_miles()
        
        self.convert_ml = self.miles * 1.609344497892563
        print("\nPROCESSING.......\n")   
        time.sleep(2) 
        print(f"\nTHE VALUE OF {self.miles} MILES IN KILOMETERS: {self.convert_ml:.2f} KM")
        return self.Homepage()


    def Homepage(self):
        print("\nWANT TO PERFORM ANOTHER OPERATION?")
        while True:
            self.operation = input(f"\nENTER Y FOR YES OR Q to QUIT\n>>>> ").strip().upper()
            if self.operation not in ['Y', 'Q']:
                continue
            else:
                break
        if self.operation == 'Y':
            print("\nLOADING.......\n")   
            time.sleep(1) 
            return self.Home()
        else:
            sys.exit()


start = Conversion()

start.Home()
start.convert_km()
start.convert_miles()

        
            


        





                       