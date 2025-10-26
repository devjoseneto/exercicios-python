def get_input(index):
    while True:
        try:
            grade = float(input(f'Enter grade #{index}: '))
            if 0 <= grade <= 10:
                return grade
            else:
                print('Grade must be between 0 and 10.')
        except ValueError:
            print('Please enter a valid number.')

grades = [get_input(i) for i in range(1, 5)]

def calculate_average(*grades):
    return sum(grades) / len(grades)

print(f"Average grade: {calculate_average(*grades):.2f}")