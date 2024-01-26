class Product:
    def __init__(self, id, name, price, category) :
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        difference = self.price * percent_change
        
        if is_increased == True:
            self.price += difference
        else:
            self.price -= difference
    def print_info(self):
        print(f"ID: {self.id}", f"NAME: {self.name}", f"COST: ${self.price}", f"CATEGORY: {self.category}")
    