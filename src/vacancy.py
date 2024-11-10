import os.path
from src.load_vacancies import HeadHunter


class Vacancy(HeadHunter):
    __slots__ = (
        "name",
        "city",
        "salary",
        "requirement",
        "responsibility",
        "schedule",
        "experience",
        "result",
    )

    def __init__(
        self,
        keyword,
        name,
        city,
        salary,
        requirement,
        schedule,
        experience,
        data_hh=os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "vacancy_list.json"),
    ):
        super().__init__()
        self.name = name
        self.city = city
        self.salary = salary
        self.requirement = requirement
        self.schedule = schedule
        self.experience = experience
        self.result = []
        self.data_hh = data_hh
        self.__filter_vacancy(self.data_hh)

    def __filter_vacancy(self, data_hh):
        for i in data_hh:
            if i["salary"] is not None:
                self.result.append(
                    {
                        "name": i["name"],
                        "city": i["area"]["name"],
                        "salary": ({"from": i["salary"]["from"], "to": i["salary"]["to"]}),
                        "requirement": i["snippet"]["requirement"],
                        "schedule": i["schedule"]["name"],
                        "experience": i["experience"]["name"],
                    }
                )
                return self.result

            elif i["salary"]["from"] is None:
                self.result.append(
                    {
                        "name": i["name"],
                        "city": i["area"]["name"],
                        "salary": {"from": 0, "to": i["salary"]["to"]},
                        "requirement": i["snippet"]["requirement"],
                        "schedule": i["schedule"]["name"],
                        "experience": i["experience"]["name"],
                    }
                )
                return self.result
            elif i["salary"]["to"] is None:
                self.result.append(
                    {
                        "name": i["name"],
                        "city": i["area"]["name"],
                        "salary": {"from": i["salary"]["from"], "to": 0},
                        "requirement": i["snippet"]["requirement"],
                        "schedule": i["schedule"]["name"],
                        "experience": i["experience"]["name"],
                    }
                )
                return self.result

    def filter_city(self):
        result_city = []
        for i in self.result:
            if self.city == i["city"]:
                result_city.append(i)
        return result_city

    def __le__(self, other, my_list):
        res_salary = []
        for i in my_list:
            if other <= i["salary"]["from"]:
                res_salary.append(i)
        return res_salary


def top_vacancy(number, my_list):
    if number == "":
        return my_list
    else:
        return my_list[0 : int(number)]


def filter_vacancy(my_list, words_list):
    fin_list = []
    for index in my_list:
        for i in words_list:
            if index["name"] is None:
                continue
            elif i in index["name"]:
                fin_list.append(index)
    return fin_list
