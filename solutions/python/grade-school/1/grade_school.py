"""school"""
class School:
    """school"""
    def __init__(self):
        self.grades = []
        self.addition_log = []

    def add_student(self, name, grade):
        while len(self.grades)-1 < grade:
            self.grades.append(set())
        if name in self.roster():
            self.addition_log.append(False)
        else:
            self.grades[grade].add(name)
            self.addition_log.append(True)

    def roster(self):
        return [student for grade in self.grades for student in sorted(grade)]

    def grade(self, grade_number):
        if grade_number < len(self.grades):
            return sorted(self.grades[grade_number])
        return []

    def added(self):
        return self.addition_log