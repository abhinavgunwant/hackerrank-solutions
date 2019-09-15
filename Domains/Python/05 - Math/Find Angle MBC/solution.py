import math
import cmath

ab, bc = int(input()), int(input())
comp = complex(bc, ab)
r,phi = cmath.polar(comp)
comp2 = cmath.rect(r/2, phi)
comp3 = complex(bc - comp2.real, comp2.imag)
r2,phi2 = cmath.polar(comp3)

print(str(int(round(math.degrees(phi2)))) + u'\u00b0')