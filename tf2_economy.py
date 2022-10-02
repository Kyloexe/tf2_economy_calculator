# Kyloexe
# This program is a calculator for the TF2 economy

# There are 4 different currencies. They are:
# Scrap Metal, Reclaimed Metal, Refined Metal and lastly, Keys
# The first three have fixed values, with a 3:1 ratio.
# So, 1 refined is 3 reclaimed, 3 reclaimed is 9 scrap

# Keys have a fluctualing value, changing with supply and demand in the economy, but a rough estimate is around 45 refined metal.

# Weapons drop every half-hour or so in game, each weapon is 0.5 scrap as you need 2 weapons to make 1 scrap metal

# The final ratio is 1:3:9:18

# IMPORTS
import math

# CONSTANTS
RECLAIMED_VALUE = 0.333
SCRAP_VALUE = 0.111
KEY_REFINED_VALUE = 45.22

def main(module_select_moved):
    if module_select_moved == 'melt':
        catch_melt = melt_keys()

        num_keys = catch_melt[0]
        num_refined = catch_melt[1]
        
        split_num_refined = math.modf(num_refined)

        refined = split_num_refined[1]

        scrap = split_num_refined[0] / 0.111

        print(f"From {num_keys} keys, you'll recieve {refined} refined metal and {math.ceil(scrap)} scrap metal")

    if module_select_moved == 'make':
        catch_make = make_keys()

        num_refined = catch_make[0]
        num_keys = catch_make[1]

        split_refined = math.modf(num_keys)
        spare_refined = split_refined[0] * KEY_REFINED_VALUE
        keys = split_refined[1] 

        print(f"From {num_refined} refined metal, you create {keys} keys, with {int(spare_refined)} refined left over")

def melt_keys():
    number_of_keys = int(input("How many keys do you want to smelt? "))

    print("~"*100)

    if number_of_keys < 0:
        print("ERROR: Number below 0, retry again")
        melt_keys()

    elif ValueError == True:
        print("ERROR: Not a number. Please retry")
        melt_keys()

    elif number_of_keys > 0:
        refined_total_keys = KEY_REFINED_VALUE * number_of_keys
        return number_of_keys , refined_total_keys
        

def make_keys():
    number_of_refined = int(input("How much refined metal do you have?: "))

    print("~"*100)

    if number_of_refined < 0:
        print("ERROR: Number below 0, try again")
        make_keys()

    elif number_of_refined > 0:
        keys_total_refined = number_of_refined / KEY_REFINED_VALUE
        return number_of_refined, keys_total_refined

def mode_select():
    print("~"*100)
    print("WELCOME TO VELAORION'S TF2 CALCULATOR!")
    print("~"*100)

    print("OPTIONS")
    print("~"*100)

    print("Melt keys = melt")
    print("Make Keys = make")
    print("~"*100)

    module_select = input("Please select one of the above options: ")

    main(module_select)


mode_select()



