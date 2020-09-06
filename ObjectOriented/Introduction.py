my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}


def average_grades(student):
    return sum(student['grades'] / len(student['grades']))


print(average_grades(my_student))


class Student:
    #Define a student
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


class Movie:
    # Define a Movie class that has two properties: name and director

    def __init__(self, title, director):
        self.title = title
        self.director = director

    def print_info(self):
        print(f"<<{self.title}>> by {self.director}")


# You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski')



