def user_cart(products, cart):
    product_name = input("Enter the name of the product: ").lower()
    if product_name == "end":
        exit(0)
    product_count = int(input("Enter the quantity: "))

    for product in products:
        if product["name"] == product_name:
            if product["count"] >= product_count:
                product["count"] -= product_count
                product_to_add = {"name": product_name, "price": product["price"], "count": product_count}
                cart.append(product_to_add)
                print(product_count, product_name, "added to the cart")
                return True
            else:
                print("We have only", product['count'], product['name'])
                return False
    else:
        print("The product is not available")


def calculate_total(cart):
    total = 0
    for i in cart:
        total += i['price'] * i['count']
    if total == 0:
        exit(0)
    return total


def user_payment(total_price):
    while True:
        payment = int(input("Enter the payment amount: "))
        if payment != total_price:
            print('Please enter a valid amount')
        else:
            print('Payment received')
            return payment


def update_cart(cart, product_name, products):
    user_type = input("Are you a 'buyer' or a 'seller' ? ").lower()

    if user_type == "buyer":
        for i in cart:
            if i["name"] == product_name:
                new_count = int(input("Enter the new quantity: "))
                if new_count == 0:
                    cart.remove(i)
                else:
                    i["count"] = new_count
                return True

        print("The product is not in your cart")
        return False

    elif user_type == "seller":
        for product in products:
            if product["name"] == product_name:
                product["count"] += int(input("Enter the new quantity: "))
                return True

        add_product = input("Do you want to add this product to the list? 'yes', 'no'").lower()
        if add_product == "yes":
            price = int(input("Enter the price: "))
            count = int(input("Enter the quantity: "))
            products.append({"name": product_name, "count": count, "price": price})
            return True

        print("The product is not in the product list")
        return False


products = [
    {'name': 'book1', 'count': 5, 'price': 124000},
    {'name': 'book2', 'count': 15, 'price': 119700},
    {'name': 'book3', 'count': 23, 'price': 159300},
    {'name': 'book4', 'count': 50, 'price': 160000},
    {'name': 'book5', 'count': 2, 'price': 200000}
]
cart = []
while True:
    user_input = input("Do you want to 'add' a product, 'update' or 'end' the program: ").lower()
    if user_input == "end":
        break
    elif user_input == "update":
        product_name = input("Enter the name of the product you want to update: ").lower()
        update_cart(cart, product_name, products)
    else:
        user_cart(products, cart)
    print("Cart: ", cart)
    print(products)

total_price = calculate_total(cart)
print('Total price: {}T'.format(total_price))

payment = user_payment(total_price)
print('{}T is paid'.format(total_price))
