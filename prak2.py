def fibonacci(n):
    a, b = 0, 1
    hasil = []
    while a <= n:  # Loop terus berulang selama nilai a masih lebih kecil atau sama dengan n
        hasil.append(a)
        a, b = b, a + b  # Perbarui nilai a dan b untuk iterasi berikutnya
    return hasil

# Input nilai n dari pengguna
n = int(input("Masukkan nilai maksimum n untuk deret Fibonacci: "))

# Memanggil fungsi fibonacci dan mencetak hasilnya
print(f"Deret Fibonacci sampai {n}: {fibonacci(n)}")
