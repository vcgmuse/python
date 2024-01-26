from store import Store
from product import Product

class Walmart(Store):
    product_ids = 0
    def __init__(self, name):
        super().__init__(name)
    def update_product_id(cls):
        cls.product_ids += 1
        return cls.product_ids
san_antonio = Walmart('Wal-Mart')

san_antonio.add_product(Product(san_antonio.update_product_id(), "Cake", 5.00, "Bakery"))
san_antonio.add_product(Product(san_antonio.update_product_id(), "Donuts", 1.50, "Bakery"))
san_antonio.add_product(Product(san_antonio.update_product_id(), "Muffins", 2.50, "Bakery"))
san_antonio.show_all_products()
san_antonio.sell_product(1)
san_antonio.show_all_products()
san_antonio.inflation(.1)
san_antonio.show_all_products()
san_antonio.set_clearance("Bakery", .5)
san_antonio.set_clearance("Bakery", .5)
san_antonio.show_all_products()