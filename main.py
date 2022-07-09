class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rate(self):
        student_grades_list = []
        for grade in self.grades.values():
            student_grades_list += grade
        if len(self.grades.values()) > 0:
            average_grade = round(sum(student_grades_list) / len(student_grades_list), 1)
            return average_grade
        else:
            return 'Нет выставленных оценок'


    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_rate()}\n' \
                 f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}\n '
        return output


    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не является студентом')
            return
        return self.__average_rate() < other.__average_rate()


    def __le__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не является студентом')
            return
        return self.__average_rate() <= other.__average_rate()


    def __eq__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не является студентом')
            return
        return self.__average_rate() == other.__average_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_rate(self):
        lecturer_grades_list = []
        for grade in self.grades.values():
            lecturer_grades_list += grade
        if len(self.grades.values()) > 0:
            average_grade = round(sum(lecturer_grades_list) / len(lecturer_grades_list), 1)
            return average_grade
        else:
            return 'Нет выставленных оценок'


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не является лектором')
            return
        return self.__average_rate() < other.__average_rate()


    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не является лектором')
            return
        return self.__average_rate() <= other.__average_rate()


    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не является лектором')
            return
        return self.__average_rate() == other.__average_rate()


    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_rate()}\n'
        return output


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return output

# задание 4
def average_course_grade_s(students_list, course_name): # средняя оценка за дз по всем студентам по конкретному курсу
      grades_list = []
      for student in students_list:
          if course_name in student.grades:
              grades_list += student.grades[course_name]
      return print(f'Средняя оценка студентов по предмету {course_name}: {round(sum(grades_list) / len(grades_list), 1)}')


def average_course_grade_lec(lecturer_list, course_name):  # средняя оценка за курс по мнению студентов
    grades_list = []
    for lecturer in lecturer_list:
        if course_name in lecturer.grades:
            grades_list += lecturer.grades[course_name]
    return print(f'Средняя оценка курса {course_name}: {round(sum(grades_list) / len(grades_list), 1)}')


# полевые испытания
student1 = Student('Vova', 'Pupkin', 'male')
student2 = Student('Olya', 'Pupkina', 'female')

lecturer1 = Lecturer('Oleg', 'Bulygin')
lecturer2 = Lecturer('Alexander', 'Bardin')

reviewer1 = Reviewer('Elon', 'Musk')
reviewer2 = Reviewer('Sasha', 'Belyi')

student1.courses_in_progress += ['Python', 'Triton', 'Newton']
student2.courses_in_progress += ['Python', 'Newton', 'Boston']

student1.finished_courses += ['GIT']
student2.finished_courses += ['GIT']

lecturer1.courses_attached += ['Python', 'Triton']
lecturer2.courses_attached += ['Newton', 'Boston']

reviewer1.courses_attached += ['Python', 'Triton', 'Newton']
reviewer2.courses_attached += ['Python', 'Newton', 'Boston']

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Triton', 9)
student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Triton', 9)
student1.rate_lecturer(lecturer2, 'Newton', 10)
student1.rate_lecturer(lecturer2, 'Boston', 10)
student2.rate_lecturer(lecturer2, 'Newton', 8)
student2.rate_lecturer(lecturer2, 'Boston', 9)

reviewer1.rate_student(student1,'Python', 9)
reviewer1.rate_student(student1, 'Triton', 10)
reviewer1.rate_student(student1, 'Newton', 8)
reviewer1.rate_student(student2,'Python', 9)
reviewer1.rate_student(student2, 'Newton', 8)

reviewer2.rate_student(student1, 'Python', 7)
reviewer2.rate_student(student1, 'Newton', 8)
reviewer2.rate_student(student2, 'Python', 9)
reviewer2.rate_student(student2, 'Newton', 10)
reviewer2.rate_student(student2, 'Boston', 10)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

average_course_grade_s(students_list, 'Python')
average_course_grade_s(students_list, 'Triton')
average_course_grade_s(students_list, 'Newton')
average_course_grade_s(students_list, 'Boston')

average_course_grade_lec(lecturers_list, 'Python')
average_course_grade_lec(lecturers_list, 'Triton')
average_course_grade_lec(lecturers_list, 'Newton')
average_course_grade_lec(lecturers_list, 'Boston')


print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

print(f'student1 > student2 : {student1 > student2}')
print(f'student1 >= student2 : {student1 >= student2}')
print(f'student1 == student2 : {student1 == student2}')


print(f'lecturer1 > lecturer2 : {lecturer1 > lecturer2}')
print(f'lecturer1 >= lecturer2 : {lecturer1 >= lecturer2}')
print(f'lecturer1 == lecturer2 : {lecturer1 == lecturer2}')