import sqlite3

class SQLAgent:
    def __init__(self, name_db):
        self.db = sqlite3.connect(name_db)
        self.create_table_students()
        self.create_table_courses()
        self.create_table_courses_and_students()

    def create_table_students(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (        
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            major TEXT
            )

        ''')
        cursor.close()

    def create_table_courses(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (        
            course_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name  TEXT,
            instructor TEXT
            )

        ''')
        cursor.close()

    def create_table_courses_and_students(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS course_and_students (        
            id_c_s  INTEGER PRIMARY KEY AUTOINCREMENT,
            id_of_course INT,
            id_of_student INT,
            FOREIGN KEY(id_of_course) REFERENCES courses(course_id),
	        FOREIGN KEY(id_of_student) REFERENCES students(id)
            )

        ''')
        cursor.close()
        self.db.commit()

    def execute_query(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        cursor.close()
        self.db.commit()

    def fetch_all(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_one(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def fetch_all_without_params(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


