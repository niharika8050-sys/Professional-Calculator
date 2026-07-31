"""
------------------------------------------------------------
Professional Calculator - History Manager
------------------------------------------------------------
Handles calculation history.
------------------------------------------------------------
"""

from config import HISTORY_FILE
from datetime import datetime

history = []


def add_history(record: str):
    """Adds a calculation with timestamp."""

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    history.append({
        "time": current_time,
        "record": record
    })


def view_history():
    """Displays calculation history."""

    if not history:
        print("\n⚠️ No calculations have been performed yet.")
        return

    print("\n" + "=" * 65)
    print("📜 CALCULATION HISTORY".center(65))
    print("=" * 65)

    for index, item in enumerate(history, start=1):

        print(f"\n#{index}")
        print(f"🕒 {item['time']}")
        print(f"🧮 {item['record']}")
        print("-" * 65)
        print("=" * 65)
        print(f"Total Calculations : {len(history)}")
        print("=" * 65)

def clear_history():
    """Clears all stored calculations."""

    history.clear()

    print("\n🗑️ Calculation history cleared successfully.")




def save_history():
    """Saves history to a text file."""

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write("PROFESSIONAL CALCULATOR HISTORY\n")
        file.write("=" * 70 + "\n\n")

        for item in history:

            file.write(f"Time   : {item['time']}\n")
            file.write(f"Record : {item['record']}\n")
            file.write("-" * 70 + "\n")

    print(f"\n✅ History successfully saved to '{HISTORY_FILE}'")



