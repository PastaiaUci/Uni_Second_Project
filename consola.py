from exceptii import *


class UI(object):
    def __init__(self, srv, rsv, asg, stats):
        self.__stats = stats
        self.__srv = srv
        self.__rsv = rsv
        self.__asg = asg
        self.__comezi = {"adauga_student": self.__UI_adauga_student,  # da
                         "adauga_problema": self.__UI_adauga_problema,  # da
                         "print_studenti": self.__UI_print_studenti,  # da
                         "print_probleme": self.__UI_print_probleme,  # da
                         "sterge_student": self.__UI_sterge_student,  # da
                         "sterge_problema": self.__UI_sterge_problema,  # da
                         "modifica_student": self.__UI_modifica_student,  # da
                         "modifica_problema": self.__UI_modifica_problema,  # da
                         "cauta_student": self.__UI_cauta_student,  # da
                         "cauta_problema": self.__UI_cauta_problema,  # da
                         "cauta_student_nume": self.__UI_cauta_student_nume,  # da
                         "asignare_problema": self.__UI_asignare_problema,  # da
                         "print_asignari": self.__UI_print_asignari,  # da
                         "ordonare_nota": self.__UI_ordonare_studenti,
                         "ordonare_nume": self.__UI_ordonare_nume,
                         "medie_studenti": self.__UI_medie_studenti,
                         "ordonare_grupe": self.__UI_statistici_grupe,
                         "print_ordonare_nume": self.__UI_print_ordonare_nume,
                         "print_ordonare_nota": self.__UI_print_ordonare_studenti,
                         "print_medie_studenti": self.__UI_print_medie_studenti,
                         "sortare_studenti": self.__UI_sortare_studenti}

    def __UI_statistici_grupe(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asiganri de note in lista")
        else:
            self.__stats.ordonare_grupe()

    def __UI_sortare_studenti(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asiganri de note in lista")
        else:
            self.__srv.ordonare_studenti()

    def __UI_print_ordonare_studenti(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asignari de note")
        else:
            ordonari = self.__stats.get_ordonari_studenti()
            for ordonare in ordonari:
                print(ordonare)

    def __UI_print_medie_studenti(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asignari de note")
        else:
            medii = self.__stats.get_medie_studenti()
            for medie in medii:
                print(medie)

    def __UI_print_ordonare_nume(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asignari de note")
        else:
            ordonari = self.__stats.get_ordonari_nume()
            for ordonare in ordonari:
                print(ordonare)

    def __UI_ordonare_studenti(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asignari de note")
        else:
            self.__stats.ordonare_studenti()

    def __UI_medie_studenti(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asignari de note")
        else:
            self.__stats.medie_studenti()

    def __UI_ordonare_nume(self):
        if self.__asg.numar_asignari() == 0:
            print("nu exista asignari de note")
        else:
            self.__stats.ordonare_nume()

    def __UI_adauga_student(self):  # da
        student_id = int(input("Introduceti id-ul studentului:"))
        nume = input("Introduceti numele studentului:")
        grup = int(input("Introduceti grupa studentului:"))
        self.__srv.adauga_student(student_id, nume, grup)

    def __UI_adauga_problema(self):  # da
        id_problema = int(input("Introduceti numarul problemei:"))
        descriere = input("Descrierea problemei:")
        deadline = input("Introduceti un deadline:")
        self.__rsv.adauga_problema(id_problema, descriere, deadline)

    def __UI_print_studenti(self):  # da
        if self.__srv.numar_studenti() == 0:
            print("nu exista stundeti in lista")
        studenti = self.__srv.get_studenti()
        for student in studenti:
            print(student)

    def __UI_print_probleme(self):  # da
        if self.__rsv.numar_probleme() == 0:
            print("nu exista probleme in lista")
        probleme = self.__rsv.get_probleme()
        for problema in probleme:
            print(problema)

    def __UI_modifica_student(self):  # da
        if self.__srv.numar_studenti() == 0:
            print("nu exista stundeti in lista")
        else:
            student_id = int(input("Introduceti id-ul   studentului:"))
            nume = input("Introduceti numele nou al studentului:")
            grup = int(input("Introduceti grupa noua a studentului:"))
            self.__srv.modifica_student(student_id, nume, grup)

    def __UI_modifica_problema(self):  # da
        if self.__rsv.numar_probleme() == 0:
            print("nu exista probleme in lista")
        else:
            id_problema = int(input("Introduceti numarul problemei:"))
            descriere = input("Descrierea noua a problemei:")
            deadline = input("Introduceti un nou deadline:")
            self.__rsv.modifica_problema(id_problema, descriere, deadline)

    def __UI_sterge_problema(self):  # da
        if self.__rsv.numar_probleme() == 0:
            print("nu exista probleme in lista")
        else:
            id_problema = int(input("Introduceti numarul problemei:"))
            self.__rsv.sterge_problema(id_problema)
            self.__asg.sterge_asignare_problema(id_problema)

    def __UI_sterge_student(self):  # da
        if self.__srv.numar_studenti() == 0:
            print("nu exista studenti in lista")
        else:
            id_student = int(input("Introduceti id-ul studentului:"))
            self.__srv.sterge_student(id_student)

    def __UI_cauta_student(self):  # da
        if self.__srv.numar_studenti() == 0:
            print("nu exista stundeti in lista")
        else:
            student_id = int(input("Introduceti id-ul studentului:"))
            self.__srv.cauta_student(student_id)

    def __UI_cauta_student_nume(self):  # da
        if self.__srv.numar_studenti() == 0:
            print("nu exista stundeti in lista")
        else:
            nume = input("Introduceti numele studentului:")
            self.__srv.cauta_student_nume(nume)

    def __UI_cauta_problema(self):  # da
        if self.__rsv.numar_probleme() == 0:
            print("nu exista probleme in lista")
        else:
            problema_id = int(input("Introduceti id-ul problemei:"))
            self.__rsv.cauta_problema(problema_id)

    def __UI_asignare_problema(self):  # da
        if self.__rsv.numar_probleme() == 0:
            print("nu exista probleme in lista")
        if self.__srv.numar_studenti() == 0:
            print("nu exista stundeti in lista")
        else:
            id_ul = int(input("Introduceti id-ul studentului:"))
            problema = int(input("Introduceti numarul problemei:"))
            nota = int(input("Introduceti nota studentului:"))
            self.__asg.asignare_problema(id_ul, problema, nota)

    def __UI_print_asignari(self):  # da
        if self.__asg.numar_asignari() == 0:
            print("nu exista asignari")
        asignari = self.__asg.get_asignari()
        for asignare in asignari:
            print(asignare)

    def run(self):

        print("       Menu:  ")
        print("  1.Adauga student:adauga_student//adauga_problema")
        print("  2.Afiseaza studenti:print_studenti//print_probleme")
        print("  3.Sterge un student:sterge_student//sterge_problema")
        print("  4.Cauta un student:cauta_student//cauta_problema")
        print("  5.Modifica un student:modifica_student//modifica_problema")
        print("  6.Generare:generare_studenti/generare_note")
        print("  7.Asignare_problema:asignare_problema")
        print("  9.Asignare_problema:asignare_problema")
        print("  10.Orodnare dupa nume:ordonare_nume")
        print("  11.Ordonare dupa nota:ordonare_nota")
        print("  12.Iesire:exit")
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            if cmd in self.__comezi:
                try:
                    self.__comezi[cmd]()
                except ValueError:
                    print("valoare numerica invalida\n")
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)

            else:
                print("comanda invalida!")
