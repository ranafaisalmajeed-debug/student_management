# This file shows a simple school system using basic OOP.
# We use classes to organise data and actions.
# Each class has its own variables and functions.


class Student:
    # A student has a name, student ID, and a status showing if they are enrolled.
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled = True


class Course:
    # A course has a name and a list of students in it.
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []


class School:
    # The School class keeps all the students and courses together.
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        # Add a new student to the school list.
        self.students.append(student)
        print(student.name, "has been added.")

    def add_course(self, course):
        # Add a new course to the school list.
        self.courses.append(course)
        print(course.course_name, "has been added.")

    def enrol_student(self, student_id, course_name):
        # Find the student and the course, then add the student to the course.
        for student in self.students:
            if student.student_id == student_id:

                for course in self.courses:
                    if course.course_name == course_name:

                        if student not in course.students:
                            course.students.append(student)
                            print(student.name, "has enrolled in", course.course_name)
                        else:
                            print("Student is already enrolled.")
                        return

                print("Course not found.")
                return

        print("Student not found.")

    def remove_student(self, student_id, course_name):
        # Remove a student from a course if they are enrolled there.
        for student in self.students:
            if student.student_id == student_id:

                for course in self.courses:
                    if course.course_name == course_name:

                        if student in course.students:
                            course.students.remove(student)
                            print(student.name, "has been removed from", course.course_name)
                        else:
                            print("Student is not enrolled in this course.")
                        return

                print("Course not found.")
                return

        print("Student not found.")

    def display_courses(self):
        # Show all courses and the students in each one.
        print("\nCourses and Students:")

        for course in self.courses:
            print("\nCourse:", course.course_name)

            if len(course.students) == 0:
                print("No students enrolled.")
            else:
                for student in course.students:
                    print("-", student.name, "(", student.student_id, ")")


# Create a school object.
school = School()

# Create student objects.
student1 = Student("Ali", "S001")
student2 = Student("Sarah", "S002")
student3 = Student("John", "S003")

# Add students to the school.
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

# Create course objects.
course1 = Course("Python Programming")
course2 = Course("Database Basics")

# Add courses to the school.
school.add_course(course1)
school.add_course(course2)

# Enrol students in courses.
school.enrol_student("S001", "Python Programming")
school.enrol_student("S002", "Python Programming")
school.enrol_student("S003", "Database Basics")

# Show the course list and the students in each course.
school.display_courses()

# Remove a student from a course.
school.remove_student("S002", "Python Programming")

# Show the courses again after the removal.
school.display_courses()