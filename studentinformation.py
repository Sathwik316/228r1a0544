from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
class Student:
    def _init_(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.unit_test_scores = []
        self.records_submitted = 0

    def add_unit_test_score(self, score):
        self.unit_test_scores.append(score)

    def submit_record(self):
        self.records_submitted += 1

    def display_info(self):
        print(f"Student InformationSystem\nName: {self.name}\nRoll Number: {self.roll_number}")
        print(f"Unit Test Scores: {', '.join(map(str, self.unit_test_scores))}")
        print(f"Records Submitted: {self.records_submitted}\n")


class StudentInformationSystem:
    def _init_(self):
        self.students = {}

    def add_student(self, name, roll_number):
        if roll_number not in self.students:
            self.students[roll_number] = Student(name, roll_number)
            print(f"Student {name} with Roll Number {roll_number} added successfully.")
        else:
            print(f"Student with Roll Number {roll_number} already exists.")

    def add_unit_test_score(self, roll_number, score):
        if roll_number in self.students:
            student = self.students[roll_number]
            student.add_unit_test_score(score)
            print(f"Unit test score {score} added for {student.name} (Roll Number: {roll_number}).")
        else:
            print(f"Student with Roll Number {roll_number} not found.")

    def submit_record(self, roll_number):
        if roll_number in self.students:
            student = self.students[roll_number]
            student.submit_record()
            print(f"Record submitted for {student.name} (Roll Number: {roll_number}).")
        else:
            print(f"Student with Roll Number {roll_number} not found.")

    def display_student_info(self, roll_number):
        if roll_number in self.students:
            self.students[roll_number].display_info()
        else:
            print(f"Student with Roll Number {roll_number} not found.")


# Example usage:
sis = StudentInformationSystem()

sis.add_student("Ssthwik", "228R1A0544")
sis.add_student("S", "228R1A0544")