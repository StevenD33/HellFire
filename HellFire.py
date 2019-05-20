# Import the necessary packages
# from consolemenu import *
# from consolemenu.items import *
from Audit import audit
from Basic_Hardening import basic_hardening
# Create the menu
# menu = ConsoleMenu("Hellfire")

# # Create some items
# # A CommandItem runs a console command

# audit_item = CommandItem("Run Audit on your system",  "python Audit.py",)
# basic_hardening_item = CommandItem("Run Basic Hardening on your system",  "python Basic_Hardening.py")
# advanced_hardening_item = CommandItem("Run Advanced Hardening on your system",  "python Advanced_Hardening.py")
# personalised_hardening_item = CommandItem("Run Personalised Hardening on your system",  "python Personalised_Hardening.py")

# function_item = FunctionItem("Call a Python function",audit)

# # A SelectionMenu constructs a menu from a list of strings
# selection_menu = SelectionMenu(["item1", "item2", "item3"])

# # A SubmenuItem lets you add a menu (the selection_menu above, for example)
# # as a submenu of another menu
# submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# # Once we're done creating them, we just add the items to the menu
# menu.append_item(audit_item)
# menu.append_item(basic_hardening_item)
# menu.append_item(advanced_hardening_item)
# menu.append_item(personalised_hardening_item)
# menu.append_item(submenu_item)
# menu.append_item(function_item)

# menu.show()


import sys, os

# Main definition - constants
menu_actions  = {}  

# Main menu
def main_menu():
    os.system('clear')
    print (" ('-. .-.   ('-.                                       _  .-')     ('-.   ")
    print ("( OO )  / _(  OO)                                     ( \( -O )  _(  OO)  ")
    print (",--. ,--.(,------.,--.      ,--.        ,------.,-.-') ,------. (,------. ")
    print ("|  | |  | |  .---'|  |.-')  |  |.-') ('-| _.---'|  |OO)|   /`. ' |  .---' ")
    print ("|   .|  | |  |    |  | OO ) |  | OO )(OO|(_\    |  |  \|  /  | | |  |     ")
    print ("|       |(|  '--. |  |`-' | |  |`-' |/  |  '--. |  |(_/|  |_.' |(|  '--.  ")
    print ("|  .-.  | |  .--'(|  '---.'(|  '---.'\_)|  .--',|  |_.'|  .  '.' |  .--'  ")
    print ("|  | |  | |  `---.|      |  |      |   \|  |_)(_|  |   |  |\  \  |  `---. ")
    print ("`--' `--' `------'`------'  `------'    `--'    `--'   `--' '--' `------' ")
    print ("Welcome,\n")
    print ("1. Run Audit on your system")
    print ("2. Run Basic Hardening on your system")
    print ("3. Run Advanced Hardening on your system")
    print ("4. Run Personalised Hardening on your system")
    print ("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    audit()


# Menu 2
def menu2():
    basic_hardening()

def menu3():
    print ("Hello Menu 2 !\n")
    choice = input(" >>  ")
    exec_menu(choice)
    return
def menu4():
    print ("Hello Menu 2 !\n")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()


# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}


# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()