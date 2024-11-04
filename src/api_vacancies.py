from abc import ABC, abstractmethod

class ApiVacancies(ABC):

    @classmethod
    @abstractmethod
    def load_vacancies(cls, keyword):
        pass

