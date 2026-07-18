import sys


def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart


def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"\nCaught Expected Error: {e}")
        print("Explanation: Tuples are immutable sequence structures.")
        print("Their internal memory elements cannot be reassigned after creation.")


def calculate_total(cart):
    raw_total = sum(item["price"] * item["qty"] for item in cart["items"])
    discount_multiplier = 1 - (cart["discount"] / 100)
    return round(raw_total * discount_multiplier, 2)


def run_bug_demonstration():
    print("\n--- Running Part A: Buggy Function Output ---")
    print(add_item_buggy("apple"))
    print(add_item_buggy("banana"))
    print(add_item_buggy("milk", cart=["bread"]))
    print(add_item_buggy("eggs"))

    print("\n--- Running Part B: Fixed Function Output ---")
    print(add_item_fixed("apple"))
    print(add_item_fixed("banana"))
    print(add_item_fixed("milk", cart=["bread"]))
    print(add_item_fixed("eggs"))


def main():
    print("Welcome! Let's explore mutable vs immutable behavior.")
    carts = {}

    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. Run Bug & Fix Demonstration (Part A & B)")
        print("2. Create New Customer Cart")
        print("3. Add Item to a Cart")
        print("4. Calculate Cart Total")
        print("5. Test Tuple Immutability Error")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            run_bug_demonstration()

        elif choice == "2":
            owner = input("Enter customer name: ").strip()
            if not owner:
                print("Name cannot be empty.")
                continue
            if owner in carts:
                print(f"A cart already exists for {owner}.")
                continue
            try:
                disc = float(input("Enter discount percentage (0-100): "))
                if not (0 <= disc <= 100):
                    print("Discount must be between 0 and 100.")
                    continue
            except ValueError:
                print("Invalid number for discount.")
                continue

            carts[owner] = create_cart(owner, disc)
            print(f"Success! Independent cart created for {owner}.")

        elif choice == "3":
            if not carts:
                print("No carts available. Create one first.")
                continue
            owner = input("Enter customer name: ").strip()
            if owner not in carts:
                print(f"No cart found for {owner}.")
                continue
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                qty = int(input("Enter item quantity: "))
                if price < 0 or qty <= 0:
                    print("Price must be positive and quantity must be at least 1.")
                    continue
            except ValueError:
                print("Invalid input values.")
                continue

            add_to_cart(carts[owner], name, price, qty)
            print(f"Added {qty}x '{name}' to {owner}'s cart.")

        elif choice == "4":
            if not carts:
                print("No active carts found.")
                continue
            owner = input("Enter customer name: ").strip()
            if owner not in carts:
                print(f"No cart found for {owner}.")
                continue

            cart = carts[owner]
            print(f"\n--- Receipt for {cart['owner']} ---")
            for item in cart["items"]:
                print(
                    f"- {item['qty']}x {item['name']} @ ${item['price']:.2f} each"
                )
            total = calculate_total(cart)
            print(f"Applied Discount: {cart['discount']}%")
            print(f"Total Amount Due: ${total:.2f}")

        elif choice == "5":
            print("\nTesting what happens when trying to modify a tuple...")
            dummy_tuple = (10.99, "USD")
            print(f"Initial tuple structure: {dummy_tuple}")
            update_price(dummy_tuple, 12.99)

        elif choice == "6":
            print("Thank you for exploring python object behaviors. Goodbye!")
            sys.exit()

        else:
            print("Invalid selection. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()

