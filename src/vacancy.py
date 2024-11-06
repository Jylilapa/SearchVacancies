class Vacancy:
    __slots__ = ('name', 'city', 'salary', 'requirement', 'responsibility', 'schedule', 'experience', 'result', )

    def __init__(self, name, city, salary, requirement, responsibility, schedule, experience):
        self.name = name
        self.city = city
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule
        self.experience = experience
        self.result = []

