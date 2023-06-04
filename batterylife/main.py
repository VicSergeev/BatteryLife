# June 4th 2023
# BatteryLife v1.1
# made by Vic Sergeev for own purposes and just for fun, because I love python
# this is a part of future project for iPad

# libraries needed to compile executable file

# for WIN64 machines
# pip install auto-py-to-exe

# after installation execute following code in terminal
# auto-py-to-exe
# perform following instruction from PyInstaller screen

def greet():
    print("""
            _______________________
            |                     |
            |   T = (Ah * 10) / W |
            |_____________________|
    """)

def data_collection():
    greet()
    while True:
        try:
            ampers_per_hour = float(input("Enter your battery capacity(Ah): "))
            break
        except ValueError:
            print("value must be number(integer or floating point)")
    while True:
        try:
            watts = float(input("Enter your consumer power in watts: "))
            break
        except ValueError:
            print("value must be number(integer or floating point)")
    result = ((ampers_per_hour * 10) / watts) * 60
    print(f'Approximate battery life of {ampers_per_hour}Ah capacity with {watts}W consumers is ~{result} minutes')
    repeat_calc()

def repeat_calc():
    possible_answers = ["yes", "y"]
    try:
        repeatCalculation = str(input("would you like another calculation? y/n: "))
        if repeatCalculation == possible_answers[0]:
            data_collection()
        elif repeatCalculation == possible_answers[1]:
            data_collection()
        else:
            print("Goodbye!")
    except ValueError:
        print("yes or no?")


data_collection()