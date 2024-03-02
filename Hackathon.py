print("This program takes in an amount of days given by the user to see if they have enough money in their Flex account to do their desired loads of laundry. \nIf they do not, the program will tell them how much they need to add. \nIf they do have enough in their account, the program will tell them how much their leftover balance will be after their laundry is finished.")
#while loop for time variable (checks if data is numeric or is a 'semester')
time = input("\nEnter the desired amount of days or enter 'semester' (without quotations): ")
while time.isnumeric() == False and time.upper() != "SEMESTER":
    time = input("\nEnter the desired amount of days. Enter 'semester' or a number please: ")
        
#while loop for frequency variable (checks if data is numeric)
frequency = input("\nHow often do you typically do your laundry? How many days between each load: ")
while frequency.isnumeric() == False:
    frequency = input("\nHow often do you typically do your laundry? How many days between each load? Enter a number please: ")

#while loop for loads variable (checks if data is numeric)
loads = input("\nHow many loads of laundry do you typically do on one occassion? ")
while loads.isnumeric() == False:
    loads = input("\nHow many loads of laundry do you typically do on one occassion? Enter a number, please: ")

#while loop for loads variable
dryers = input("\nHow many of those loads go in the dryer? ")
while dryers.isnumeric() == False:
    dryers = input("\nHow many of those loads go in the dryer? Enter a number, please: ")

#while loop helper functions for flex balance
def time_change():
    if time.upper() == "SEMESTER":
        newtime = 105
    else:
        newtime = time
    return newtime

def proper_input():
    if len(flex_balance) < 4:
        return False
    elif flex_balance[-3] != ".":
        return False
    else:
        return flex_balance.replace(".", "").isnumeric


#while loop for flex account variable
flex_balance = input("\nHow much money do you have in your flex account? (Format: 00.00): ")
while proper_input() == False:
    flex_balance = input("\nInput a number in the format 00.00. How much money do you currently have in yout flex account?")

#first helper function to find how much money is spent doing laundry once
def find_laundry_money()-> float:
    total_money = 1.75 * float(loads) + 1.75 * float(dryers)
    return total_money

#second helper function to find number of laundry
def find_how_often()-> int:
    if time.upper() == "SEMESTER":
        number_of_loads = 105//int(frequency)
    else: 
        number_of_loads = int(time)//int(frequency)
    return number_of_loads

#finding total amount of money necessary for laundry throughout whole time
def find_total_laundry_money() -> float:
    return find_how_often() * find_laundry_money()

balance_left = float(flex_balance) - find_total_laundry_money()
balance_needed = find_total_laundry_money() - float(flex_balance)

#helper function that checks amount in flex balance & compares it to amount needed to do the desired amount of laundry
def enough_money():
    if (float(flex_balance) > find_total_laundry_money()) or (float(flex_balance) == find_total_laundry_money()):
        print("\nYou have enough money do to your laundry! Your remaining flex balance is: $" + str(balance_left)
    if float(flex_balance) < find_total_laundry_money():
        print("\nYou must add $" + str(balance_needed) + " to your account.")
    return 0

#function call
enough_money()