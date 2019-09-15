class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return (self.x * no.x + self.y * no.y + self.z * no.z)

    def cross(self, no):
        a = self.absolute()
        b = no.absolute()
        return Points(self.y * no.z - self.z * no.y, self.x*no.z - no.x*self.z, self.x * no.y - no.x*self.y)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
