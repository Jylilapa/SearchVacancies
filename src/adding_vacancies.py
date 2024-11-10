from abc import ABC, abstractmethod


class AddingVacancies(ABC):
    """Абстрактный метод сохранения, удаления и выборки вакансий с JSON файла"""

    @abstractmethod
    def save_vacancy(self, vacancy_list):
        pass

    @abstractmethod
    def del_vacancy(self, del_json):
        pass

    @abstractmethod
    def get_data(self, keyword):
        pass
