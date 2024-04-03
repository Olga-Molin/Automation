class Salat:
    def __init__(self, add = None):
        self.add = add
        

    def show_my_salat(self):
        if self.add == None:
            print("Салат без добавки") 
        else:
            print("Салат с добавкой " + self.add)


my_salat1 = Salat()
my_salat2 = Salat("укроп")
my_salat3 = Salat("перчик")

my_salat1.show_my_salat()
my_salat2.show_my_salat()
my_salat3.show_my_salat()
      
     
  