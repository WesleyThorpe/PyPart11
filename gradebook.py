from typing import List, Dict
from enum import Enum
import uuid

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class person: 
    def __init__(x, first_name, last_name, dob): 
        x.first_name = first_name
        x.last_name = last_name
        x.dob = dob 
        x.alive = AliveStatus.Alive
    
def __str__(x):
    return f"{x.first_name} {x.last_name}"

def update_first_name(x,first_name):
    x.first_name = first_name

def update_last_name(x, last_name):
    x.last_name = last_name

def update_dob(x,dob):
    x.dob = dob
def update_status (x,alive:AliveStatus):
    x.alive = alive

class instructor(person):
    def __init__(x, first_name, last_name, dob):
        person. __init__(x,first_name,last_name, dob)
        x.instructor_id = f"Instructor_{uuid.uuid3()}"

class student(person): 
    def __init__(x, first_name, last_name, dob):
        person. __init__(x,first_name,last_name, dob)
        x.student_id = f"student_{uuid.uuid3()}"

class zip_code_student(student):
    def __init__(x, first_name, last_name, dob):
        student. __init__(x, first_name, last_name, dob)

class college(student): 
    def __init__(x, first_name, last_name, dob):
        student. __init__(x, first_name, last_name, dob)

class classroom:
    def __init__(x):
        x.students: dict[str,student] = {} 
        x.instructors: dict[str,instructor] = {} 
   
    def add_instructor(x, instructor: instructor):
        x.instructors[instructor.instructor_id] = instructor
    
    
    def remove_instructor(x, instructor: instructor ):
        if instructor.instructor_id in x.instructors:
            del x.instructors[instructor.instructor_id]

    
    def add_student(x, student:student):
        x.students[student.student_id] = student


    def remove_student(x, student:student):
        if student.student_id in x.students:
            del x.student[student.student_id]

    def print_instructors(x):
        for key, value in x.instructors.items():
            print(f"{key}: {value}")

    def print_students(x):
        for key, value in x.students.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    pass
