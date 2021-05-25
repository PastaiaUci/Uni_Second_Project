from exceptii import *


class ValidatoriStudent(object):

    def valideaza(self, student):
        erori = ""
        if student.get_student_id() < 0:
            erori += "id invalid\n"
        if student.get_nume() == "":
            erori += "nume invalid\n"
        if student.get_grup() < 0:
            erori += "grup invalid\n"
        if len(erori):
            raise ValidError(erori)

    def valideaza1(self, problema):
        erori = ""
        if problema.get_problema_id() < 0:
            erori += "id invalid\n"
        if problema.get_descriere() == "":
            erori += "descriere invalida\n"
        if problema.get_deadline() == "":
            erori += "deadline invalid\n"
        if len(erori):
            raise ValidError(erori)
