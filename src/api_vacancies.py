from abc import ABC, abstractmethod

class ApiVacancies(ABC):

    @classmethod
    @abstractmethod
    def file_worker(cls, *args, **kwargs):
        pass

