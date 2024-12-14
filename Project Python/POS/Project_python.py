
class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

class PointOfSale:
    def __init__(self):
        self.products = []

    def add_product(self, name, category, price, stock):
        product = Product(name, category, price, stock)
        self.products.append(product)
        print(f"Add Products : {name}")

    def list_products(self):
        print("Products List :")
        for product in self.products:
            print(f"{product.name} (Product Type : {product.category}), Price {product.price} Baht, Products in Stock: {product.stock} item")

    def sell_product(self, name, quantity):
        for product in self.products:
            if product.name == name:
                if product.stock >= quantity:
                    product.stock -= quantity
                    total_price = product.price * quantity
                    print(f"Sale Products : {name} x {quantity} Price {total_price} Baht")
                else:
                    print(f"Product {name} not enough in stock")
                return
        print(f"Not found products {name}")

if __name__ == "__main__":
    pos = PointOfSale()
    while True:
        print("\n")
        print("="*23)
        print(":      Main Menu      :")
        print("="*23)
        print(": 1. Add Products     :")
        print(": 2. Products List    :")
        print(": 3. Sale Products    :")
        print(": 4. Exit Program     :")
        print("="*23)

        choice = input("Please enter your choice : ")

        if choice == "1":
            name = input("Add Products : ")
            category = input("Products Type : ")
            price = float(input("Products Price : "))
            stock = int(input("Number of products in stock : "))
            pos.add_product(name, category, price, stock)
        elif choice == "2":
            pos.list_products()
        elif choice == "3":
            name = input("Name of products to be sold : ")
            quantity = int(input("Number of products to be sold : "))
            pos.sell_product(name, quantity)
        elif choice == "4":
            print("Exit Program. . .")
            break
        else:
            print("The products list is not incorrect.")
