import json
import os.path
from src.adding_vacancies import AddingVacancies
from src.vacancy import Vacancy


class AddVacanciesJSON(AddingVacancies, Vacancy):
    """Класс сохранения, удаления и выборки вакансий"""

    def __init__(
        self,
        name,
        city,
        salary,
        requirement,
        schedule,
        experience,
        name_list=os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "vacancy_list.json"),
    ):
        super().__init__(name, city, salary, requirement, schedule, experience)
        self.__name_list = name_list

    def get_name_list(self):
        return self.__name_list

    def save_vacancy(self, vacancy_list):
        """Метод сохранения вакансий"""
        if os.path.exists(self.get_name_list()):
            with open(self.get_name_list(), "r", encoding="utf-8") as file:
                data = json.load(file)
            for i in vacancy_list:
                if i not in data:
                    data.append(i)
            with open(self.get_name_list(), "a", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            with open(self.get_name_list(), "a", encoding="utf-8") as file:
                json.dump(vacancy_list, file, indent=4, ensure_ascii=False)

    def get_data(self, keyword):
        """Метод выборки вакансий"""
        with open(self.get_name_list(), "r", encoding="utf-8") as file:
            data_json_file = json.load(file)
            for vacancy in data_json_file:
                if (
                    self.name in vacancy.get("name")
                    and self.city in vacancy["area"].get("name")
                    and self.salary in vacancy.get("salary")
                    and self.requirement in vacancy["snippet"].get("requirement")
                    and self.schedule in vacancy["schedule"].get("name")
                    and self.experience in vacancy["experience"].get("name")
                ):
                    return data_json_file
                else:
                    continue

    def del_vacancy(self, del_json):
        """Метод удаления вакансий"""
        data_del = []
        with open(self.get_name_list(), "r", encoding="utf-8") as file:
            data = json.load(file)
        for i in data:
            if del_json != i["city"] and del_json not in i["name"] and del_json not in i["salary"]:
                data_del.append(i)
        with open(self.get_name_list(), "w", encoding="utf-8") as file:
            json.dump(data_del, file, indent=4, ensure_ascii=False)
        return data_del
