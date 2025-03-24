import abc
from abc import ABC, abstractmethod

class CourseErr(Exception):
    pass

class InvalidAgeErr(Exception):
    pass

class Person(ABC):
    c = 0
    def __init__(self, n, a):
        if a < 0:
            raise InvalidAgeErr("Age cannot be negative.")
        self._n = n
        self._a = a
        Person.c += 1
    @classmethod
    def p_count(cls):
        return cls.c
    @staticmethod
    def is_adult(age):
        return age >= 18
    @abstractmethod
    def info(self):
        pass

class Student(Person):
    all_crs = [
        "Electrodynamics",
        "Web Programming",
        "Electronics",
        "Elementary Math",
        "History of Kazakhstan",
        "English"
    ]
    def __init__(self, n, a, sid, mj):
        super().__init__(n, a)
        self.__sid = sid
        self._mj = mj
        self._mycrs = []
    @property
    def sid(self):
        return self.__sid
    @sid.setter
    def sid(self, val):
        if val:
            self.__sid = val
    def info(self):
        return f"Student {self._n} age:{self._a} ID:{self.__sid} Major:{self._mj}"
    def enroll(self, c):
        if c not in Student.all_crs:
            raise CourseErr(f"{c} not found in available courses")
        self._mycrs.append(c)
    def show_crs(self):
        return self._mycrs

class GradStudent(Student):
    def __init__(self, n, a, sid, mj, thesis, adv):
        super().__init__(n, a, sid, mj)
        self._th = thesis
        self._adv = adv
    def info(self):
        b = super().info()
        return f"{b} | Thesis:{self._th} Advisor:{self._adv}"

class Researcher:
    def __init__(self, area):
        self.area = area
    def do_res(self):
        return f"Research on {self.area}"

class ResearchStudent(Student, Researcher):
    def __init__(self, n, a, sid, mj, area):
        Student.__init__(self, n, a, sid, mj)
        Researcher.__init__(self, area)
    def info(self):
        base = super(Student, self).info()
        return f"{base}; RArea:{self.area}"

class Faculty(Person):
    def __init__(self, n, a, fid, dept):
        super().__init__(n, a)
        self._fid = fid
        self._dept = dept
    def info(self):
        return f"Faculty {self._n} age:{self._a} ID:{self._fid} Dept:{self._dept}"
    def teach(self, c):
        return f"{self._n} teaches {c}"

class Admin(Person):
    def __init__(self, n, a, admid, pos):
        super().__init__(n, a)
        self._admid = admid
        self._pos = pos
    def info(self):
        return f"Admin {self._n} age:{self._a} ID:{self._admid} Pos:{self._pos}"
    def manage(self):
        return f"{self._n} is managing university systems"

class Course:
    def __init__(self, title, teacher, desc):
        self.title = title
        self.teacher = teacher
        self.desc = desc
    def show_info(self):
        return f"Course:{self.title} by:{self.teacher} | {self.desc}"

class GradeBook:
    def __init__(self):
        self.grades = {}
    def set_grade(self, student_id, course_name, grade):
        if student_id not in self.grades:
            self.grades[student_id] = {}
        self.grades[student_id][course_name] = grade
    def get_grade(self, student_id, course_name):
        return self.grades.get(student_id, {}).get(course_name, "No grade")
    def get_all_grades(self, student_id):
        return self.grades.get(student_id, {})

def main():
    c_elec = Course("Electrodynamics", "Prof. Yergali", "Study of electric fields")
    c_web = Course("Web Programming", "Dr. Amina", "Frontend and Backend basics")
    c_hist = Course("History of Kazakhstan", "Prof. Bota", "From ancient times to present")
    print(c_elec.show_info())
    print(c_web.show_info())
    print(c_hist.show_info())
    st_list = [
        Student("Aigerim", 19, "S001", "CS"),
        Student("Bauyrzhan", 20, "S002", "Math"),
        Student("Erkebulan", 18, "S003", "IT"),
        Student("Altyn", 17, "S004", "History"),
        Student("Akbota", 21, "S005", "Electronics"),
        Student("Gabit", 20, "S006", "English"),
        Student("Gaukhar", 22, "S007", "Physics"),
        Student("Miras", 18, "S008", "IT"),
        Student("Nursultan", 21, "S009", "Math"),
        Student("Dariga", 19, "S010", "History"),
        Student("Yelnur", 20, "S011", "Physics"),
        Student("Zhamilya", 18, "S012", "Electronics"),
        Student("Azamat", 19, "S013", "WebDev"),
        Student("Zhanibek", 17, "S014", "English"),
        Student("Kausar", 21, "S015", "IT"),
        Student("Olzhas", 22, "S016", "Math"),
        Student("Saltanat", 18, "S017", "Physics"),
        Student("Zhaniya", 19, "S018", "Electronics"),
        Student("Arman", 20, "S019", "History"),
        Student("Karina", 18, "S020", "WebDev")
    ]
    fac1 = Faculty("Aiman", 35, "F101", "MathDep")
    fac2 = Faculty("Serik", 45, "F102", "PhysDep")
    adm1 = Admin("Damir", 29, "A001", "SystemAdmin")
    adm2 = Admin("Samal", 34, "A002", "OfficeAdmin")
    rs1 = ResearchStudent("Zhasulan", 23, "S500", "Bio", "Genetics")
    rs2 = ResearchStudent("Akzhan", 24, "S501", "Math", "Topology")
    gd1 = GradStudent("Bekzhan", 25, "S600", "IT", "AI in Robotics", "DrX")
    gd2 = GradStudent("Aknur", 24, "S601", "Physics", "QuantumSensors", "DrY")
    people = st_list + [fac1, fac2, adm1, adm2, rs1, rs2, gd1, gd2]
    print("\n--- Enrolling Students on courses ---")
    for st in st_list[:5]:
        try:
            st.enroll("Electrodynamics")
            st.enroll("English")
            st.enroll("History of Kazakhstan")
        except CourseErr as ce:
            print("Enroll error:", ce)
    print("\n--- Info about all persons ---")
    for p in people:
        print(p.info())
    print("\n--- Additional calls ---")
    print(fac1.teach("Electrodynamics"))
    print(adm1.manage())
    print(rs1.do_res())
    print(gd1.info())
    gb = GradeBook()
    gb.set_grade("S001", "Electrodynamics", 95)
    gb.set_grade("S001", "English", 88)
    gb.set_grade("S002", "English", 77)
    print("\n--- Grades ---")
    print("Ann (S001) Electrodynamics grade:", gb.get_grade("S001", "Electrodynamics"))
    print("Ann (S001) English grade:", gb.get_grade("S001", "English"))
    print("Bob (S002) English grade:", gb.get_grade("S002", "English"))
    print("Bob (S002) Math101 grade:", gb.get_grade("S002", "Math101"))
    print("\nTotal Person objects created:", Person.p_count())

if __name__ == "__main__":
    main()
