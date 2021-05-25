class Teste(object):

    def __ruleaza_teste_domeniu(self):
        student_id = 11
        nume = "David"
        grup = 214
        student = Student(student_id, nume, grup)
        assert (student.get_student_id() == student_id)
        assert (student.get_nume() == nume)
        assert (student.get_grup() == grup)
        assert (str(student) == "11 David 214")
        alt_student = Student(student_id, None, 0)
        assert (student.__eq__(alt_student))

    def __ruleaza_teste_domeniu_prb(self):
        student_id = 1
        nume = "a"
        grup = "1/1/2020"
        problema = Problema(student_id, nume, grup)
        assert (problema.get_problema_id() == student_id)
        assert (problema.get_descriere() == nume)
        assert (problema.get_deadline() == grup)
        assert (str(problema) == "1 a 1/1/2020")
        alt_student = Problema(student_id, None, 0)
        assert (problema.__eq__(alt_student))

    def __ruleaza_teste_valid(self):
        student_id = -11
        nume = ""
        grup = -214
        student = Student(student_id, nume, grup)
        valid = ValidatoriStudent()
        try:
            valid.valideaza(student)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "id invalid\nnume invalid\ngrup invalid\n")

    def __ruleaza_teste_valid_prb(self):
        student_id = -11
        nume = ""
        grup = ""
        problema = Problema(student_id, nume, grup)
        valid = ValidatoriStudent()
        try:
            valid.valideaza1(problema)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "id invalid\ndescriere invalida\ndeadline invalid\n")

    def __ruleaza_teste_repo(self):
        #repo = RepositoryStudenti()
        repo = FileRepoStudenti("studenti_teste.txt")
        assert (repo.size() == 0)
        student_id = 11
        nume = "David"
        grup = 214
        student = Student(student_id, nume, grup)
        repo.adauga(student)
        assert (repo.size() == 1)
        key_student = Student(student_id, None, 0)

        gasit = repo.cauta(key_student.get_student_id())
        try:
            repo.adauga(key_student)
            assert(False)
        except RepoError as re:
            assert(True)
        key_student_nu = Student(24, None, 0)
        try:
            repo.cauta(key_student_nu)
            assert (False)
        except RepoError as re:
            assert (str(re) == "element inexistent\n")
        student_nou = Student(11, "David", 243)
        repo.modifica(student_nou)
        al = repo.get_all()
        assert (len(al) == 1)
        assert (al[0].get_nume() == nume)
        repo.sterge(key_student.get_student_id())
        assert (repo.size() == 0)
        try:
            repo.sterge(key_student)
            assert (False)
        except RepoError as re:
            assert (str(re) == "element inexistent\n")

    def __ruleaza_teste_service(self):
        repo = RepositoryStudenti()
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        srv.adauga_student(11, "david", 214)
        assert (srv.numar_studenti() == 1)
        try:
            srv.adauga_student(-11, "david", -214)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "id invalid\ngrup invalid\n")
        try:
            srv.adauga_student(11, "A", 23)
            assert (False)
        except RepoError as re:
            assert (str(re) == "element existent\n")

    def __ruleaza_teste_service_prb(self):
        repo = RepositoryProbleme()
        valid = ValidatoriStudent()
        srv = ServiceProbleme(repo, valid)
        srv.adauga_problema(11, "david", '1/1')
        assert (srv.numar_probleme() == 1)
        try:
            srv.adauga_problema(-11, "david", "1/1")
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "id invalid\n")
        try:
            srv.adauga_problema(11, "A", '1')
            assert (False)
        except RepoError as re:
            assert (str(re) == "element existent\n")

    def __ruleaza_teste_asignare_problema(self):
        repo = RepositoryStudenti()
        repo1 = RepositoryProbleme()
        repo2 = RepositoryAsignari(repo, repo1)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        srv.adauga_student(1, "David", 214)
        rsv.adauga_problema(1, "asd", "1/1/2020")
        rsv.adauga_problema(2, "as", "1/2/2020")
        asg.asignare_problema(1, 1)
        assert (asg.get_asignari() == ['David are de facut problema 1'])
        asg.asignare_problema(1, 2)
        assert(asg.get_asignari() == [
               'David are de facut problema 1', 'David are de facut problema 2'])
        try:
            asg.asignare_problema(1, 3)
            assert (False)
        except RepoError as re:
            assert (str(re) == "problema inexistent\n")
        try:
            asg.asignare_problema(5, 1)
            assert(False)
        except RepoError as re:
            assert (str(re) == "student  inexistent\n")

    def __ruleaza_teste_asignare_nota(self):
        repo = RepositoryStudenti()
        repo1 = RepositoryProbleme()
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryNote(repo2)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        nte = ServiceNote(repo3)
        srv.adauga_student(1, "David", 214)
        rsv.adauga_problema(1, "asd", "1/1/2020")
        rsv.adauga_problema(2, "as", "1/2/2020")
        asg.asignare_problema(1, 1)
        nte.asignare_nota(1, 1, 3)
        assert(nte.get_asignari_note() == [
               'David a obtinut la problema 1 nota 3'])
        asg.asignare_problema(1, 2)
        nte.asignare_nota(1, 2, 3)
        assert(nte.get_asignari_note() == [
               'David a obtinut la problema 1 nota 3', 'David a obtinut la problema 2 nota 3'])
        try:
            nte.asignare_nota(1, 1, -1)
            assert (False)
        except RepoError as re:
            assert (str(re) == "nota trbuie sa fie intre 0 si 10\n")
        try:
            nte.asignare_nota(2, 1, 3)
            assert (False)
        except RepoError as re:
            assert (str(re) == "student  inexistent\n")
        try:
            nte.asignare_nota(1, 4, 3)
            assert (False)
        except RepoError as re:
            assert (str(re) == "problema inexistent\n")

    def __ruleaza_teste_ordonare_nume(self):
        repo = RepositoryStudenti()
        repo1 = RepositoryProbleme()
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryNote(repo2)
        repo4 = RepositoryStatistici(repo3)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        nte = ServiceNote(repo3)
        stats = ServiceStats(repo4)
        srv.adauga_student(1, "David", 214)
        srv.adauga_student(2, "Andrei", 212)
        rsv.adauga_problema(1, 'ds', 'f')
        asg.asignare_problema(1, 1)
        asg.asignare_problema(2, 1)
        nte.asignare_nota(1, 1, 4)
        assert (stats.ordonare_nume() == [['David', 1, 4]], [['David', 1, 4]])
        nte.asignare_nota(2, 1, 2)
        assert (stats.ordonare_nume() == [['Andrei', 1, 2], [
                'David', 1, 4]], [['Andrei', 1, 2], ['David', 1, 4]])

    def __ruleaza_teste_ordonare_nota(self):
        repo = RepositoryStudenti()
        repo1 = RepositoryProbleme()
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryNote(repo2)
        repo4 = RepositoryStatistici(repo3)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        nte = ServiceNote(repo3)
        stats = ServiceStats(repo4)
        srv.adauga_student(1, "David", 214)
        srv.adauga_student(2, "Andrei", 212)
        rsv.adauga_problema(1, 'ds', 'f')
        asg.asignare_problema(1, 1)
        asg.asignare_problema(2, 1)
        nte.asignare_nota(1, 1, 4)
        assert (stats.ordonare_nume() == [['David', 1, 4]], [['David', 1, 4]])
        nte.asignare_nota(2, 1, 6)
        assert (stats.ordonare_nume() == [[
                'David', 1, 4], ['Andrei', 1, 6]], [[
                    'David', 1, 4], ['Andrei', 1, 6]])

    def __ruleaza_teste_medie_studenti(self):
        repo = RepositoryStudenti()
        repo1 = RepositoryProbleme()
        repo2 = RepositoryAsignari(repo, repo1)
        repo3 = RepositoryNote(repo2)
        repo4 = RepositoryStatistici(repo3)
        valid = ValidatoriStudent()
        srv = ServiceStudenti(repo, valid)
        rsv = ServiceProbleme(repo1, valid)
        asg = ServiceAsignari(repo2)
        nte = ServiceNote(repo3)
        stats = ServiceStats(repo4)
        srv.adauga_student(1, "David", 214)
        srv.adauga_student(2, "Andrei", 212)
        rsv.adauga_problema(1, 'ds', 'f')
        asg.asignare_problema(1, 1)
        asg.asignare_problema(2, 1)
        nte.asignare_nota(1, 1, 4)
        assert (stats.medie_studenti() == [["David", 4.0]])
        nte.asignare_nota(2, 1, 5)
        assert (stats.medie_studenti() == [["David", 4.0]])
        rsv.adauga_problema(2, 'dfa', 'd')
        asg.asignare_problema(2, 2)
        nte.asignare_nota(2, 2, 3)
        assert (stats.medie_studenti() == [["David", 4.0], ["Andrei", 4.0]])

    def ruleaza_teste(self):
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_valid()
        self.__ruleaza_teste_repo()
        self.__ruleaza_teste_service()
        self.__ruleaza_teste_domeniu_prb()
        self.__ruleaza_teste_service_prb()
        self.__ruleaza_teste_valid_prb()
        self.__ruleaza_teste_asignare_problema()
        self.__ruleaza_teste_asignare_nota()
        self.__ruleaza_teste_ordonare_nume()
        self.__ruleaza_teste_ordonare_nota()
