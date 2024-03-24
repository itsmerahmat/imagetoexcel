import cv2
import pandas as pd

# Membaca gambar "kucing.jpg" dan menyimpannya dalam variabel "image"
image = cv2.imread("./img/kucing.jpg")

# Mengubah gambar ke skala abu-abu (grayscale)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Membuat dataframe dari gambar skala abu-abu
df = pd.DataFrame(grayImage)

# Menyimpan dataframe ke dalam file Excel
df.to_excel("./excel/grayscaleImage.xlsx", index=False, header=False)