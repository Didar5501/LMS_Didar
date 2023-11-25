def generate_grades_report(students, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"Студент: {student.full_name}\n")
            file.write("Оценки:\n")
            for topic, grade in student.grades.items():
                file.write(f"- Тема: {topic}, Оценка: {grade}\n")
            file.write("\n")