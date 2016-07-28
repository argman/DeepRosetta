from abc import ABCMeta, abstractmethod, abstractproperty

class BaseImporter:
    """ Abstract class modeling a base importer

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def load(self, file_path):
        """ Loads a given model file.
            It will call the subroutine to load an specific format

        :param file_path: path to the model file
        """
        return NotImplementedError