import json
import os.path
from src.adding_vacancies import AddingVacancies


class AddVacanciesJSON(AddingVacancies):

    def __init__(self, name_list="data/vacancy_list.json"):
        self.name_list = name_list

    def save_vacancy(self, vacancy_list):
        if os.path.exists(self.name_list):
            with open(self.name_list, 'r', encoding="utf-8") as file:
                data = json.load(file)
            for i in vacancy_list:
                if i not in data:
                    data.append(i)
            with open(self.name_list, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4,
                          ensure_ascii=False)
        else:
            with open(self.name_list, 'w', encoding="utf-8") as file:
                json.dump(vacancy_list, file, indent=4, ensure_ascii=False)

    def del_vacancy(self, del_json):
        data_del = []
        with open(self.name_list, 'r', encoding="utf-8") as file:
            data = json.load(file)
        for i in data:
            if del_json != i['city'] and del_json not in i['name'] and del_json not in i['description']:
                data_del.append(i)
        with open(self.name_list, 'w', encoding="utf-8") as file:
            json.dump(data_del, file, indent=4,
                      ensure_ascii=False)
        return data_del
