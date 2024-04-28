# Konumlarımız
points = [(40, 20), (10, 50),(7,15),(4,7)] 

# Öklid algoritma hesaplaması
def euclideanDistance(konum1, konum2):
    x1, y1 = konum1                                
    x2, y2 = konum2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) **0.5

# points dizimizin içindeki demetlerin aralarındaki mesafeyi tutar.
distances = []
for i in range(len(points)):                         
    for j in range(i+1, len(points)):
        _ = euclideanDistance(points[i], points[j])
        distances.append(_)

# En küçük değer
min_distance = min(distances)
print(f"En küçük mesafe: {min_distance}")     