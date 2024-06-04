from SQLAgent import SQLAgent
from Student import Student
from Course import Course
from CS import CS

sql_agent = SQLAgent("database.db")


#Trying student ------------------------------------------------------------------------


student_agent = Student("database.db")
student_agent.add_student("Матвій", 14, "Фіз-мат")
student_agent.add_student( "Іван", 15, "Біо-хім і Українська філологія")
student_agent.add_student("Настя", 17, "Українська філологія")



#Trying course ------------------------------------------------------------------------

course_agent = Course("database.db")
course_agent.add_course("Українська філологія", "Ольга")
course_agent.add_course("Фіз-мат", "Іван")
course_agent.add_course("Біо-хім", "Ірина")


cs_agent = CS("database.db")
cs_agent.add_belonging(1, 3)
cs_agent.add_belonging(1, 2)
cs_agent.add_belonging(2, 1)
cs_agent.add_belonging(3, 2)

#print(cs_agent.get_students_for_course())





