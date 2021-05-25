from exceptii import *
from validatori import *
from random import *
from entitati import *
from operator import itemgetter
import os
from Sortari import *


class RepositoryStudenti(object):
    def __init__(self):
        self.elems = []
        self.__asi = []

    def size(self):
        return len(self.elems)

    def adauga(self, student):
        ok = 0
        for st in self.elems:
            if st.get_student_id() == student.get_student_id():
                ok += 1
        if ok == 1:
            raise RepoError("element existent\n")
        else:
            self.elems.append(student)

    def modifica(self, student_nou):
        ok = 0
        for st in self.elems:
            if st.get_student_id() == student_nou.get_student_id():
                ok += 1
        if ok == 0:
            raise RepoError("element inexistent\n")
        else:
            for i in range(len(self.elems)):
                if self.elems[i].get_student_id() == student_nou.get_student_id():
                    self.elems[i] = student_nou
                    return

    def cauta(self, key_student):
        """
        Functia nu este constanta din cauza if-ului

        caz favorabil : key_student e pe prima pozitie (omega) T(n) =  10 € Θ(1)

        caz mediu : key_student e pe o pozitie aleatorie   T(n)  =  [n(n+1)/2]/n = (n+1)/2 € Θ(n)

        caz nefavorabil : key_student e pe ultimul loc T(n) = 1+9n € Θ(n)


        Complexitatea overall : O(n)

        """

        n = 0
        for st in self.elems:
            n += 1
            if st.get_student_id() == key_student:
                print("Student existent pe pozitia " + str(n)+"\n")
                print(st)
                return
        raise RepoError("element inexistent\n")

    def cauta_nume(self, key_student):
        ok = 0
        for st in self.elems:
            if st.get_nume() == key_student:
                ok += 1
        if ok == 0:
            raise RepoError("element inexistent\n")
        n = 0
        for elem in self.elems:
            n = n+1
            if elem.get_nume() == key_student:
                print("Student existent pe pozitia " + str(n)+"\n")
                print(elem)
                return

    def sterge(self, key_student, array):
        ok = 0
        for st in self.elems:
            if st.get_student_id() == key_student:
                ok += 1
        if ok == 0:
            raise RepoError("element inexistent\n")
        elif array[0].get_student_id() == key_student:
            del array[0]
            return
        else:
            return sterge(array[0], key_student) or array(array[1:], key_student)
        """
            for i in range(len(self.elems)):
                if self.elems[i].get_student_id() == key_student:
                    del self.elems[i]
                    return
        """

    def get_all(self):
        return self.elems[:]

    def generare(self, cati):
        lista_nume = ['David', 'Andrei', 'Adi', 'Matei',
                      'Teodor', 'Gabriel', 'Rafael', 'Gicu']
        while cati != 0:
            idul = randint(0, 50)
            care_nume = randint(0, 7)
            grupa = randint(200, 220)
            nume = lista_nume[care_nume]
            student = Student(idul, nume, grupa)

            ok = 0
            for st in self.elems:
                if st.get_student_id() == student.get_student_id():
                    ok += 1
            if ok == 1:
                print("exista un student cu id ul acesta")
                continue
            else:
                self.elems.append(student)
                cati = cati-1


class RepositoryProbleme(object):
    def __init__(self):
        self.prb = []

    def size(self):
        return len(self.prb)

    def adauga1(self, problema):
        ok = 0
        for st in self.prb:
            if st.get_problema_id() == problema.get_problema_id():
                ok += 1
        if ok == 1:
            raise RepoError("element existent\n")
        else:
            self.prb.append(problema)

    def modifica1(self, problema_noua):
        ok = 0
        for st in self.prb:
            if st.get_problema_id() == problema_noua.get_problema_id():
                ok += 1
        if ok == 0:
            raise RepoError("element inexistent\n")
        else:
            for i in range(len(self.prb)):
                if self.prb[i].get_problema_id() == problema_noua.get_problema_id():
                    self.prb[i] = problema_noua
                    return

    def sterge1(self, problema, array):
        ok = 0
        for st in self.prb:
            if st.get_problema_id() == problema:
                ok += 1
        if ok == 0:
            raise RepoError("element inexistent\n")
        elif array[0].get_problema_id() == problema:
            del array[0]
            return
        else:
            return sterge1(array[0], problema) or array(array[1:], problema)
        """
        for i in range(len(self.prb)):
            if self.prb[i].get_problema_id() == problema:
                del self.prb[i]
                return
        """

    def get_all(self):
        return self.prb[:]

    def cauta1(self, key_student):
        ok = 0
        for st in self.prb:
            if st.get_problema_id() == key_student:
                ok += 1
        if ok == 0:
            raise RepoError("element inexistent\n")
        n = 0
        for elem in self.prb:
            n = n+1
            if elem.get_problema_id() == key_student:
                print("problema existenta pe pozitia " + str(n)+"\n")
                print(elem)
                return

    def generare1(self, cate):
        lista_descriere = ['fd', 'gf', 'bd', 'yhgt',
                           'sgt', 'yj6', 'srgt', 'by5t']
        lista_deadline = ['1/1/2020', '2/3/2031', '1/4/2004',
                          '4/12/2015', '4/42020', '5/5/2020', '7/7/2021', '1/04/2019']
        while cate != 0:
            care_descriere = randint(0, 7)
            care_deadline = randint(0, 7)
            idul = randint(0, 50)
            descriere = lista_descriere[care_descriere]
            deadline = lista_deadline[care_deadline]

            problema = Problema(idul, descriere, deadline)

            ok = 0
            for st in self.prb:
                if st.get_problema_id() == problema.get_problema_id():
                    ok += 1
            if ok == 1:
                print("element existent\n")
                continue
            else:
                self.prb.append(problema)
                cate = cate-1


class FileRepoStudenti(RepositoryStudenti):
    def __init__(self, filename):
        self.filename = filename
        RepositoryStudenti.__init__(self)

    def ordonare_studenti(self):
        sort = Sortari()
        x = sort.ShakerSort(array=RepositoryStudenti.get_all(self),
                            key1=lambda x: x.get_nume(), key2=lambda x: x.get_student_id())
        for x1 in x:
            print(x1)

    def write_in_directory(self, student):
        open(self.filename, 'w').close()
        my_file = open(self.filename, "a+")
        for student in self.elems:
            my_file.write(str(student.get_student_id())+"," +
                          student.get_nume() + "," + str(student.get_grup()) + "\n")

    def write_in_directory1(self):
        open(self.filename, 'w').close()
        my_file = open(self.filename, "a+")
        for student in self.elems:
            my_file.write(str(student.get_student_id())+"," +
                          student.get_nume() + "," + str(student.get_grup())+"\n")

    def write_all(self):
        open(self.filename, 'w').close()
        my_file = open(self.filename, "a+")
        for student in self.elems:
            my_file.write(str(student.get_student_id())+"," +
                          student.get_nume() + "," + str(student.get_grup())+"\n")

    def rewrite_elems(self):
        self.elems.clear()
        my_file = open(self.filename, "r")
        lines = my_file.readlines()
        for line in lines:
            line.strip()
            if line != "" and line != "\n":
                parts = line.split(",")
                student = Student(int(parts[0]), parts[1], int(parts[2]))
                self.elems.append(student)
        my_file.close()

    def adauga(self, student):
        self.rewrite_elems()
        RepositoryStudenti.adauga(self, student)
        self.write_in_directory(student)

    def get_all(self):
        self.rewrite_elems()
        return RepositoryStudenti.get_all(self)

    def size(self):
        self.rewrite_elems()
        return RepositoryStudenti.size(self)

    def cauta(self, key_student):
        self.rewrite_elems()
        RepositoryStudenti.cauta(self, key_student)

    def modifica(self, student_nou):
        self.rewrite_elems()
        RepositoryStudenti.modifica(self, student_nou)
        self.write_in_directory1()

    def sterge(self, key_student):
        self.rewrite_elems()
        RepositoryStudenti.sterge(self, key_student, self.elems)
        self.write_all()


class FileRepoProbleme(RepositoryProbleme):

    def __init__(self, filename):
        self.filename = filename
        RepositoryProbleme.__init__(self)

    def write_in_directory(self):
        open(self.filename, 'w').close()
        my_file = open(self.filename, "a+")
        for problema in self.prb:
            my_file.write(str(problema.get_problema_id())+"," +
                          problema.get_descriere() + "," + str(problema.get_deadline()) + "\n")

    def rewrite_prb(self):
        self.prb.clear()
        my_file = open(self.filename, "r")
        lines = my_file.readlines()
        for line in lines:
            line.strip()
            if line != "" and line != "\n":
                parts = line.split(",")
                parts[2] = parts[2].rsplit()
                problema = Problema(int(parts[0]), parts[1], parts[2][0])
                self.prb.append(problema)
        my_file.close()

    def adauga1(self, problema):
        self.rewrite_prb()
        RepositoryProbleme.adauga1(self, problema)
        self.write_in_directory()

    def get_all(self):
        self.rewrite_prb()
        return RepositoryProbleme.get_all(self)

    def size(self):
        self.rewrite_prb()
        return RepositoryProbleme.size(self)

    def cauta1(self, key_student):
        self.rewrite_prb()
        RepositoryProbleme.cauta1(self, key_student)

    def modifica1(self, student_nou):
        self.rewrite_prb()
        RepositoryProbleme.modifica1(self, student_nou)
        self.write_in_directory()

    def sterge1(self, key_student):
        self.rewrite_prb()
        RepositoryProbleme.sterge1(self, key_student, self.prb)
        self.write_in_directory()


class RepositoryAsignari(RepositoryStudenti, RepositoryProbleme):

    def __init__(self, student, problema):
        self.student = student
        self.problema = problema
        self.asg = []

    def asigneaza(self, idul, numar, nota):
        ok = 0
        for st in self.student.elems:
            if st.get_student_id() == idul:
                ok += 1
        if ok == 0:
            raise RepoError("student  inexistent\n")
        ok = 0
        for st in self.problema.prb:
            if st.get_problema_id() == numar:
                ok += 1
        if ok == 0:
            raise RepoError("problema inexistent\n")
        if nota < 1 or nota > 10:
            raise RepoError("nota trebuie sa fie intre 1 si 10")
        else:
            asignare = Asignare(idul, numar, nota)
            self.asg.append(asignare)

    def get_all_asg(self):
        return self.asg[:]

    def size_asg(self):
        return len(self.asg)

    def sterge_asignare_problema(self, id_problema):
        for x in self.asg[:]:
            if int(x.get_problema()) == id_problema:
                self.asg.remove(x)


class FileRepoAsignari(RepositoryAsignari):
    def __init__(self, filename, student, problema):
        self.filename = filename
        super().__init__(student, problema)

    def write_in_directory(self):
        open(self.filename, 'w').close()
        my_file = open(self.filename, "a+")
        for asignare in self.asg:
            my_file.write(str(asignare.get_student())+"," +
                          str(asignare.get_problema()) + "," + str(asignare.get_nota()) + "\n")

    def rewrite_asg(self):
        self.asg.clear()
        my_file = open(self.filename, "r")
        lines = my_file.readlines()
        for line in lines:
            line.strip()
            if line != "" and line != "\n":
                parts = line.split(",")
                parts[2] = parts[2].rsplit()
                asignare = Asignare(int(parts[0]), int(
                    parts[1]), int(parts[2][0]))
                self.asg.append(asignare)
        my_file.close()

    def asigneaza(self, idul, numar, nota):
        self.rewrite_asg()
        RepositoryAsignari.asigneaza(self, idul, numar, nota)
        self.write_in_directory()

    def size_asg(self):
        self.rewrite_asg()
        return RepositoryAsignari.size_asg(self)

    def get_all_asg(self):
        self.rewrite_asg()
        return RepositoryAsignari.get_all_asg(self)

    def sterge_asignare_problema(self, id_problema):
        self.rewrite_asg()
        RepositoryAsignari.sterge_asignare_problema(self, id_problema)
        self.write_in_directory()


class RepositoryStatistici(RepositoryAsignari):
    def __init__(self, ordo):
        self.ordo = ordo
        self.lista_ordonari = []
        self.lista_medie = []
        self.lista_grupe = []

    def rewrite_elems(self):
        x = r"C:/Users/David/Desktop/GestionareLaboratoare/studenti.txt"
        self.ordo.student.elems.clear()
        my_file = open(x, "r")
        lines = my_file.readlines()
        for line in lines:
            line.strip()
            if line != "" and line != "\n":
                parts = line.split(",")
                student = Student(int(parts[0]), parts[1], int(parts[2]))
                self.ordo.student.elems.append(student)
        my_file.close()

    def get_a_doua_chestie(self, x):
        return x[2]

    def ordonare_nota(self):

        self.rewrite_elems()
        self.lista_ordonari.clear()
        for asignare in self.ordo.asg:
            lista = []
            lista.append(asignare.get_student())
            lista.append(asignare.get_problema())
            lista.append(asignare.get_nota())
            self.lista_ordonari.append(lista)
        for asignare in self.lista_ordonari:
            for student in self.ordo.student.elems:
                if asignare[0] == student.get_student_id():
                    asignare[0] = student.get_nume()

        # self.lista_ordonari.sort(key=lambda x: x[2])
        sortari = Sortari()
        sortari.SelectionSort(array=self.lista_ordonari,
                              key1=lambda x: self.get_a_doua_chestie(x), key2=lambda x: x[1])

    def get_ordonari_nota(self):
        return self.lista_ordonari[:]

    def get_medie_studenti(self):
        return self.lista_medie[:]

    def get_ordonari_nume(self):
        return self.lista_ordonari[:]

    def ordonare_nume(self):
        self.rewrite_elems()
        self.lista_ordonari.clear()
        for asignare in self.ordo.asg:
            lista = []
            lista.append(asignare.get_student())
            lista.append(asignare.get_problema())
            lista.append(asignare.get_nota())
            self.lista_ordonari.append(lista)
        for asignare in self.lista_ordonari:
            for student in self.ordo.student.elems:
                if asignare[0] == student.get_student_id():
                    asignare[0] = student.get_nume()
        # self.lista_ordonari.sort()
        Sortari.SelectionSort(self, array=self.lista_ordonari)

    def medie_studenti(self):
        self.rewrite_elems()
        self.lista_medie.clear()
        copie_repo = self.ordo.asg.copy()
        lista_id = []
        for i in range(0, len(copie_repo)):
            s = 0
            idul = copie_repo[i].get_student()
            counter = 0
            for x in copie_repo:
                if x.get_student() == idul:
                    if x.get_student() not in lista_id:
                        s += x.get_nota()
                        counter += 1
            if counter != 0:
                lista_id.append(idul)
                media = s / counter
                lista = []
                if media < 5:
                    for student in self.ordo.student.elems:
                        if copie_repo[i].get_student() == student.get_student_id():
                            lista.append(student.get_nume())
                    lista.append(media)
                    self.lista_medie.append(lista)

    def ordonare_grupe(self):
        self.rewrite_elems()
        self.lista_grupe.clear()
        for x in self.ordo.student.elems:
            lista = []
            lista.append(x.get_grup())
            self.lista_grupe.append(lista)
        for x in self.lista_grupe:
            counter = 0
            for student in self.ordo.student.elems:
                if x[0] == student.get_grup():
                    id_student = student.get_student_id()
                    for i in self.ordo.asg:
                        if i.get_student() == id_student:
                            if i.get_nota() < 7:
                                counter = counter + 1
            x.append(counter)
        self.lista_grupe.sort(key=lambda y: y[1])
        print(self.lista_grupe)
