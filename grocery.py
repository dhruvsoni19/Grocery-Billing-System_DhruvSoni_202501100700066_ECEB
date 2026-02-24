total = 0

for i in range(5):
    print("\nItem", i+1)

    price = input("Enter price: ")
    while price.replace('.', '', 1).isdigit() == False:
        print("Invalid input")
        price = input("Enter price: ")
    price = float(price)

    qty = input("Enter quantity: ")
    while qty.isdigit() == False:
        print("Invalid input")
        qty = input("Enter quantity: ")
    qty = int(qty)

    total = total + (price * qty)

discount = 0
if total > 100:
    discount = total * 0.1

final_amount = total - discount

print("\n----- BILL SUMMARY -----")
print("Total =", total)
print("Discount =", discount)
print("Final Amount =", final_amount)