import matplotlib.pyplot as plt
import numpy as np

# Fungsi pertama: y = 3x + 4
def func1(x):
    return 3*x + 4

# Fungsi kedua: y = 2x^2 + 1
def func2(x):
    return 2*x**2 + 1

# Fungsi ketiga: y = x^3 + 3
def func3(x):
    return x**3 + 3

# Range x yang akan digunakan untuk membuat grafik
x = np.linspace(-5, 5, 100)

# Membuat grafik fungsi pertama
plt.plot(x, func1(x), label="y = 3x + 4")

# Membuat grafik fungsi kedua
plt.plot(x, func2(x), label="y = 2x^2 + 1")

# Membuat grafik fungsi ketiga
plt.plot(x, func3(x), label="y = x^3 + 3")

# Menambahkan judul dan label pada sumbu x dan y
plt.title("Grafik Beberapa Fungsi")
plt.xlabel("Nilai x")
plt.ylabel("Nilai y")

# Menampilkan legenda
plt.legend()

# Menampilkan grafik
plt.show()
