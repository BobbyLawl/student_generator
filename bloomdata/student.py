'''
This module will be used to generate random students using several
pre-defined features.
'''

import random

eye_color = ["blue", "pink", "orange", "green", "red", "brown"]

foods = ["pineapple cake", "pizza", "cheesesteak", "apple pie",
         "seafood boil", "turkey dinner"]

names = ["Ben", "Annie", "Billy", "Katrina", "Daniel", "Rebecca",]

bloomtech = ["Data Science", "Web Development"]


class Student:
    '''
    This is the parent class, Student. It contains attributes
    and two associated methods.
    '''
    def student_intro():
        name = random.choice(names)
        eyes = random.choice(eye_color)
        food = random.choice(foods)

        print(f"This is {name} they have {eyes} eyes and\
              their favorite food is {food}.")

    print(student_intro())
    print(student_intro())
    print(student_intro())

    def GPA_response():
        gpa = round(random.uniform(2.0, 3.9), 1)
        name = random.choice(names)

        if gpa <= 3.2:
            print(f"{name} has a GPA score of {gpa},\
                  they're working on improving.")

        if gpa >= 3.3:
            print(f"{name} has a GPA score of {gpa}, they're doing great!")

    print(GPA_response())
    print(GPA_response())
    print(GPA_response())


class BloomTechStudent:
    '''
    This is a child of the Student class
    '''
    def student_intro():
        name = random.choice(names)
        eyes = random.choice(eye_color)
        food = random.choice(foods)

        print(f"This is {name} they have {eyes}\
              eyes and their favorite food is {food}.")

    print(student_intro())
    print(student_intro())
    print(student_intro())

    def generic_gpa():
        gpa = round(random.uniform(2.0, 3.9), 1)

        if gpa <= 3.2:
            print(f"Their GPA score is {gpa}, they're working on improving.")

        if gpa >= 3.3:
            print(f"Their GPA score is {gpa}, they're doing great!")

    def bloomtech_student():
        student = random.choice(bloomtech)
        print(f"They're pursuing {student} at Bloomtech Institute")

    print(bloomtech_student())
    print(bloomtech_student())
    print(bloomtech_student())

    print(student_intro(), bloomtech_student(), generic_gpa())

    num_students = int

    def student_generator(num_students):
        student_list = []
        name = random.choice(names)
        eyes = random.choice(eye_color)
        food = random.choice(foods)

        x = print(f"This is {name} they have {eyes} eyes and their favorite food is {food}.")

        for items in range(num_students):
            student_list.append(x)

    print(student_generator(30))
