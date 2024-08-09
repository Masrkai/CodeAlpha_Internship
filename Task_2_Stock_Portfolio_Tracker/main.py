from portfolio import Portfolio
from ANSII import ANSIColor

def sep():
    print("----------------------")

def INVALID():
    inv="Invalid choice. Please try again."
    invc=ANSIColor.format_text(inv, color='white', bg_color='bright_red', style='bold')
    print(f"{invc}")

def menu():
    x2="1) Add Stock."
    x2C=ANSIColor.format_text(x2, color='green', bg_color='bright_white', style='bold')
    x3="2) View Portfolio Value."
    x3C=ANSIColor.format_text(x3, color='bright_yellow', bg_color='bright_white', style='bold')
    x4="3) Remove Stock."
    x4C=ANSIColor.format_text(x4, color='red', bg_color='bright_white', style='bold')
    x5="4) Exit."
    x5C=ANSIColor.format_text(x5, color='red', bg_color='bright_white', style='bold')
    print(f"{x2C}\n{x3C}\n{x4C}\n{x5C}")
    sep()

def main():
    portfolio = Portfolio()

    x1="\n>>>>>Stock Portfolio Tracker<<<<<"
    x1C=ANSIColor.format_text(x1, color='magenta', style='bold')
    print(f"{x1C}\n")

    while True:
        menu()

        choice = input("Enter choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
            print(f"Added {shares} shares of {symbol} to portfolio.")
            sep()


        elif choice == '2':
            value = portfolio.get_portfolio_value()
            print(f"Total Portfolio Value: ${value:.2f}")
            sep()


        elif choice == '3':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(symbol, shares)
            print(f"Removed {shares} shares of {symbol} from portfolio.")
            sep()

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            INVALID()

if __name__ == "__main__":
    main()