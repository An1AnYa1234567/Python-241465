# Write a program to demonstrate Custom Flexible Student Grade & Statistics Calculator.
# Calculate performance scores using *args and **kwargs
def calculate_scores(*args, **kwargs):
    if not args:
        return 0, 0, 0, {}

    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)

    # Calculate letter grade distribution
    grades = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for score in args:
        if score >= 90:
            grades["A"] += 1
        elif score >= 80:
            grades["B"] += 1
        elif score >= 70:
            grades["C"] += 1
        elif score >= 60:
            grades["D"] += 1
        else:
            grades["F"] += 1

    print("\nStudent:", kwargs.get("name", "Unknown"))
    print("Class:", kwargs.get("class_name", "Not specified"))

    return minimum, maximum, average, grades


# Assessment scores
result = calculate_scores(
    95, 82, 76, 60, 45,
    name="Ananya",
    class_name="BTech CSE"
)

# Tuple unpacking
minimum, maximum, average, distribution = result

print("\nMinimum Score:", minimum)
print("Maximum Score:", maximum)
print("Average Score:", round(average, 2))
print("Grade Distribution:", distribution)