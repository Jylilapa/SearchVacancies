from abc import ABC, abstractmethod

class AddingVacancies(ABC):

    @abstractmethod
    def save_vacancy(self, vacancy_list):
        pass

    @abstractmethod
    def del_vacancy(self, del_json):
        pass
