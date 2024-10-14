#mencetak deret fiboncci hingga #fibonacci adalah penjumlahan 2 bilangan sebelumnya
def fibonacci(n):
    a, b =0, 1
    hasil = []
    while a <= n:  #while: Kata kunci yang menandai awal dari loop.
        hasil.append(a)
        a, b =b, a + b
    return hasil
#input nilai n dari pengguna
n = int(input ("masukan nilai n; "))

#memanggil fungsi fibonacci dab mencetak hasilnya
print(f"deret fibonacci sampai {n}: {fibonacci(n)}")