# Homework 01: Bakery Ordering System
subtotal = 0.0
while True:
    print("==============================")
    print("    WELCOME TO OUR BAKERY")
    print("==============================")
    print("1. Order Items")
    print("2. View Total")
    print("3. Checkout")
    print("4. Exit")
    print("==============================")
    option = input("Please select an option (1-4): ")
    if option == "1":
        print("==========BAKERY MENU=========")
        print("1. Croissant            $10.00")
        print("2. Chocolate Muffin      $2.50")
        print("3. Bread                 $2.00")
        print("4. Back to Main Menu")
        print("==============================")
        item = input("Please select an item (1-4): ")
        if item == "1":
            subtotal = subtotal + 10.00
            print("Croissant added successfully!")
            print(f"Current subtotal: ${subtotal:.2f}")
        elif item == "2":
            subtotal = subtotal + 2.50
            print("Chocolate Muffin added successfully!")
            print(f"Current subtotal: ${subtotal:.2f}")
        elif item == "3":
            subtotal = subtotal + 2.00
            print("Bread added successfully!")
            print(f"Current subtotal: ${subtotal:.2f}")
        elif item == "4":
            print("Back to Main Menu")
        else:
            print("Invalid item selection!")
            print("Subtotal remains unchanged.")
            print(f"Current subtotal: ${subtotal:.2f}")
    elif option == "2":
        print("==========YOUR ORDER==========")
        if subtotal == 0:
            print("Your order is empty.")
        else:
            print(f"Current subtotal: ${subtotal:.2f}")
    elif option == "3":
        print("===========CHECKOUT===========")
        if subtotal == 0:
            print("Your order is empty.")
            print("Please order something first.")
            continue
        if subtotal >= 10:
            discount = subtotal * 0.10
        else:
            discount = 0.0
        final_total = subtotal - discount
        print(f"Subtotal:            ${subtotal:.2f}")
        print(f"Discount (10%):      ${discount:.2f}")
        print("------------------------------")
        print(f"Final Total:         ${final_total:.2f}")
        cash = float(input("Enter cash received ($): "))
        if cash < 0:
            print("Invalid cash amount!")
        elif cash >= final_total:
            change = cash - final_total
            print("===========PAYMENT============")
            print(f"Final Total:         ${final_total:.2f}")
            print(f"Cash Received:       ${cash:.2f}")
            print(f"Change:              ${change:.2f}")
            subtotal = 0.0
        else:
            remaining = final_total - cash
            print("===========PAYMENT============")
            print("Insufficient Payment!")
            print(f"You need ${remaining:.1f} more.")
    elif option == "4":
        print("Thank you for visiting our bakery!")
        print("Have a wonderful day!")
        break
    else:
        print("Invalid option selection!")
        print("Please select a valid option (1-4).")
        continue