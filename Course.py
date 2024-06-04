from SQLAgent import SQLAgent


class Course:
    def __init__(self, db):
        self.db = SQLAgent("database.db")

    def add_course(self, course_name, instructor):
        self.db.execute_query('''
        INSERT INTO courses (course_name, instructor) VALUES (?, ?)
        ''', (course_name, instructor))

    def get_course(self, id):
        return self.db.fetch_one('''
        SELECT * FROM courses WHERE course_id=?
        ''', (id,))

    def update_course(self, id, course_name, instructor):
        if course_name:
            self.db.execute_query('''
            UPDATE courses SET course_name=? WHERE course_id=?
            ''', (course_name, id))
        if instructor:
            self.db.execute_query('''
            UPDATE courses SET instructor=? WHERE course_id=?
            ''', (instructor, id))
    def delete_student(self, id):
        self.db.execute_query('''
        DELETE FROM courses WHERE course_id=?
        ''', (id,))

    def get_all_courses(self):
        return self.db.fetch_all_without_params('''
        SELECT * FROM courses
        ''')


