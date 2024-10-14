# Function to find the largest of three numbers
def Angka_terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input from user
num1 = int(input("MASUKAN ANGKA KE 1: "))
num2 = int(input("MASUKAN ANGKA KE 2: "))
num3 = int(input("MASUKAN ANGKA KE 3: "))

# Call the function and store the result
terbesar = Angka_terbesar(num1, num2, num3)

# Print the largest number
print(f"The largest number is: {terbesar}")