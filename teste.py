from entitati import *
from validatori import *
from exceptii import *
from repos import *
from servicii import *
import unittest


class Teste(unittest.TestCase):

    def setUp(self):
        open("studenti_teste.txt", 'w').close()
        open("probleme_teste.txt", 'w').close()
        self.student1 = Student(1, 'Schafer', 214)
        self.student2 = Student(2, 'Smith', 211)
        self.prb1 = Problema(1, "da", "1/1/2020")
        self.prb2 = Problema(2, "nu", "1/2/2020")

    def test_domeniu_studenti(self):
        self.assertEqual(self.student1.get_grup(), 214)
        self.assertEqual(self.student1.get_student_id(), 1)
        self.assertEqual(self.student1.get_nume(), 'Schafer')
        self.assertEqual(str(self.student1), '1 Schafer 214')
        self.student2 = Student(self.student1.get_student_id(), None, 0)
        assert (self.student1.__eq__(self.student2))

    def test_domeniu_prb(self):
        self.assertEqual(self.prb1.get_problema_id(), 1)
        self.assertEqual(self.prb1.get_descriere(), "da")
        self.assertEqual(self.prb1.get_deadline(),  "1/1/2020")
        self.assertEqual(str(self.prb1), '1 da 1/1/2020')
        self.prb2 = Problema(self.prb1.get_problema_id(), None, 0)
        assert (self.prb1.__eq__(self.prb2))

    def test_valid_studenti(self):
        valid = ValidatoriStudent()
        self.student1.set_nume("")
        self.student1.set_grup(-214)
        with self.assertRaises(ValidError):
            valid.valideaza(self.student1)

    def test_valid_prb(self):
        self.prb1.set_nume("")
        self.prb1.set_grup("")
        valid = ValidatoriStudent()
        with self.assertRaises(ValidError):
            valid.valideaza1(self.prb1)

    def test_repo(self):
        repo = FileRepoStudenti(
            r"C:/Users/David/Desktop/GestionareLaboratoare/studenti_teste.txt")
        self.assertEqual(repo.size(), 0)
        repo.adauga(self.student1)
        self.assertEqual(repo.size(), 1)
        key_student = Student(self.student1.get_student_id(), None, 0)
        gasit = repo.cauta(key_student.get_student_id())
        self.assertEqual(gasit, None)
        with self.assertRaises(RepoError):
            repo.cauta(2)
        repo.modifica(self.student1)
        al = repo.get_all()
        self.assertEqual(len(al), 1)
        self.assertEqual(al[0].get_nume(), self.student1.get_nume())
        repo.sterge(key_student.get_student_id())
        self.assertEqual(repo.size(), 0)
        with self.assertRaises(RepoError):
            repo.sterge(5)

    def test_service_studenti(self):
        repo = FileRepoStudenti(
            r"C:/Users/David/Desktop/GestionareLaboratoare/studenti_teste.txt")
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        srv.adauga_student(self.student1.get_student_id(),
                           self.student1.get_nume(), self.student1.get_grup())
        self.assertEqual(srv.numar_studenti(), 1)
        with self.assertRaises(ValidError):
            srv.adauga_student(-1, "david", -214)
        with self.assertRaises(RepoError):
            srv.adauga_student(1, "david", 12)

    def test_service_prb(self):
        repo = FileRepoProbleme(
            r"C:/Users/David/Desktop/GestionareLaboratoare/studenti_teste.txt")
        valid = ValidatoriStudent()
        srv = ServiceProbleme(repo, valid)
        srv.adauga_problema(self.prb1.get_problema_id(),
                            self.prb1.get_descriere(), self.prb1.get_deadline())
        self.assertEqual(srv.numar_probleme(), 1)

        with self.assertRaises(ValidError):
            srv.adauga_problema(-1, "david", -214)
        with self.assertRaises(RepoError):
            srv.adauga_problema(1, "david", 12)

    def test_asignare_problema(self):
        repo = FileRepoStudenti(
            r"C:/Users/David/Desktop/GestionareLaboratoare/studenti_teste.txt")
        repo1 = FileRepoProbleme(
            r"C:/Users/David/Desktop/GestionareLaboratoare/probleme_teste.txt")
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryStatistici(repo2)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        stats = ServiceStats(repo3)
        srv.adauga_student(self.student1.get_student_id(),
                           self.student1.get_nume(), self.student1.get_grup())
        rsv.adauga_problema(self.prb1.get_problema_id(),
                            self.prb1.get_descriere(), self.prb1.get_deadline())
        rsv.adauga_problema(self.prb2.get_problema_id(),
                            self.prb2.get_descriere(), self.prb2.get_deadline())
        asg.asignare_problema(1, 1, 1)
        self.assertEqual(asg.numar_asignari(), 1)
        asg.asignare_problema(1, 2, 4)
        self.assertEqual(asg.numar_asignari(), 2)
        with self.assertRaises(RepoError):
            asg.asignare_problema(1, 3, -1)
        with self.assertRaises(RepoError):
            asg.asignare_problema(5, 1, 4)

    def test_ordonare_nume(self):
        repo = FileRepoStudenti(
            r"C:/Users/David/Desktop/GestionareLaboratoare/studenti_teste.txt")
        repo1 = FileRepoProbleme(
            r"C:/Users/David/Desktop/GestionareLaboratoare/probleme_teste.txt")
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryStatistici(repo2)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        stats = ServiceStats(repo3)
        srv.adauga_student(self.student1.get_student_id(),
                           self.student1.get_nume(), self.student1.get_grup())
        srv.adauga_student(self.student2.get_student_id(),
                           self.student2.get_nume(), self.student2.get_grup())
        rsv.adauga_problema(self.prb1.get_problema_id(),
                            self.prb1.get_descriere(), self.prb1.get_deadline())
        asg.asignare_problema(1, 1, 4)
        for x in stats.get_ordonari_nume():
            self.assertEqual(x, [['David', 1, 4]], [['David', 1, 4]])
        asg.asignare_problema(2, 1, 2)
        for x in stats.get_ordonari_nume():
            self.assertEqual(x, [['Andrei', 1, 2], [
                'David', 1, 4]], [['Andrei', 1, 2], ['David', 1, 4]])

    def test_ordonare_nota(self):
        repo = FileRepoStudenti(
            r"C:/Users/David/Desktop/GestionareLaboratoare/studenti_teste.txt")
        repo1 = FileRepoProbleme(
            r"C:/Users/David/Desktop/GestionareLaboratoare/probleme_teste.txt")
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryStatistici(repo2)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        stats = ServiceStats(repo3)
        srv.adauga_student(self.student1.get_student_id(),
                           self.student1.get_nume(), self.student1.get_grup())
        srv.adauga_student(self.student2.get_student_id(),
                           self.student2.get_nume(), self.student2.get_grup())
        rsv.adauga_problema(self.prb1.get_problema_id(),
                            self.prb1.get_descriere(), self.prb1.get_deadline())
        asg.asignare_problema(1, 1, 4)
        for x in stats.get_ordonari_studenti():
            self.assertEqual(x, [['David', 1, 4]], [['David', 1, 4]])
        asg.asignare_problema(2, 1, 6)
        for x in stats.get_ordonari_studenti():
            self.assertEqual(x, [[
                'David', 1, 4], ['Andrei', 1, 6]], [[
                    'David', 1, 4], ['Andrei', 1, 6]])

    def test_medie_studenti(self):
        repo = FileRepoStudenti(
            r"C:/Users/David/Desktop/GestionareLaboratoare/studenti_teste.txt")
        repo1 = FileRepoProbleme(
            r"C:/Users/David/Desktop/GestionareLaboratoare/probleme_teste.txt")
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryStatistici(repo2)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        stats = ServiceStats(repo3)
        srv.adauga_student(self.student1.get_student_id(),
                           self.student1.get_nume(), self.student1.get_grup())
        srv.adauga_student(self.student2.get_student_id(),
                           self.student2.get_nume(), self.student2.get_grup())
        rsv.adauga_problema(self.prb1.get_problema_id(),
                            self.prb1.get_descriere(), self.prb1.get_deadline())
        asg.asignare_problema(1, 1, 4)
        for medie in stats.get_medie_studenti():
            self.assertEqual(medie, ["David", 4.0])
        asg.asignare_problema(2, 1, 5)
        for medie in stats.get_medie_studenti():
            self.assertEqual(medie, ["David", 4.0])
        rsv.adauga_problema(self.prb2.get_problema_id(),
                            self.prb2.get_descriere(), self.prb2.get_deadline())
        asg.asignare_problema(2, 2, 3)
        for medie in stats.get_medie_studenti():
            self.assertEqual(medie,  [["David", 4.0], ["Andrei", 4.0]])

    def ruleaza_teste(self):
        self.test_domeniu_studenti()
        self.test_domeniu_prb()
        self.test_valid_studenti()
        self.test_valid_prb()
        self.test_repo()
        self.test_service_studenti()
        self.test_service_prb()
        self.test_asignare_problema()
        self.test_asignare_nota()
        self.test_ordonare_nume()
        self.test_ordonare_nota()
        self.test_medie_studenti()


if __name__ == '__main__':
    unittest.main()
