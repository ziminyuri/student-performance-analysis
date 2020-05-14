from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from transform.errors import bd_error
from settings import YEAR
import numpy as np

Base = declarative_base()


def get_user_password(session, login):
    user = session.query(Users).filter_by(login=login).first()

    try:
        return user

    except:
        return None


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)


class Discipline(Base):
    __tablename__ = 'discipline'
    id_discipline = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    @staticmethod
    def all(session):
        try:
            list_name = session.query(Discipline.name).order_by(Discipline.name).all()
            return list_name
        except Exception as e:
            session.rollback()
            print(str(e))

    @staticmethod
    def show_name(session):
        try:
            list_all = session.query(Discipline).order_by(Discipline.name).all()
            ls_name = []
            for i in list_all:
                ls_name.append(i.name)

            return ls_name

        except Exception as e:
            session.rollback()
            print(str(e))


class Specialty(Base):
    __tablename__ = 'specialty'
    id_specialty = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    name = Column(String(255), nullable=False)

    @staticmethod
    def show_name(session):
        try:
            list_all = session.query(Specialty).all()
            ls_name = []
            for i in list_all:
                ls_name.append(i.name)

            return ls_name

        except Exception as e:
            session.rollback()
            print(str(e))


class Group(Base):
    __tablename__ = 'group_table'
    id_group = Column(Integer, primary_key=True)
    number = Column(String(100), nullable=False)
    id_specialty = Column(Integer, ForeignKey('specialty.id_specialty'), nullable=False, primary_key=True)
    specialty = relationship(Specialty, primaryjoin=id_specialty == Specialty.id_specialty, backref="p_specialty")

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.number, self.specialty.name)

    @staticmethod
    def show_name(session):
        try:
            list_all = session.query(Group).all()
            ls = []
            for i in list_all:
                ls.append(i.number)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def show_all(session):
        try:
            list = session.query(Group).join(Specialty).order_by(Specialty.name).all()
            ls = []
            for i in list:
                ls1 = []
                ls1.append(i.specialty.name)
                ls1.append(i.number)

                ls.append(ls1)

            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def add(session, number, specialty):
        try:
            s = session.query(Specialty).filter_by(name=specialty).first()
            id_specialty = s.id_specialty
            new_group = Group(number=number, id_specialty=id_specialty)
            session.add(new_group)
            session.flush()
        except Exception as e:
            bd_error()

    @staticmethod
    def update(session, old_number, number, specialty):
        try:
            s = session.query(Specialty).filter_by(name=specialty).first()
            id_specialty = s.id_specialty
            g = session.query(Group).filter_by(number=old_number)
            g.update({Group.number: number, Group.id_specialty: id_specialty})
            session.commit()

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def delete(session, number):
        try:
            s = session.query(Group).filter_by(number=number)
            s.delete()
            session.commit()

        except Exception as e:
            session.rollback()
            bd_error()


class Student(Base):
    __tablename__ = 'student'
    id_student = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    record_book = Column(Integer, nullable=False)
    id_group = Column(Integer, ForeignKey('group_table.id_group'), nullable=False, primary_key=True)
    group = relationship(Group, primaryjoin=id_group == Group.id_group, backref="parent_group")

    @staticmethod
    def all(session, group_number: str):
        try:
            student_list: list = session.query(Student).order_by(Student.name).all()
            ls: list = []
            for i in student_list:
                if i.group.number == group_number:
                    ls1: list = []
                    ls1.append(i.name)
                    ls1.append(i.record_book)

                    ls.append(ls1)

            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def all_name(session, group_number: str):
        try:
            s = session.query(Student).join(Group).filter(Group.number == group_number).order_by(Student.name).all()
            ls = []
            for i in s:
                ls.append(i.name)

            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def add(session, name, record_book, group_number):
        try:
            g = session.query(Group).filter_by(number=group_number).first()
            id_group = g.id_group
            new_student = Student(name=name, record_book=record_book, id_group=id_group)
            session.add(new_student)
            session.flush()

        except Exception as e:
            bd_error()

    @staticmethod
    def update(session, old_record_book, new_name, new_record_book):
        try:
            s = session.query(Student).filter_by(record_book=old_record_book)
            s.update({Student.record_book: new_record_book, Student.name: new_name})
            session.commit()

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def delete(session, record_book):
        try:
            s = session.query(Student).filter_by(record_book=record_book)
            s.delete()
            session.commit()

        except Exception as e:
            session.rollback()


class Work(Base):
    __tablename__ = 'work'
    id_work = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    deadline = Column(Date, nullable=False)
    id_group = Column(Integer, ForeignKey('group_table.id_group'), nullable=False, primary_key=True)
    group = relationship(Group, primaryjoin=id_group == Group.id_group, backref="parent_work_group")
    id_discipline = Column(Integer, ForeignKey('discipline.id_discipline'), nullable=False, primary_key=True)
    discipline = relationship(Discipline, primaryjoin=id_discipline == Discipline.id_discipline,
                              backref="parent_work_group")

    @staticmethod
    def show_name(session, discipline, group_number):
        try:
            list_all = session.query(Work).all()
            ls = []
            ls.append("ФИО студента")
            for i in list_all:
                if i.discipline.name == discipline:
                    if i.group.number == group_number:
                        ls.append(i.name)
                        ls.append("Дата защиты")
            return ls

        except Exception as e:
            session.rollback()
            bd_error()


class Grade(Base):
    __tablename__ = 'grade'
    id_grade = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    id_work = Column(Integer, ForeignKey('work.id_work'), nullable=False, primary_key=True)
    work = relationship(Work, primaryjoin=id_work == Work.id_work, backref="parent_grade_work")
    id_student = Column(Integer, ForeignKey('student.id_student'), nullable=False, primary_key=True)
    student = relationship(Student, primaryjoin=id_student == Student.id_student, backref="parent_grade_student")

    @staticmethod
    def all(session, discipline, group_number):
        try:
            grade_all = session.query(Grade).join(Work).join(Discipline).join(Group).join(Student).filter(
                Discipline.name == discipline).filter(Group.number == group_number).order_by(Grade.id_student).all()
            student_all = session.query(Student).join(Group).filter(Group.number == group_number).order_by(
                Student.name).all()
            work_all = session.query(Work).join(Discipline).join(Group).filter(Discipline.name == discipline).filter(
                Group.number == group_number).order_by(Work.name).all()
            ls = []
            for i in student_all:
                row = []
                row.append(i.name)
                for j in work_all:
                    for k in grade_all:
                        if k.id_work == j.id_work and k.id_student == i.id_student:
                            row.append(k.value)
                            row.append(str(k.date))
                ls.append(row)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def lagging_students(session):
        try:
            work_all = session.query(Work).join(Discipline).order_by(Discipline.name).all()

            ls = []
            for work in work_all:
                if work.deadline.year == YEAR:
                    ls.append(work)
            print('dfsdf')
        except Exception as e:
            session.rollback()
            bd_error()


class SessionType(Base):
    __tablename__ = 'session_type'
    id_session_type = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)


class TypeFinalGrade(Base):
    __tablename__ = 'type_final_grade'
    id_type_final_grade = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)


class FinalGrade(Base):
    __tablename__ = 'final_grade'
    id_final_grade = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    id_type_final_grade = Column(Integer, ForeignKey('type_final_grade.id_type_final_grade'), nullable=False,
                                 primary_key=True)
    type_final_grade = relationship(TypeFinalGrade,
                                    primaryjoin=id_type_final_grade == TypeFinalGrade.id_type_final_grade,
                                    backref="parent_TypeFinalGrade_FinalGrade")
    id_session_type = Column(Integer, ForeignKey('session_type.id_session_type'), nullable=False, primary_key=True)
    session_type = relationship(SessionType, primaryjoin=id_session_type == SessionType.id_session_type,
                                backref="parent_SesstionType_FinalGrade")
    id_discipline = Column(Integer, ForeignKey('discipline.id_discipline'), nullable=False, primary_key=True)
    discipline = relationship(Discipline, primaryjoin=id_discipline == Discipline.id_discipline,
                              backref="parent_discipline_FinalGrade")
    id_group = Column(Integer, ForeignKey('group_table.id_group'), nullable=False, primary_key=True)
    group = relationship(Group, primaryjoin=id_group == Group.id_group, backref="parent_group_FinalGrade")


class Control(Base):
    __tablename__ = 'control'
    id_control = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    value = Column(Integer, nullable=False)
    set_off = Column(Boolean)
    id_final_grade = Column(Integer, ForeignKey('final_grade.id_final_grade'), nullable=False, primary_key=True)
    final_grade = relationship(FinalGrade, primaryjoin=id_final_grade == FinalGrade.id_final_grade,
                               backref="parent_FinalGrade_Control")
    id_student = Column(Integer, ForeignKey('student.id_student'), nullable=False, primary_key=True)
    student = relationship(Student, primaryjoin=id_student == Student.id_student, backref="parent_SesstionType_Control")

    @staticmethod
    def analysis_student(session, student, stud_session, period):
        try:
            if stud_session == 'Все сессии':
                student_control_all = session.query(Control).join(Student).filter(Student.name == student).\
                    order_by(Control.date).all()
            else:
                student_control_all = session.query(Control).join(Student).join(FinalGrade).join(SessionType).filter(
                    Student.name == student). \
                    filter(SessionType.name == stud_session).order_by(Control.date).all()

            ls = []
            average_value = 0
            year_begin = YEAR
            count = 0

            if period == "За последний год":
                period_all = 1
            elif period == 'За последние 2 года':
                period_all = 2
            elif period == 'За последние 3 года':
                period_all = 3
            else:
                period_all = 4

            average_all = []
            for i in range(period_all):
                average_all1 = []
                average_all1.append(str(year_begin))
                average_all1.append(average_value)
                average_all1.append(count)
                average_all.append(average_all1)
                year_begin -= 1

            for j in average_all:
                for i in student_control_all:
                    if i.final_grade.type_final_grade.name == 'Экзамен':
                        if int(j[0]) == i.date.year:
                            j[1] = j[1] + i.value
                            j[2] = j[2] + 1

            for j in average_all:
                if j[2] != 0:
                    ls1 = []
                    year = int(j[0])
                    year_value = str(year - 1) + '-' + str(year)
                    ls1.append(year_value)
                    value = j[1] / j[2]
                    ls1.append(value)
                    ls.append(ls1)

            ls = np.array(ls)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def analysis_student_proportional(session, student, stud_session, period):
        try:
            if stud_session == 'Все сессии':
                student_control_all = session.query(Control).join(Student). \
                    filter(Student.name == student).all()
            else:
                student_control_all = session.query(Control).join(Student).join(FinalGrade).join(SessionType). \
                    filter(Student.name == student).filter(SessionType.name == stud_session).all()

            ls = []
            year_begin = YEAR
            count = 0

            if period == "За последний год":
                period_all = 1
            elif period == 'За последние 2 года':
                period_all = 2
            elif period == 'За последние 3 года':
                period_all = 3
            else:
                period_all = 4

            average_all = []
            for i in range(period_all):
                average_all1 = []
                average_all1.append(str(year_begin))
                average_all1.append(count)
                average_all1.append(count)
                average_all1.append(count)
                average_all1.append(count)
                average_all.append(average_all1)
                year_begin -= 1

            for j in average_all:
                for i in student_control_all:
                    if i.final_grade.type_final_grade.name == 'Экзамен':
                        if int(j[0]) == i.date.year:
                            if i.value < 25:
                                j[1] = j[1] + 1
                            elif 25 <= i.value < 50:
                                j[2] = j[2] + 1
                            elif 50 <= i.value < 75:
                                j[3] = j[3] + 1
                            else:
                                j[4] = j[4] + 1

            for j in average_all:
                ls1 = []
                year = int(j[0])
                year_value = str(year - 1) + '-' + str(year)
                ls1.append(year_value)
                value = j[1]
                ls1.append(value)
                value = j[2]
                ls1.append(value)
                value = j[3]
                ls1.append(value)
                value = j[4]
                ls1.append(value)
                ls.append(ls1)

            ls = np.array(ls)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def analysis_group(session, group, stud_session, period):
        try:
            if stud_session == 'Все сессии':
                student_control_all = session.query(Control).join(Student).join(Group).join(FinalGrade).\
                    filter(Group.number == group).all()
            else:
                student_control_all = session.query(Control).join(Student).join(Group).join(FinalGrade).join(SessionType). \
                    filter(Group.number == group).filter(SessionType.name == stud_session).all()

            ls = []
            average_value = 0
            year_begin = YEAR
            count = 0

            if period == "За последний год":
                period_all = 1
            elif period == 'За последние 2 года':
                period_all = 2
            elif period == 'За последние 3 года':
                period_all = 3
            else:
                period_all = 4

            average_all = []
            for i in range(period_all):
                average_all1 = []
                average_all1.append(str(year_begin))
                average_all1.append(average_value)
                average_all1.append(count)
                average_all.append(average_all1)
                year_begin -= 1

            for j in average_all:
                for i in student_control_all:
                    if i.final_grade.type_final_grade.name == 'Экзамен':
                        if int(j[0]) == i.date.year:
                            j[1] = j[1] + i.value
                            j[2] = j[2] + 1

            for j in average_all:
                if j[2] != 0:
                    ls1 = []
                    year = int(j[0])
                    year_value = str(year - 1) + '-' + str(year)
                    ls1.append(year_value)
                    value = j[1] / j[2]
                    value = round(value, 2)
                    ls1.append(value)
                    ls.append(ls1)

            ls = np.array(ls)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()

    @staticmethod
    def analysis_group_proportional(session, group, stud_session, period):
        try:
            if stud_session == 'Все сессии':
                student_control_all = session.query(Control).join(Student).join(Group).join(FinalGrade). \
                    filter(Group.number == group).all()
            else:
                student_control_all = session.query(Control).join(Student).join(Group).join(FinalGrade).join(SessionType). \
                    filter(Group.number == group).filter(SessionType.name == stud_session).all()

            ls = []
            year_begin = YEAR
            count = 0

            if period == "За последний год":
                period_all = 1
            elif period == 'За последние 2 года':
                period_all = 2
            elif period == 'За последние 3 года':
                period_all = 3
            else:
                period_all = 4

            average_all = []
            for i in range(period_all):
                average_all1 = []
                average_all1.append(str(year_begin))
                average_all1.append(count)
                average_all1.append(count)
                average_all1.append(count)
                average_all1.append(count)
                average_all.append(average_all1)
                year_begin -= 1

            for j in average_all:
                for i in student_control_all:
                    if i.final_grade.type_final_grade.name == 'Экзамен':
                        if int(j[0]) == i.date.year:
                            if i.value < 25:
                                j[1] = j[1] + 1
                            elif 25 <= i.value < 50:
                                j[2] = j[2] + 1
                            elif 50 <= i.value < 75:
                                j[3] = j[3] + 1
                            else:
                                j[4] = j[4] + 1

            for j in average_all:
                ls1 = []
                year = int(j[0])
                year_value = str(year - 1) + '-' + str(year)
                ls1.append(year_value)
                value = j[1]
                ls1.append(value)
                value = j[2]
                ls1.append(value)
                value = j[3]
                ls1.append(value)
                value = j[4]
                ls1.append(value)
                ls.append(ls1)

            ls = np.array(ls)
            return ls

        except Exception as e:
            session.rollback()
            bd_error()
