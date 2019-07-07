class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):        
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        x = self.real
        y = self.imaginary
        u = no.real
        v = no.imaginary
        return Complex(x*u - y*v, x*v + y*u)

    def __truediv__(self, no):
        x = self.real
        y = self.imaginary
        u = no.real
        v = no.imaginary
        div = (u ** 2 + v ** 2)
        mod = no.mod()
        #return Complex((x*u - y*v), -1 * (x*v + y*u) / div)
        #return Complex(self.real, self.imaginary) * Complex(no.real, -1*no.imaginary)
        return Complex((x*u + y*v) / div, -1*(x*v - y*u) / div)
        
    def mod(self):
        return Complex(math.sqrt((self.real ** 2) + (self.imaginary ** 2)), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result