import random

#main function that gets users grades and manages the overall flow of the program
def main():
    grades = []

    print("Welcome to the grade calculator!")
    while True:
        grade = int(input("Enter a grade (-1 to quit): "))
        if grade == -1:
            break
        grades.append(grade)

    print("Grades entered:", grades)

    lowest_removal(grades)
    random_removal(grades)
    grade_editing(grades)
    grade_sorter(grades)
    grade_average_and_total(grades)

#lowest grade removal function
def lowest_removal(grades):
    print("Now I'll remove your lowest grade.")
    if grades:
        lowest = min(grades)
        grades.remove(lowest)
    print("Updated grades:", grades)
    return grades

#random grade removal function
def random_removal(grades):
    print("Now I'll remove a random grade.")
    if grades:
        index_to_remove = random.randrange(len(grades))
        grades.pop(index_to_remove)
    print("Updated grades:", grades)
    return grades

#grade editing function
def grade_editing(grades):
    print("Now, entering a number will allow you to edit that grade.")
    while True:
        index = int(input(f"Enter the grade you'd like to edit (0 to {len(grades) - 1}, -1 to quit): "))
        if index == -1:
            break
        if 0 <= index < len(grades):
            new_grade = int(input(f"Enter the new value for grade {index}: "))
            grades[index] = new_grade
        else:
            print("Invalid index. Please try again.")
    print("Updated grades:", grades)
    return grades


#quick and simple sorter for grades
def grade_sorter(grades):
    print("Now I'll sort your grades in descending order.")
    grades.sort(reverse=True)
    print("Updated grades:", grades)
    return grades

#grade average and total calculation
def grade_average_and_total(grades):
    print("Now I'll calculate the average and total of your grades.")
    if grades:
        total = sum(grades)
        average = total / len(grades)
        print("Total grades:", total)
        print("Average grade:", average)
        print("Completed by Gregary Coplan")
        return total, average
    print("No grades to calculate.")
    return 0, 0
    

if __name__ == "__main__":
    main()