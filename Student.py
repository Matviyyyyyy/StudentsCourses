from SQLAgent import SQLAgent


class Student:
    def __init__(self, db):
        self.db = SQLAgent("database.db")

    def add_student(self, name, age, major):
        self.db.execute_query('''
        INSERT INTO students (name, age, major) VALUES (?, ?, ?)
        ''', (name, age, major))

    def get_student(self, id):
        return self.db.fetch_one('''
        SELECT * FROM students WHERE id=?
        ''', (id,))

    def update_student(self, id, name, age, major ):
        if name:
            self.db.execute_query('''
            UPDATE students SET name=? WHERE id=?
            ''', (name, id))
        if age:
            self.db.execute_query('''
            UPDATE students SET age=? WHERE id=?
            ''', (age, id))
        if major:
            self.db.execute_query('''
            UPDATE students SET major=? WHERE id=?
            ''', (major, id))

    def delete_student(self, id):
        self.db.execute_query('''
        DELETE FROM students WHERE id=?
        ''', (id,))

    def get_all_students(self):
        return self.db.fetch_all_without_params('''
        SELECT * FROM students
        ''')