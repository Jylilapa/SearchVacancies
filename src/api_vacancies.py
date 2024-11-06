from abc import ABC, abstractmethod

class ApiVacancies(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

