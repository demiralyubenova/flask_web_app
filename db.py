from website import db
from website.models import Item, Grades
from main import app 

with app.app_context():
                
                new_grade = Grades(grade = 4, student_id = 1, subject = "MATH", teacher_id = 2)
                db.session.add(new_grade)
                db.session.commit()