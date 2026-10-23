def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def get_valid_score(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 100:
                print("Score must be between 0 and 100.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if name == "":
            print("Name cannot be empty.")
            continue
        return name

def main():
    students = {}
    n = get_valid_int("How many students? ")

    for i in range(n):
        name = get_valid_name(f"Enter name of student {i+1}: ")
        score = get_valid_score(f"Enter {name}'s score: ")
        students[name] = score

    print("\n--- Grade Report ---")
    all_scores = list(students.values())

    for name, score in students.items():
        grade = assign_grade(score)
        print(f"{name}: {score} -> Grade {grade}")

    class_average = calculate_average(all_scores)
    print(f"\nClass Average: {class_average:.2f}")
    print(f"Class Average Grade: {assign_grade(class_average)}")

main()

