import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    # İki nokta arasındaki Öklid mesafesini hesaplar
    distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance

# Noktaları temsil eden liste
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafeleri saklamak için bir liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplayan döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # İki nokta arasındaki mesafeyi hesapla
        dist = euclideanDistance(points[i], points[j])
        # Mesafeyi distances listesine ekle
        distances.append(dist)

# distances listesindeki minimum mesafeyi bulun
minimum_distance = min(distances)

# Minimum mesafeyi yazdır
print("Minimum Öklid mesafesi:", minimum_distance)
