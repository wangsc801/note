import numpy as np
from numpy.linalg import *
import sys


class determinant:
    def __init__(self):
        self.dtmnt = []
        self.sideLen = 0

    def is_determinant_available(self):
        if self.dtmnt != None:
            self.sideLen = int(len(self.dtmnt)**0.5)
            if self.sideLen > 0 and self.sideLen**2 == len(self.dtmnt):
                return True
            else:
                return False

    def input_derminant(self):
        print("\n>> input a determinant\nexample: for a determinant\
            \n1 2 3\n4 5 6\n7 8 9\ninput 1 2 3 4 5 6 7 8 9")
        self.dtmnt = list(map(int, input().strip().split(" ")))
        if self.is_determinant_available():
            self.dtmnt = np.reshape(self.dtmnt, (self.sideLen, self.sideLen))
            return
        else:
            print("wrong determinant!")
            self.input_derminant()

    def repl(self):
        option_tips = """
        ---
        input option:
        1.determinant
        2.inverse
        3.eig
        4.transpose
        r:reinput
        q:quit
        ---
        >>"""
        while 1:
            self.input_derminant()
            print(self.dtmnt)
            while 1:
                option = input(option_tips)
                if option == "1":
                    print(det(self.dtmnt))
                elif option == "2":
                    print(inv(self.dtmnt))
                elif option == "3":
                    print(eig(self.dtmnt))
                elif option == "4":
                    print(self.dtmnt.transpose())
                elif option == "r" or option == "R":
                    break
                elif option == "q" or option == "Q":
                    sys.exit()
                else:
                    print("...mismatched option!")


if __name__ == '__main__':
    d = determinant()
    d.repl()
