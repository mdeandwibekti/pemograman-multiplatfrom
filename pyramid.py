# Program to print a pyramid of numbers
def print_pyramid(n):
    for i in range(1, n+1):
        print((str(i) + " ") * i)

# Example usage
n = int(input("masukan angka ke n: "))
print_pyramid(n)