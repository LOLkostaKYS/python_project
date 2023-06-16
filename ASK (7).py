product_price = input("What is the price of the product without taxes? ")
taxes = input("What is the percentage (%) of the taxes? ")
product_taxes = int(product_price) * int(taxes) / 100
final_price = int(product_price) + int(product_taxes)
print ("The price of the product after taxes is", final_price, "$.")