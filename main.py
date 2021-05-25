from teste import *
from servicii import *
from repos import *
from validatori import *
from consola import *
from repo_nou import *


if __name__ == '__main__':
    repo = FileRepoStudenti(
        r"C:/Users/David/Desktop/GestionareLaboratoare/studenti.txt")
    repo1 = FileRepoProbleme(
        r"C:/Users/David/Desktop/GestionareLaboratoare/probleme.txt")
    repo2 = FileRepoAsignari(
        r"C:/Users/David/Desktop/GestionareLaboratoare/asignari.txt", repo, repo1)
    repo3 = RepositoryStatistici(repo2)
    valid = ValidatoriStudent()
    srv = ServiceStudenti(repo, valid)
    rsv = ServiceProbleme(repo1, valid)
    asg = ServiceAsignari(repo2)
    stats = ServiceStats(repo3)
    cons = UI(srv, rsv, asg, stats)
    cons.run()
