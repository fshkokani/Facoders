<<<<<<< HEAD
# I have solved it in two ways, one using if and the other using the dictionary.
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

students =[s1[0], s2[0], s3[0]]

sum1=sum(s1[1:])
sum2=sum(s2[1:])
sum3=sum(s3[1:])

s={s1[0]: sum1, s2[0]: sum2, s3[0]: sum3}
name=input('Enter student name: ')
print('Student',name, s.get(name, 'is not recorded 0'))

if name in students:
    if name== 'Ahmad':
        print(name, sum1)
    if name== 'Sami':
        print(name, sum2)
    if name== 'Faris':
        print(name, sum3)
else:
    print('Student', name, 'is not recorded 0')
=======
# I have solved it in two ways, one using if and the other using the dictionary.
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

students =[s1[0], s2[0], s3[0]]

sum1=sum(s1[1:])
sum2=sum(s2[1:])
sum3=sum(s3[1:])

s={s1[0]: sum1, s2[0]: sum2, s3[0]: sum3}
name=input('Enter student name: ')
print('Student',name, s.get(name, 'is not recorded 0'))

if name in students:
    if name== 'Ahmad':
        print(name, sum1)
    if name== 'Sami':
        print(name, sum2)
    if name== 'Faris':
        print(name, sum3)
else:
    print('Student', name, 'is not recorded 0')
>>>>>>> 616385ba3703e92075edec956e1ab01ae65799f0
