import cv2
import numpy as np

# Load gambar
image = cv2.imread('image_1.jpg')

# Konversi ke HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Tentukan rentang warna hijau dalam HSV
lower_green = np.array([40, 40, 40])
upper_green = np.array([70, 255, 255])

# Buat mask untuk warna hijau
mask = cv2.inRange(hsv, lower_green, upper_green)

# Cari kontur dalam mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Hitung jumlah kontur (jumlah kotak hijau)
jumlah_kotak_hijau = len(contours)
print("Jumlah objek hijau:", jumlah_kotak_hijau)

# Visualisasi kontur
cv2.drawContours(image, contours, -1, (255, 0, 0), 3)

# Tampilkan gambar dengan kontur
cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
cv2.imshow('Contours', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
