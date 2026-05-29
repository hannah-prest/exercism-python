"""school"""
class School:
    """school"""
    def __init__(self):
        self.students = {}
        self.addition_log = []
    
    def add_student(self, name, grade):
        if name in self.students:
            self.addition_log.append(False)
        else:
            self.students[name] = grade
            self.addition_log.append(True)
    
    def roster(self):
        return [name for _, name in sorted((grade, name) for name, grade in self.students.items())]
    
    def grade(self, grade_number):
        return sorted(name for name, grade in self.students.items() if grade == grade_number)

    def added(self):
        return self.addition_log