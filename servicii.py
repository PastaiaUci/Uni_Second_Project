from entitati import *
from random import *


class ServiceStudenti(object):
    def __init__(self, repo, valid):
        self.__repo = repo
        self.__valid = valid

    def adauga_student(self, id, nume, grup):
        student = Student(id, nume, grup)
        self.__valid.valideaza(student)
        self.__repo.adauga(student)

    def numar_studenti(self):
        return self.__repo.size()

    def get_studenti(self):
        return self.__repo.get_all()

    def sterge_student(self, student_id):
        self.__repo.sterge(student_id)

    def cauta_student(self, student_id):
        self.__repo.cauta(student_id)

    def cauta_student_nume(self, nume):
        self.__repo.cauta_nume(nume)

    def ordonare_studenti(self):
        self.__repo.ordonare_studenti()

    def modifica_student(self, student_id, nume, grup):
        student = Student(student_id, nume, grup)
        self.__repo.modifica(student)

    def generare_studenti(self, cati):
        self.__repo.generare(cati)


class ServiceProbleme(object):
    def __init__(self, repo1, valid1):
        self.__repo1 = repo1
        self.__valid = valid1

    def adauga_problema(self, id1, descriere, deadline):
        problema = Problema(id1, descriere, deadline)
        self.__valid.valideaza1(problema)
        self.__repo1.adauga1(problema)

    def numar_probleme(self):
        return self.__repo1.size()

    def get_probleme(self):
        return self.__repo1.get_all()

    def modifica_problema(self, id1, descriere, deadline):
        problema = Problema(id1, descriere, deadline)
        self.__repo1.modifica1(problema)

    def sterge_problema(self, id1):
        self.__repo1.sterge1(id1)

    def cauta_problema(self, problema_id):
        self.__repo1.cauta1(problema_id)

    def generare_probleme(self, cate):
        self.__repo1.generare1(cate)


class ServiceAsignari(object):
    def __init__(self, repo2):
        self.__repo2 = repo2

    def asignare_problema(self, idul, numar, nota):
        self.__repo2.asigneaza(idul, numar, nota)

    def numar_asignari(self):
        return self.__repo2.size_asg()

    def get_asignari(self):
        return self.__repo2.get_all_asg()

    def sterge_asignare_problema(self, care):
        self.__repo2.sterge_asignare_problema(care)


class ServiceStats(object):
    def __init__(self, repo4):
        self.__repo4 = repo4

    def ordonare_studenti(self):
        return self.__repo4.ordonare_nota()

    def ordonare_nume(self):
        return self.__repo4.ordonare_nume()

    def medie_studenti(self):
        return self.__repo4.medie_studenti()

    def ordonare_grupe(self):
        return self.__repo4.ordonare_grupe()

    def get_ordonari_nume(self):
        return self.__repo4.get_ordonari_nume()

    def get_ordonari_studenti(self):
        return self.__repo4.get_ordonari_nota()

    def get_medie_studenti(self):
        return self.__repo4.get_medie_studenti()
