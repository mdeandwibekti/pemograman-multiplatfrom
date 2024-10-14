# Program to find the largest of three numbers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = (input("Enter third number: "))
print("The largest number is:", find_largest(a, b, c))
