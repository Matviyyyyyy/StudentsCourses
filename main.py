from Course import Course
from CS import  CS
from Student import Student

student_agent = Student("database.db")
course_agent = Course("database.db")
cs_agent = CS("database.db")

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")



    if choice == "1":
        name = input("Ім'я: ")
        age = int(input("Вік: "))
        major = input("Профіль: ")
        student_agent.add_student(str(name), int(age), str(major))
    elif choice == "2":
        course_name = input("Назва курсу: ")
        instructor = input("Викладач курсу: ")
        course_agent.add_course(course_name, instructor)
    elif choice == "3":
        all_students = student_agent.get_all_students()
        for student in all_students:
            print(f"Ім'я - {student[1]}\nВік - {student[2]}\nПрофіль - {student[3]}")
            print("------------------------------------------------------------------------------------------")
    elif choice == "4":
        all_courses = course_agent.get_all_courses()
        for course in all_courses:
            print(f"Назва - {course[1]}\nВикладач - {course[2]}")
            print("------------------------------------------------------------------------------------------")
    elif choice == "5":
        id_s = int(input("Айді студента: "))
        id_c = int(input("Айді курсу: "))
        cs_agent.add_belonging(id_c, id_s)
    elif choice == "6":
        print(cs_agent.get_students_for_course())
    elif choice == "7":
        break
    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
