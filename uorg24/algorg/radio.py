import math


def circle_intersection_area(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d >= r1 + r2:
        return -1  # Çemberler kesişmiyor
    elif d <= abs(r2 - r1):
        # Bir çember diğerinin içinde
        return math.pi * min(r1, r2)**2
    else:
        # Kesişim alanını hesapla
        term1 = r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        term2 = r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
        term3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
        return term1 + term2 - term3

# Çemberlerin koordinatları ve yarıçapları
x1, y1, r1 = map(float, input("").split())
x2, y2, r2 = map(float, input("").split())

# Her iki çemberin alanlarını hesapla
alan1 = math.pi * r1**2
alan2 = math.pi * r2**2

# Kesişim alanını hesapla
kesisim_alani = circle_intersection_area(x1, y1, r1, x2, y2, r2)

# Birleşim alanını hesapla (kesişim alanını çıkartarak)
birlesim_alani = alan1 + alan2 - kesisim_alani

print(round(birlesim_alani, 2))
