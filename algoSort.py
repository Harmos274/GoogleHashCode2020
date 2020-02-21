#!/bin/env python3

import sys

dayToScan = 0

booksArray = []
LibrariesArray = []

class Book:
    def __init__(self, score):
        self.score = score
        self.libs = []
        self.id = len(booksArray)

    def addLib(self, lib):
        self.libs.append(lib)

    def dumpInfo(self):
        print("Book: " + str(self.id))
        print("BookScore: " + str(self.score) + ", nbOccurence: " + str(len(self.libs)))

class Library:
    def __init__(self, signUpTime, nbrScansDay):
        self.id = len(LibrariesArray)
        self.signUpTime = int(signUpTime)
        self.nbrScansDay = nbrScansDay
        self.books = []
        self.rendement = 0
    def addBook(self, book):
        booksArray[int(book)].addLib(self.id)
        self.books.append(booksArray[int(book)])
    def dumpInfo(self):
        print("id : " + str(self.id))
        for book in self.books:
            print(book)
        print("--------")


def getDayToScan(line):
    global dayToScan
    dayToScan = int(line.split()[2])


def getBooksScore(line):
    books = line.split()
    for book in books:
        booksArray.append(Book(int(book)))


def getLibraries(lines):
    i = 0
    while(i != len(lines)):
        lineF = lines[i].split()
        if (len(lineF) < 1):
            break
        if (int(lineF[1]) < dayToScan):
            library = Library(lineF[1], lineF[2])
            i = i + 1
            lineB = lines[i].split()
            for book in lineB:
                library.addBook(book)
            LibrariesArray.append(library)
            i = i + 1
        else:
            i = i + 2


def parser():
    if (len(sys.argv) == 1):
        print("Please give the pathfile")
        exit(1)
    pathName = sys.argv[1]
    file = open(pathName, "r")
    getDayToScan(file.readline())
    getBooksScore(file.readline())
    getLibraries(file.readlines())


def LibScoreMoy(books : list):
    maxValue = 0
    minValue = 0

    for book in books:
        if len(book.libs) == 1:
            minValue += book.score
        maxValue += book.score
    return ((maxValue + minValue) / 2)


def sumarizeSortedSignUp(sortedLib: list) -> int:
    total = 0
    for lib in sortedLib:
        total += lib.signUpTime
    return total


def BiblioSort(arrayLib : list) -> list:
    maxDay = int(dayToScan)
    sortedArray = []

    while maxDay > 0 and len(arrayLib) > 0:
        for lib in arrayLib:
            sorted(lib.books, key=lambda book : book.score, reverse=True)
            lib.rendement = float(lib.nbrScansDay) * (LibScoreMoy(lib.books)  / len(lib.books)) * float((int(dayToScan) - int(lib.signUpTime)))
        sorted(arrayLib, key=lambda lib : lib.rendement, reverse=True)
        maxDay -= int(arrayLib[0].signUpTime)
        arrayLib[0].signUpTime += sumarizeSortedSignUp(sortedArray)
        sortedArray.append(arrayLib.pop(0))
    return sortedArray


def main():
    parser()
    sortedLib = BiblioSort(LibrariesArray)
    printed = []

    sortedLib = sorted(sortedLib, key=lambda lib : lib.signUpTime, reverse=True)
    file = open("output.txt", "w");
    printed.append(str(len(sortedLib)) + "\n")
    for lib in sortedLib:
        printed.append(str(lib.id) + " " + str(len(lib.books)) + "\n")
        string = ""
        for book in lib.books:
            string += str(book.id) + " "
        string += "\n"
        printed.append(string)
    file.writelines(printed)

if __name__ == "__main__":
    main()
