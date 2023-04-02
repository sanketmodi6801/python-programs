from abc import ABC, abstractmethod
class myclass(ABC):
    @abstractmethod
    def MyMethod(self):
        pass

    def __init__(self):
        print("Hii, this is a constructor haha..!!")


class myclass2(myclass):
    def MyMethod(self):
        pass


sanket = myclass2()
