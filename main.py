from discipline_module import Discipline, Topic
from user_class import Student, Teacher
import json
import os

russian_language = Discipline("russian language")
kazakh_language = Discipline("kazakh language")
mathematics = Discipline("mathematics")

russian_language.add_topic(Topic("Грамматика рус"))
russian_language.add_topic(Topic("Склонения рус"))

kazakh_language.add_topic(Topic("Грамматика каз"))
kazakh_language.add_topic(Topic("Склонения каз"))

mathematics.add_topic(Topic("Дроби"))
mathematics.add_topic(Topic("Степени"))
russian_language.to_dict()
kazakh_language.to_dict()
mathematics.to_dict()
russian_language.create_json_file()
kazakh_language.create_json_file()
mathematics.create_json_file()




student1 = Student("Cтудент","Райымкулов Дидар Маратович", "Didar550")
student2 = Student("Cтудент", "Байгамбатов Ахымбай", "Akhym550")
teacher1 = Teacher("Преподватель","Сочалина Юлия", "Yuliya550", mathematics)


print("Информация о студентах и учителе:")
student1.display_info()
student2.display_info()
teacher1.display_info()

student1.add_grade("Грамматика рус", 4.5)
student1.add_grade("Склонения рус", 3.8)
student1.add_grade("Грамматика каз", 4.0)
student1.add_grade("Склонения каз", 4.2)
student1.add_grade("Дроби", 4.0)
student1.add_grade("Степени", 4.2)

student2.add_grade("Грамматика рус", 3.5)
student2.add_grade("Склонения рус", 4.8)
student2.add_grade("Грамматика каз", 5.0)
student2.add_grade("Склонения каз", 4.5)
student2.add_grade("Дроби", 4.8)
student2.add_grade("Степени", 4.9)


students = [student1, student2]
for student in students:
    student.display_grades()
from function import generate_grades_report 



generate_grades_report(students, "grades_repot.txt")

students_directory = "Students_info"
for student in students:
    student.save_grades_to_json(students_directory)