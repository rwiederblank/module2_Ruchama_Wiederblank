"""
psedocode:
create constants coffe_price, muffin_price and tax
a. create user_input:
    1. in a try/except
    2. get user input for num_coffees, num_muffins, tip_percent
b. create line_total(price, qty)
    1. takes in the unit_price and qty
    2. returns unit_price*qty
c. creat format_currency
    1.takes in a float (amnt of money)
    converts it to a string and rounds to 2 decimal points
    2. returns it with a dollar sign as a string
d. create calcualte_subtotal():
    1. calls line_total() for with the muffin parameters
    2. calls line_total() with coffeee parameters
    3. adds them in variable called subtotal
    4. returns subtotoal, and the totals for muffins and coffees
e. create calculate_tip():
    1. takes in subtotal
    2. returns subtotal * tip_percent / 100
f. create calculate_tax():
    1. takes in subtotal
    2. returns subtotal * the constant tax

In main:
call user_input and store the variables
call calcualte_subtotal and return the variables
print the reciept

"""
#current price of coffee
coffee_price = 2.25
#current price of muffins
muffin_price = 2.75
#current tax rate
tax_rate = .088751

#asks the user how many muffins and coffees they want and their tip percent and returns them
def user_input():
    try:
        num_coffees = int(input('How many coffees? '))
        num_muffins = int(input('How many muffins? '))
        tip_percent = int(input('Enter tip percent (e.g., 10 for 10%): '))
    except ValueError:
        print("Invalid Input. Please enter an integer")
    return num_coffees, num_muffins, tip_percent

#calcualtes the total price based on the unit_price and the desired quantity
def line_total(unit_price, qty):
    return  unit_price * qty

#returns a float as a string rounded to 2 decimal places with a dollar sign (ex: $2.75)
def format_currency(price):
    price = round(price,2)
    price = str(price)
    #print(type(price))
    price= '$' + price
    #print(type(price))
    return price

#calls line_total to calculate the total muffin cost, coffee cost and subtotal
#returns all 3 values
def calculate_subtotal():
    muffin_subtotal = line_total(num_muffins, muffin_price)
    coffee_subtotal = line_total(num_coffees, coffee_price)
    subtotal = muffin_subtotal + coffee_subtotal
    return muffin_subtotal, coffee_subtotal, subtotal


#calculates total including tax and tip and returns it
def calculate_totals(subtotal, tax_rate, tip_percent):
    tip = subtotal * (tip_percent/100)
    tax = subtotal * tax_rate
    total = subtotal + tip + tax
    return tip, tax, subtotal
    
def print_receipt():
    tip, tax, total = calculate_totals(subtotal, tax_rate, tip_percent)
    print('---Receipt---')
    #prints the number of coffees, the unit price of coffee converted into currency and the subtotal, converted into a currency
    print(f'{num_coffees} x coffee @ {format_currency(coffee_price)} = {format_currency(coffee_subtotal)}')
    #prints the number of muffins, the unit price of muffins converted into currency and the subtotal, converted into a currency
    print(f'{num_muffins} x muffin @ {format_currency(muffin_price)} = {format_currency(muffin_subtotal)}')
    #prints the subtotal converted into currency
    print("Subtotal: " , format_currency(subtotal))
    #calcualtes and prints the tax, converted into currency
    print(f'Tax({tax_rate*100}%): {format_currency(tax)}')
    #calcualtes and prints the tip, converted into currency
    print(f'Tip({tip_percent}%): {format_currency(tip)}')
    #calculates and prints the total, formatted into currency
    print('TOTAL: ', format_currency(total))
    print('THANK YOU!')

#calls and stores the user input
num_coffees, num_muffins, tip_percent= user_input()
#calculates the subtotal of each item and the subtotal of them combined and stores them
muffin_subtotal, coffee_subtotal, subtotal = calculate_subtotal()
#calls print_reciept (which calls the calculate_totals() and then prints the reciept
print_receipt()



