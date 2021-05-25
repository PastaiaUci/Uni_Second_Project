class Student(object):

    def __init__(self, student_id, nume, grup):
        self.__student_id = student_id
        self.__nume = nume
        self.__grup = grup

    def set_nume(self, nume):
        self.__nume = nume

    def set_grup(self, grup):
        self.__grup = grup

    def get_student_id(self):
        return self.__student_id

    def get_nume(self):
        return self.__nume

    def get_grup(self):
        return self.__grup

    def __str__(self):
        return str(self.__student_id) + " " + self.__nume + " " + str(self.__grup)


class Problema(object):

    def __init__(self, id_problema, descriere, deadline):
        self.__id_problema = id_problema
        self.__descriere = descriere
        self.__deadline = deadline

    def set_nume(self, __descriere):
        self.____descriere = __descriere

    def set_grup(self, deadline):
        self.__deadline = deadline

    def get_problema_id(self):
        return self.__id_problema

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def __str__(self):
        return str(self.__id_problema) + " " + self.__descriere + " " + str(self.__deadline)


class Asignare(object):
    def __init__(self, student, problema, nota):
        self.__student = student
        self.__problema = problema
        self.__nota = nota

    def set_student(self, student):
        self.__student = student

    def set_problema(self, problema):
        self.__problema = problema

    def set_nota(self, nota):
        self.__nota = nota

    def get_student(self):
        return self.__student

    def get_problema(self):
        return self.__problema

    def get_nota(self):
        return self.__nota

    def __str__(self):
        return str(self.__student) + " " + str(self.__problema) + " " + str(self.__nota)
