"""
------------------------------------------------------------
Professional Calculator - Utility Functions
------------------------------------------------------------
"""

from config import APP_NAME, VERSION, MENU_OPTIONS, LINE


def display_header():
    """Displays the application header."""

    print("\n")
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 60 + "║")
    print(f"║{'🧮 PROFESSIONAL CALCULATOR v' + VERSION:^60}║")
    print(f"║{'Developed by Niharika V':^60}║")
    print("║" + " " * 60 + "║")
    print("╚" + "═" * 60 + "╝")
 
 
def display_menu():
    """Displays the calculator menu."""

    print("\n📌 Mathematical Operations\n")

    print("[1]  Addition")
    print("[2]  Subtraction")
    print("[3]  Multiplication")
    print("[4]  Division")
    print("[5]  Modulus")
    print("[6]  Power")
    print("[7]  Square Root")
    print("[8]  Floor Division")
    print("[9]  Percentage")

    print("\n📁 History")

    print("[10] View History")
    print("[11] Clear History")
    print("[12] Save History")

    print("\n🚪 Exit")
    print("[13] Exit")

    print("\n" + LINE) 
 









def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= 13:
                return choice
            print("Please choose between 1 and 13.")
        except ValueError:
            print("Enter a valid menu number.")

def format_number(number):
    """
    Removes unnecessary .0 from whole numbers.
    """

    if isinstance(number, float) and number.is_integer():
        return int(number)

    return number