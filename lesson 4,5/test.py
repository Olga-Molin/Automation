class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a + self.b < self.c:
            print("это не треугольник")
        elif self.a == self.b == self.c:
            print("равносторонний")

        else:
            print("это треугольник")
            

triangle1 = Triangle(4, 5, 6)
triangle2 = Triangle(7, 7, 7)
triangle3 = Triangle(1, 6, 12) 

triangle1.is_triangle()
triangle2.is_triangle()
triangle3.is_triangle()