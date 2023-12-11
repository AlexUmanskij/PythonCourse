class quad:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def squad(self):
        return self.height*self.width

    def perimetr(self):
        return 2*(self.height+self.width)


a = quad(5, 2)
print(a.squad())
print(a.perimetr())
