price = input("What is the price of the product(without discount)? ")
discount = input("What is the discount of the product? ")
discount_price = int(price) * int(discount) / 100
print ("The money that you save is", discount_price, "$.")
final_price = int(price) - discount_price
print ("The price that you will have to pay after the discount is", final_price, "$.")