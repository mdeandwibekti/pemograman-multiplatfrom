# Program to print odd numbers up to n
def print_odd_numbers(n):   #def: Kata kunci yang digunakan untuk mendefinisikan sebuah fungsi.
    for i in range(1, n+1, 2):
        print(i, end=" ")

# Example usage
n = int(input("MASUKAN ANGKA KE n: "))
print("Odd numbers up to", n, "are:")
print_odd_numbers(n)