import json
import os
class User:
    
    def __init__(self,user_type, full_name, username):
        self.user_type=user_type
        self.full_name = full_name
        self.username = username
        

    def display_info(self):
        print (f"Тип пользователя: {self.user_type}")
        print(f"ФИО: {self.full_name}")
        print(f"UserName: {self.username}")

class Student(User):
    def __init__(self, user_type, full_name, username):
        super().__init__(user_type,full_name, username)
        self.grades={}
    def display_info(self):
        super().display_info()

    def add_grade(self,topic,grade):
        self.grades[topic]=grade
    
    def display_grades(self):
        print(f"оценки студента {self.full_name} {self.grades}")
    
    
    def save_grades_to_json(self, directory):
        data = {
            "full_name": self.full_name,
            "username": self.username,
            "grades": self.grades
        }
        json_filename = os.path.join(directory, f"{self.username.lower()}_grades.json")

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    
class Teacher(User):
    def __init__(self, user_type,full_name, username, discipline):
        super().__init__(user_type,full_name, username)
        self.discipline = discipline
    
    def display_info(self):
        super().display_info()
        print(f"Преподает: {self.discipline.name}")