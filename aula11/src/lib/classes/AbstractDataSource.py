from abc import ABC, abstractmethod

class AbstractDataSource(ABC):
    def __init__(self):
        pass
     
    @abstractmethod #esse decorador indica que é um método abstrato, ou seja, precisa estar implementado na próxima classe ou o código quebra
    #garante que os desenvolvedores implementem esses métodos em classes filhas ou netas
    def start(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Método não implementado")

    def hello_world(self):
        print('Hello World')