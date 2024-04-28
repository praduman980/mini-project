def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    score = float(input("Enter the score: "))
    grade = calculate_grade(score)
    print("The grade for the score", score, "is", grade)

if __name__ == "__main__":
    main()
