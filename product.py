class Product:
    def add_to_cart(self):
        self.id=int(input("Enter product ID:"))
        self.name=input("Enter product type:")
        self.price=int(input("Enter price:"))
    def display(self):
        print("---Product Details---")
        print("Product ID:",self.id,"\nProduct Type:",self.name,"\nPrice:",self.price)
class Electronics(Product):
    def electronics(self):
        super().add_to_cart()
        print("Electronics Details")
        self.pname=input("Enter product name:")
        self.brand=input("Enter brand:")
        self.warranty=input("Enter warranty:")
    def display(self):
        super().display()
        print("Product Name:",self.pname,"\nBrand:",self.brand,"\nWarranty:",self.warranty)
class Clothing(Product):
    def getcloth(self):
        super().add_to_cart()
        print("Cloth Details")
        self.type=input("Enter cloth type:")
        self.size=input("Enter cloth size:")
        self.color=input("Enter cloth color:")
    def display(self):
        super().display()
        print("Type:",self.type," \nSize:",self.size,"\nColor:",self.color)
E=Electronics()
C=Clothing()
E.electronics()
C.getcloth()
E.display()
C.display()
