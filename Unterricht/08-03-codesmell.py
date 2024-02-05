def calculate_total_price(quantity, price):
    tax_rate = 0.1
    discount_rate = 0.05

    subtotal = quantity * price
    tax = subtotal * tax_rate
    discount = subtotal * discount_rate

    total_price = subtotal + tax - discount

    print("Total price:", total_price)

# Main code
calculate_total_price(10, 20)

def calculate_total_price2(quantity, price):
    tax_rate = 0.1
    discount_rate = 0.05

    subtotal = calculate_subtotal(quantity, price)
    tax = calculate_tax(subtotal, tax_rate)
    discount = calculate_discount(subtotal, discount_rate)

    total_price = subtotal + tax - discount

    print("Total price:", total_price)

def calculate_subtotal(quantity, price):
    return quantity * price

def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate

def calculate_discount(subtotal, discount_rate):
    return subtotal * discount_rate

# Main code
calculate_total_price(10, 20)
