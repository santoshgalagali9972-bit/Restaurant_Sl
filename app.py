def show_menu():
    print("\n===== RESTAURANT MENU =====")
    print("1. Burger - Rs.120")
    print("2. Pizza - Rs.250")
    print("3. Pasta - Rs.180")
    print("4. Sandwich - Rs.90")
    print("5. Coffee - Rs.60")
    print("===========================")


def take_order():
    menu = {
        1: ("Burger", 120),
        2: ("Pizza", 250),
        3: ("Pasta", 180),
        4: ("Sandwich", 90),
        5: ("Coffee", 60)
    }

    show_menu()

    order = []
    total = 0

    while True:
        choice = input("\nEnter item number (0 to finish): ")

        if choice == "0":
            break

        if not choice.isdigit() or int(choice) not in menu:
            print("Invalid choice. Try again.")
            continue

        item_no = int(choice)

        qty = input(f"Enter quantity for {menu[item_no][0]}: ")

        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity.")
            continue

        qty = int(qty)
        name, price = menu[item_no]
        cost = price * qty

        order.append((name, qty, price, cost))
        total += cost

        print(f"Added: {name} x {qty} = Rs.{cost}")

    if order:
        print("\n======= ORDER BILL =======")
        print("Item        Qty   Price   Cost")

        for name, qty, price, cost in order:
            print(f"{name:<12}{qty:<6}Rs.{price:<6}Rs.{cost}")

        print("--------------------------")
        print(f"GRAND TOTAL: Rs.{total}")
        print("Thank you for your order!")
    else:
        print("No items ordered.")


if __name__ == "__main__":
    take_order()