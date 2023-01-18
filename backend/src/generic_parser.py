import abc


class MedicalDocParser(metaclass=abc.ABCMeta):
    def __int__(self, text):
        # takes input as document text extracted from pytesseract
        self.text = text

    @abc.abstractmethod
    def parse(self):
        """
        Here abstract_method is used becoz we want that if MedicalDocParser class has any child class,
        it should have this method "parse" in it otherwise that child class cannot be executed.
        """
        pass
