class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.height * self.radius * self.radius


    def surface_area(self):
        return Cylinder.pi * self.radius * self.radius

c = Cylinder(2,3)
print(c.surface_area())
print(c.volume())