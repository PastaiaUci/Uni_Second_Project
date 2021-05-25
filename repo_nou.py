from exceptii import *
from validatori import *
from random import *
from entitati import *
from operator import itemgetter
import re


class RepoStudentiNou(object):

    def __init__(self, filename):
        self.filename = filename

    def write_in_directory(self, student):
        my_file = open(self.filename, 'a')
        my_file.write(str(student.get_student_id())+"," +
                      student.get_nume() + "," + str(student.get_grup()) + "\n")
        my_file.close()

    def write_in_output(self):
        open('studenti_output.txt', 'w').close()
        filepath = self.filename
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                with open('studenti_output.txt', 'a') as out:
                    out.write(line)
                line = fp.readline()

    def write_in_input(self):
        open(self.filename, 'w').close()
        with open('studenti_output.txt') as fp:
            line = fp.readline()
            while line:
                with open(self.filename, 'a') as out:
                    out.write(line)
                line = fp.readline()

    def adauga(self, student):
        self.write_in_directory(student)
        self.write_in_output()

    def get_all(self):
        self.write_in_output()
        elems = []
        my_file = open('studenti_output.txt', 'r')
        line = my_file.readline()
        while line:
            elems.append(line)
            line = my_file.readline()
        return elems

    def size(self):
        self.write_in_output()
        filepath = 'studenti_output.txt'
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                line = fp.readline()
                cnt += 1
        return cnt

    def modifica(self, student):
        open('studenti_output.txt', 'w').close()
        filepath = self.filename
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                parts = line.split(',')
                if student.get_student_id() == int(parts[0]):
                    with open('studenti_output.txt', 'a') as out:
                        out.write(str(student.get_student_id()) + "," +
                                  student.get_nume() + ","+str(student.get_grup())+"\n")
                else:
                    with open('studenti_output.txt', 'a') as out:
                        out.write(line)
                line = fp.readline()

        self.write_in_input()

    def sterge(self, student_id):
        open('studenti_output.txt', 'w').close()
        filepath = self.filename
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                parts = line.split(',')
                if student_id == int(parts[0]):
                    pass
                else:
                    with open('studenti_output.txt', 'a') as out:
                        out.write(line)
                line = fp.readline()
        self.write_in_input()

    def cauta(self, student_id):
        filepath = self.filename
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                parts = line.split(',')
                if student_id == int(parts[0]):
                    print(line)
                line = fp.readline()
