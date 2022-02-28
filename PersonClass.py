class Person:

    def __init__(self,name,address,telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone
    
    def show_person(self):
        print('Name:', self.__name,"Address:", self.__address,"Telephone:", self.__telephone)

class Customer(Person):
    def __init__(self):
        Person.__init__(self,'Customer Number')

    def mailing_list(self):
        self.__mailing_list
        print("Do you want to be on the mailing list?")

class Print_Person(Person):
    def __init__(self):
        print(self.__name, self.__address, self.__telephone, self.__mailing_list)
