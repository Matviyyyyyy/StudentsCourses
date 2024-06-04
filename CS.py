from SQLAgent import SQLAgent


class CS:
    def __init__(self, db):
        self.db = SQLAgent("database.db")

    def add_belonging(self, id_of_course, id_of_student):
        self.db.execute_query('''
        INSERT INTO course_and_students (id_of_course, id_of_student) VALUES (?, ?)
        ''', (id_of_course, id_of_student))

    def get_students_for_course(self):
        return self.db.fetch_all('''
        SELECT courses.course_name, students.name, students.age 
        FROM courses
        INNER JOIN course_and_students ON course_and_students.id_of_course = courses.course_id
        INNER JOIN students ON students.id = course_and_students.id_of_student;
        ''',  ())

    def update_belonging(self, id, id_of_course, id_of_student):
        if id_of_course:
            self.db.execute_query('''
            UPDATE course_and_students SET id_of_course=? WHERE id_c_s=?
            ''', (id_of_course, id))
        if id_of_student:
            self.db.execute_query('''
            UPDATE course_and_students SET id_of_student=? WHERE id_c_s=?
            ''', (id_of_student, id))
    def delete_belonging(self, id):
        self.db.execute_query('''
        DELETE FROM course_and_students WHERE id_c_s=?
        ''', (id,))