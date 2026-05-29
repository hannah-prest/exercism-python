"""garden"""
class Garden:
    """garden"""
    def __init__(self, diagram, students = None):
        plants = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
        if students is None:
            students = ["Alice","Bob","Charlie","David","Eve","Fred","Ginny","Harriet","Ileana","Joseph","Kincaid","Larry"]
        students = sorted(students)
        rows = diagram.split("\n")
        self.roster = {}
        for index in range(0,len(rows[0]),2):
            student = students[index//2]
            students_plants_codes = [rows[0][index],rows[0][index+1],rows[1][index],rows[1][index+1]]
            self.roster[student] = [plants[char] for char in students_plants_codes]

    def plants(self, student):
        return self.roster[student]
