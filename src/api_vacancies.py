from abc import ABC, abstractmethod


class ApiVacancies(ABC):
    """Абстрактный класс получения вакансий по API"""

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
