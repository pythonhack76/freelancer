class Base:

    def func(self):
        print("base func")

    def __func(self):
        print("metodo privato")

class Derivato(Base):
    def __init__(self):

        Base.__init__(self)

        print("\n Dentro inserisco derivato classe")
        self.fun()

    def call_private(self):
        self.__func()


        
