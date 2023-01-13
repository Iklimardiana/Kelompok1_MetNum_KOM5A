import numpy as np #Memasukkan bundle NumPy ke dalam program untuk mempermudah perhitungan array
def my_bisection(g, a, b, e): #Mendefinisikan fungsi my_bisection
  #np.sign digunakan untuk mengembalikan sign atau tanda dari setiap elemen angka dalam sebuah array
  #artinya jika sign fungsi (g(a)) sama dengan sign fungsi (g(b)), maka...
  if np.sign(g(a)) == np.sign(g(b)):
    #kata "raise" biasanya digunakan untuk mengangkat sebuah exception atau error dan mencetaknya
    raise Exception('Tidak ada akar pada interval a dan b')
  #variabel m nantinya akan berisi hasil penjumlahan antara variabel a dan b; kemudian dibagi 2
  m = (a + b)/2 
  #np.abs digunakan untuk menghitung hasil yang absolut dari suatu Numpy Array
  #artinya jika hasil absolut fungsi g(m) lebih kecil dari e
  if np.abs(g(m)) < e:
    return m #maka akan mengembalikan nilai m
  #jika sign fungsi g(a) sama dengan sign fungsi g(m)
  elif np.sign(g(a)) == np.sign(g(m)): 
    #maka akan mengembalikan nilai fungsi my_bisection(g, m, b, e)
    return my_bisection(g, m, b, e)
  #jika sign fungsi g(b) sama dengan sign fungsi g(m)
  elif np.sign(g(b)) == np.sign(g(m)):
    #maka akan mengembalikan nilai fungsi my_bisection(g, a, m, e)
    return my_bisection(g, a, m, e) 

from numpy import *

# Definisi Matriks A
matA = [[6, -1, 2], [-4, -2, 3]]
matA = reshape(matA,(2,3))
print("Matriks A (2X3): \n", matA, "\n")

# Definisi Matriks B
matB = [[-4, 7, -3], [-1, -7, 6], [8, -5, 4]]
matB = reshape(matB,(3,3))
print("Matriks B (3X3): \n", matB, "\n")

# Definisi Matriks C
matC = [[-2, 4], [2, 5], [3, -6]]
matC = reshape(matC,(3,2))
print("Matriks C (3X2): \n", matC, "\n")

# Perkalian Matriks Menggunakan Perulangan FOR
# Perkalian Matriks A dan Matriks B
resultAB = [[0, 0, 0],
    [0, 0, 0]]

# ITERASI DARI BARIS MATRIKS A
for i in range(len(matA)):
   # ITERASI DARI KOLOM MATRIKS B
   for j in range(len(matB[0])):
       # ITERASI DARI BARIS MATRIKS B
       for k in range(len(matB)):
           resultAB[i][j] += matA[i][k] * matB[k][j]

print("Hasil Perkalian Matriks A dengan Matriks B (2X3):")
for r in resultAB:
  print(r)

# Perkalian Matriks B dan Matriks C
resultBC = [[0, 0],
    [0, 0],
    [0, 0]]

# ITERASI DARI BARIS MATRIKS B
for i in range(len(matB)):
   # ITERASI DARI KOLOM MATRIKS C
   for j in range(len(matC[0])):
       # ITERASI DARI BARIS MATRIKS C
       for k in range(len(matC)):
           resultBC[i][j] += matB[i][k] * matC[k][j]

print("\nHasil Perkalian Matriks B dengan Matriks C (3X2):")
for r in resultBC:
  print(r)

# Perkalian Matriks C dan Matriks A
resultCA = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

# ITERASI DARI BARIS MATRIKS C
for i in range(len(matC)):
   # ITERASI DARI KOLOM MATRIKS A
   for j in range(len(matA[0])):
       # ITERASI DARI BARIS MATRIKS A
    for k in range(len(matA)):
           resultCA[i][j] += matC[i][k] * matA[k][j]

print("\nHasil Perkalian Matriks C dengan Matriks A (3X3):")
for r in resultCA:
  print(r)

# Dengan bantuan numpy, merubah gaya matriks agar benar-benar terlihat seperti matriks
from numpy import *

A = [[1, 2, 0],
    [2, 2, 1],
    [0, 3, 3]]

B = [[-1, 5],
    [3, 1],
    [0, 1]]

# VARIABEL result DIBUAT UNTUK MENYIMPAN HASIL PERKALIAN DARI MATRIKS A DENGAN MATRIKS B
# VARIABEL result MEMBENTUK MATRIKS 3X2
result_multiply = [[0, 0],
    [0, 0],
    [0, 0]]

print("=== NOMOR 1 MENAMPILKAN MATRIKS A DAN MATRIKS B ===")
# MENAMPILKAN MATRIKS A
A = reshape(A,(3,3)) 
print("Matriks A (3X3): \n", A)

# MENAMPILKAN MATRIKS B
B = reshape(B,(3,2)) 
print("\nMatriks B (3X2): \n", B)

# === NOMOR 2 MELAKUKAN PERKALIAN MATRIKS A DENGAN MATRIKS B ===
# PERKALIAN MATRIKS - DILAKUKAN DENGAN PERULANGAN FOR
# ITERASI DARI BARIS MATRIKS A
for i in range(len(A)):
    # ITERASI DARI KOLOM MATRIKS B
   for j in range(len(B[0])):
       # ITERASI DARI BARIS MATRIKS B
       for k in range(len(B)):
           result_multiply[i][j] += A[i][k] * B[k][j]

print("\n=== NOMOR 3 MENAMPILKAN PERKALIAN DAN PENJUMLAHAN MATRIKS A DENGAN MATRIKS B ===")
# MENAMPILKAN HASIL PERKALIAN MATRIKS A DENGAN MATRIKS B
print("Hasil Perkalian Matriks A dan Matriks B (3X2):")
for r in result_multiply:
  print(r)

# MENAMPILKAN HASIL PENJUMLAHAN MATRIKS A DENGAN MATRIKS B
print("\nHasil Penjumlahan Matriks A dan Matriks B:")
try :
  result_sum = [[A[i][j] + B[i][j]
    for j in range(len(A[0]))]
      for i in range(len(A))]
  for r in result_sum:
   print(r)
except IndexError:
  print("ERROR : List index out of range")
  print("Kedua matriks tidak memiliki ordo yang sama. Maka penjumlahan antara kedua matriks tidak dapat dilakukan")