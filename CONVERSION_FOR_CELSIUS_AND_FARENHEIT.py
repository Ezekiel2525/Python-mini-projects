# farenheit = (celsius * (9/5)) + 32

import sys

class Temperature:

    def Home(self):
        self.choose = input("\nENTER THE CHOICE OF CONVERSION...\n1 TO CONVERT TO FARENHEIT\n2 TO CONVERT TO CELSIUS\n>>> ").strip()
        if self.choose not in ['1', '2']:
            print("\nINVALID INPUT!...PLEASE ENTER ONLY 1 OR 2")
            return self.Home()
        else:
            if self.choose == "1":
                return self.convert_farenheit()
            elif self.choose == "2":
                return self.convert_celsius()
            
    
    def convert_farenheit(self):
        try:
            self.celsius = float(input("\nENTER THE TEMPERATURE IN CELSIUS\n>>> "))
        except Exception:
            print("\nYOU CAN ONLY USE NUMBERS")
            return self.convert_farenheit()

        self.conversion = (self.celsius * 1.8) + 32

        print(f"\n{self.celsius} DEGREE CELSIUS IS EQUAL TO {self.conversion:.2f} DEGREE FARENHEIT")
        return self.Homepage()
    

    def convert_celsius(self):
        try:
            self.farenheit = float(input(f"\nENTER THE TEMPERATURE IN FARENHEIT\n>>> "))
        except Exception:
            print("\nYOU CAN ONLY USE NUMBERS")
            return self.convert_celsius()
        
        self.convert = (self.farenheit - 32) * 0.5556

        print(f"\n{self.farenheit} DEGREE FARENHEIT IS EQUAL TO {self.convert:.2f} DEGREE CELSIUS")
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
            # time.sleep(1) 
            return self.Home()
        else:
            sys.exit()


start = Temperature()
start.Home()
start.convert_farenheit()
start.convert_celsius()








# def init(self, num):
#     convert(num)
#     def cpnvet(self, num):
#         print(num)



# Car(input("Enter your number "))


    
# def convert():
#     try:
#         celsius = float(input("\nENTER THE TEMPERATURE IN CELSIUS\n>>> "))