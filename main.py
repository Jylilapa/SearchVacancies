from src.load_vacancies import HeadHunter
from src.add_vacancies_json import AddVacanciesJSON
from src.vacancy import Vacancy, top_vacancy, filter_vacancy


def user_interaction():

    search_query = input("Введите поисковый запрос: ")
    hh = HeadHunter()
    city_search = input("Введите город для поиска вакансии: ")
    hh.load_vacancies(search_query)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary = int(input("Введите желаемую зарплату: "))
    requirement = input("Введите ключевые слова в описании: ")
    schedule = input("Введите график - полная занятость, гибкий график и т.д.: ")
    experience = input("Введите опыт работы - без опыта, 1 год и т.д.: ")
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    vacancy = Vacancy(search_query, city_search, salary, hh.vacancies, requirement, schedule, experience)
    res_city = vacancy.filter_city()
    res_salary = vacancy.__le__(salary, res_city)
    result_fil_words = filter_vacancy(res_salary, filter_words)
    sd = AddVacanciesJSON()
    sd.save_vacancy(result_fil_words)
    result_of_top = top_vacancy(top_n, result_fil_words)
    del_vacancy = input("Требуется что-нибудь удалить из файла? 'Да,Нет': ")
    if del_vacancy == 'Да':
        del_json = input('Введите ключевые слова для удаления вакансий(Название вакансии,город или зарплата): ')
        sd.del_vacancy(del_json)

    return result_of_top


if __name__ == "__main__":
    user_interaction()
