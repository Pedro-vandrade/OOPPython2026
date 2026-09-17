class Student:

    def __init__(self, name, module):
        self.name = name
        self.module = module

        self.grade1 = None
        self.grade2 = None
        self.exam = None

        def submit_grade1(self, grade1):
            self.grade1 = float(grade1)

        def submit_grade2(self, grade2):
            self.grade2 =  float(grade2)

        def submit_exam(self, exam):
            self.exam = float(exam)

        def situation(self):
            # verifica se as notas são nulas ou não
            if self.grade1 is None and self.grade2 is None:
                return 0.0, "Grades were not submited."

            first_avg = self.grade1 + self.grade2 / 2

            # if the average higher than 6, student passes.

            if first_avg >= 6:
                return round(first_avg, 2), "Passed"

            if self.exam is None:
                return round(first_avg, 2), "At final exam, expect final exam grade."

            final_avg = (self.grade1 + self.grade2 + self.exam) / 3

            if final_avg >= 6:
                return round(final_avg, 2), "Passed."
            else:
                return round(final_avg,2), "Failed."

            def show_status(student):
                average, msg = student.situation()

                print(f' Student: {student.name} | Module: {student.module}')
                print(f'Grades: [{student.grade1}, {student.grade2}, {student.exam}]')
                print(f'GPA: {average} | Status: {msg}')




