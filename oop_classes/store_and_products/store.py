class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        self.products.remove(self.products[id])
    def show_all_products(self):
        for product in self.products:
            product.print_info()
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        matching_products = [product for product in self.products if product.category == category]
        
        for product in matching_products:
            product.update_price(percent_discount, False)
