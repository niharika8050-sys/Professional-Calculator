"""
------------------------------------------------------------
Professional Calculator
Main Controller
------------------------------------------------------------
Author : Niharika V
Version: 1.0
------------------------------------------------------------
"""

from calculator_engine import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    square_root,
    floor_division,
    percentage,
)

from utils import (
    display_header,
    display_menu,
    get_number,
    get_choice,
    format_number,
)

from history import (
    add_history,
    view_history,
    clear_history,
    save_history,
)

# Dictionary for all two-number operations
OPERATIONS = {
    1: ("Addition", "+", add),
    2: ("Subtraction", "-", subtract),
    3: ("Multiplication", "×", multiply),
    4: ("Division", "÷", divide),
    5: ("Modulus", "%", modulus),
    6: ("Power", "^", power),
    8: ("Floor Division", "//", floor_division),
    9: ("Percentage", "%", percentage),
}


def show_result(title, expression, answer):
    """Displays calculation result in a professional format."""

    print("\n" + "=" * 60)
    print(f"{('🧮 ' + title.upper()):^60}")
    print("=" * 60)

    print("\n" + "─" * 60)
    print("✅ CALCULATION SUCCESSFUL")
    print("─" * 60)

    print(f"\nExpression : {expression}")
    print(f"Answer     : {answer}")

    print("─" * 60)


def main():
    """Main Application Loop"""

    while True:

        display_header()
        display_menu()

        choice = get_choice()

        # ================= EXIT =================
        if choice == 13:

            print("\n")
            print("╔" + "═" * 60 + "╗")
            print(f"║{'Thank you for using Professional Calculator!':^60}║")
            print(f"║{'Have a productive day! 🚀':^60}║")
            print("╚" + "═" * 60 + "╝")

            break

        # ================= VIEW HISTORY =================
        elif choice == 10:

            view_history()
            input("\nPress Enter to continue...")
            continue

        # ================= CLEAR HISTORY =================
        elif choice == 11:

            clear_history()
            input("\nPress Enter to continue...")
            continue

        # ================= SAVE HISTORY =================
        elif choice == 12:

            save_history()
            input("\nPress Enter to continue...")
            continue

        # ================= SQUARE ROOT =================
        elif choice == 7:

            number = get_number("Enter number : ")

            try:

                result = square_root(number)

                number = format_number(number)
                result = format_number(result)

                show_result(
                    "Square Root",
                    f"√{number}",
                    result,
                )

                add_history(f"√{number} = {result}")

            except ValueError as error:

                print(f"\n❌ Error : {error}")

            input("\nPress Enter to continue...")
            continue

        # ================= ALL OTHER OPERATIONS =================
        elif choice in OPERATIONS:

            operation_name, symbol, operation = OPERATIONS[choice]

            first_number = get_number("Enter first number : ")
            second_number = get_number("Enter second number : ")

            try:

                result = operation(first_number, second_number)

                first_number = format_number(first_number)
                second_number = format_number(second_number)
                result = format_number(result)

                expression = f"{first_number} {symbol} {second_number}"

                show_result(
                    operation_name,
                    expression,
                    result,
                )

                add_history(
                    f"{expression} = {result}"
                )

            except Exception as error:

                print(f"\n❌ Error : {error}")

            input("\nPress Enter to continue...")
            continue

        else:

            print("\n❌ Invalid Choice")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()