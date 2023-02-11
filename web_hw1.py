from abc import abstractmethod, ABC


class InfoBaseClass(ABC):
    @abstractmethod
    def help_info_ab(self, *args, **kwargs):
        pass

    @abstractmethod
    def help_info_nb(self, *args, **kwargs):
        pass

    @abstractmethod
    def start_info_ab(self):
        pass

    @abstractmethod
    def start_info_nb(self):
        pass

    @abstractmethod
    def start_info_sf(self):
        pass

    @abstractmethod
    def start_info_menu(self):
        pass
