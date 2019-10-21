<<<<<<< HEAD
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

def students_names(grade):
    return grade.keys()

def student_score(grade,name):
    if name in grade:
        return sum(list(grade.get(name)))
    else:
        return ('student name is not listed')

def students_count(grade):
    return len(list(grade.keys()))

while True:
    choice1 = input ('Choose one: students_names, student_score, students_count: ')

    if choice1 == 'students_names' :
        grade = input ('Enter grade: ' )

        if grade == 'grade_one':
            print( students_names(grade_one) )
        elif grade == 'grade_two':
            print( students_names(grade_two) )
        elif grade == 'grade_three':
            print( students_names(grade_three) )
        else:
            print('grade is not listed' )

    elif choice1 == 'student_score' :
        grade = input ('Enter grade: ' )
        name = input ('Enter student name: ' )

        if grade == 'grade_one':
            print( student_score(grade_one,name) )
        elif grade == 'grade_two':
            print( student_score(grade_two,name) )
        elif grade == 'grade_three':
            print( student_score(grade_three,name) )
        else:
            print('grade not listed' )

    elif choice1 == 'students_count' :
        grade = input ('Enter grade: ' )

        if grade == 'grade_one':
            print( students_count(grade_one) )
        elif grade == 'grade_two':
            print( students_count(grade_two) )
        elif grade == 'grade_three':
            print( students_count(grade_three) )
        else:
            print('grade is not listed')

    else:
        print('Not in the choices')

    finish =input('Enter Done if you have finished or More to continue ')
    if finish== 'Done':
        break
    elif finish== 'More':
        continue
    else:
         input('Enter Done if you have finished or More to continue ')
=======
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

def students_names(grade):
    return grade.keys()

def student_score(grade,name):
    if name in grade:
        return sum(list(grade.get(name)))
    else:
        return ('student name is not listed')

def students_count(grade):
    return len(list(grade.keys()))

while True:
    choice1 = input ('Choose one: students_names, student_score, students_count: ')

    if choice1 == 'students_names' :
        grade = input ('Enter grade: ' )

        if grade == 'grade_one':
            print( students_names(grade_one) )
        elif grade == 'grade_two':
            print( students_names(grade_two) )
        elif grade == 'grade_three':
            print( students_names(grade_three) )
        else:
            print('grade is not listed' )

    elif choice1 == 'student_score' :
        grade = input ('Enter grade: ' )
        name = input ('Enter student name: ' )

        if grade == 'grade_one':
            print( student_score(grade_one,name) )
        elif grade == 'grade_two':
            print( student_score(grade_two,name) )
        elif grade == 'grade_three':
            print( student_score(grade_three,name) )
        else:
            print('grade not listed' )

    elif choice1 == 'students_count' :
        grade = input ('Enter grade: ' )

        if grade == 'grade_one':
            print( students_count(grade_one) )
        elif grade == 'grade_two':
            print( students_count(grade_two) )
        elif grade == 'grade_three':
            print( students_count(grade_three) )
        else:
            print('grade is not listed')

    else:
        print('Not in the choices')

    finish =input('Enter Done if you have finished or More to continue ')
    if finish== 'Done':
        break
    elif finish== 'More':
        continue
    else:
         input('Enter Done if you have finished or More to continue ')
>>>>>>> 616385ba3703e92075edec956e1ab01ae65799f0
