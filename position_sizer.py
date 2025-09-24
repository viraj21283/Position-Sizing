# position_sizer.py
# Position Sizing Script for Trading/Investing
# Made with ♥ by Viraj Shah

"""
Standard Disclaimer:
This script is for educational purposes only. It does not constitute financial advice.
Please consult a qualified financial advisor before making investment decisions.
"""

import sys

def calc_position_size(capital, risk, entry_price, stop_loss_price):
    """
    Calculate position size based on risk.
    Args:
        capital (float): Total available capital.
        risk (float): Amount willing to risk (in currency units).
        entry_price (float): Price at which position is entered.
        stop_loss_price (float): Price at which position is exited if trade goes wrong.
    Returns:
        int: Number of units/shares/contracts to trade.
    """
    risk_per_unit = abs(entry_price - stop_loss_price)
    if risk_per_unit == 0:
        print("Error: Entry Price and Stop Loss Price cannot be the same.")
        sys.exit(1)
    position_size = risk / risk_per_unit
    return int(position_size)

def main():
    print("Welcome to the Position Sizing Calculator!")
    try:
        capital = float(input("Enter your total capital (e.g., 100000): "))
        risk_type = input("Choose risk input type: [A]bsolute [P]ercentage of Capital [PR] Previous Profit %: ").strip().upper()

        if risk_type == 'A':
            risk = float(input("Enter amount you are willing to risk (in currency units): "))
        elif risk_type == 'P':
            risk_percent = float(input("Enter risk percentage (e.g., 2 for 2%): "))
            risk = (risk_percent / 100) * capital
        elif risk_type == 'PR':
            previous_profit = float(input("Enter previous realized profit (in currency units): "))
            risk_percent = float(input("Enter risk percentage of previous profit (e.g., 50 for 50%): "))
            risk = (risk_percent / 100) * previous_profit
        else:
            print("Invalid risk type entered.")
            sys.exit(1)

        entry_price = float(input("Enter entry price for the position: "))
        stop_loss_price = float(input("Enter stop loss price: "))

        position_size = calc_position_size(capital, risk, entry_price, stop_loss_price)

        print("\nResult:")
        print(f"Position Size: {position_size} units")
        print(f"Capital: {capital}")
        print(f"Risk Amount: {risk}")
        print(f"Entry Price: {entry_price}")
        print(f"Stop Loss Price: {stop_loss_price}")
        print("Made with \u2665 by Viraj Shah")
        print("Disclaimer: This script is for educational purposes only and does not constitute financial advice.")
    except Exception as e:
        print(f"Error: {e}\nPlease enter valid numeric inputs.")

if __name__ == "__main__":
    main()
