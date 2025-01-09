import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w') as file:
                pass
        with open(self.__file_name, 'r') as file:
            return file.read().splitlines()

    def add(self, *products):
        current_products = self.get_products()
        with open(self.__file_name, 'a') as file:
            for product in products:
                if any(str(product) == line for line in current_products):
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{product}\n')
                    current_products.append(str(product))


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print("\n".join(s1.get_products()))
