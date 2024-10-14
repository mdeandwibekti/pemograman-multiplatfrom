# Program to evaluate student performance based on percentage
def evaluate_performance(percentage):
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Below average performance"

# Example usage
percentage = float(input("Enter the percentage: "))
print(evaluate_performance(percentage))