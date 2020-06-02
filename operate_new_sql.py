from learn_sql import db,Student,Grade,Teacher,Course

#s=Student(name='张三',gender='男',phone='12345678900')
#db.session.add(s)
#db.session.commit()
#db.session.add_all([s1,s2,s3])

#stu=Student.query.get(1)
#print(stu.name)
#stu=Student.query.all()
#print(stu)
#stu=Student.query.filter(Student.id==1)
#for i in stu:
    #print(i.name)
#stu=Student.query.filter_by(name='张三').first()
#print(stu.name)

#stu=Student.query.filter(Student.id==1).update({'name':'李四'})
#db.session.commit()
#stu=Student.query.filter(Student.gender=='男').first()
#stu.gender='女'
#db.session.add(stu)
#db.session.commit()

#stu=Student.query.filter(Student.id==1).delete()

#grade1=Grade(grade=100,student_id=1)
#grade2=Grade(grade=95,student_id=1)
#db.session.add(grade1)
#db.session.add(grade2)
#db.session.commit()

#stu=Student.query.get(1)
#for i in stu.grades:
    #print(stu.name,i.grade)

#grade=Grade.query.filter(Grade.grade==100).first()
#print(grade.student.name,grade.student.gender)



