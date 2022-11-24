'''
    NAMA : ALYA ARTHAMEVIA SOLEHUDDIN
    NIM : 2000527
    KELAS : KOM-5A
    TANGGAL PENGERJAAN NOMOR 2 : RABU, 07 SEPTEMBER 2022
'''

import numpy as np
from numpy import *

# SOAL NOMOR 2
# Definisi Matriks A
'''matA = [[6, -1, 2], [-4, -2, 3]]'''
matA = [6, -1, 2, -4, -2, 3]
matA = reshape(matA,(2,3))
print("Matriks A : \n", matA, "\n")

# Definisi Matriks B
matB = [[-4, 7, -3], [-1, -7, 6], [8, -5, 4]]
matB = reshape(matB,(3,3))
print("Matriks B : \n", matB, "\n")

# Definisi Matriks C
matC = [[-2, 4], [2, 5], [3, -6]]
matC = reshape(matC,(3,2))
print("Matriks C : \n", matC, "\n")

# Perkalian matA dan matB
print("Hasil Perkalian Matriks A dan Matriks B :")
print(np.dot(matA, matB), "\n")

# Perkalian matB dan matC
print("Hasil Perkalian Matriks B dan Matriks C :")
print(np.dot(matB, matC), "\n")

# Perkalian matC dan matA
print("Hasil Perkalian Matriks C dan Matriks A :")
print(np.dot(matC, matA))

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