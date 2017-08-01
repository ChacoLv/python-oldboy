# -*- coding:utf-8 -*-
# LC


class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr =addr
        self.students = []
        self.teachers = []

    def enroll(self,stu_obj):
        print("为学员%s 办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣员工:%s,薪资为:%s"%(staff_obj.name,staff_obj.salary))
        self.teachers.append(staff_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex =sex

    def tell(self):
        print('''
        ''')

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching course %s"%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,stu_class):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.stu_class = stu_class

    def tell(self):
        print('''
        ---- info of Student:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Student_ID:%s
        Class:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.stu_class))

    def pay_tuition(self,amount):
        print("%s should pay tuition %s"%(self.name,amount))



S1 = Student("LC",20,"M",1001,"Python")
S1.tell()
S1.pay_tuition(888)
S2 = Student("XM",19,"M",1002,"English")

T1 = Teacher("Jack",29,"M",2000,"Python")
T1.tell()
T1.teach()
T2 = Teacher("Mark",23,"M",3000,"English")
SC1 = School("浙大","杭州")

SC1.hire(T1)
SC1.enroll(S1)








