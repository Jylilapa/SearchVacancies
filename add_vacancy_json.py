from src.adding_vacancies import AddingVacancies



class AddVacanciesJSON(AddingVacancies):

    def __init__(self, name_list="data/vacancy_list.json"):
        self.name_list = name_list

    def save_vacancy(self, vacancy_list):

