import sys
import os
import subprocess
class MaxSAT:
    def __init__(self):
        self.soft = []
        self.hard = []
        self.infinit = -1
        self.nvar = 0

    def read(self, fname):
        f = open(fname, "r")
        for line in f:
            l = line.split()
            if l[0] != 'c':
                if l[0] == 'p':
                    infinit = l[4]
                    self.nvar = int(l[2])
                elif l[0] == infinit:
                    self.hard.append([int(c) for c in l[1:-1]])
                else:
                    self.soft.append(([int(c) for c in l[1:-1]], int(l[0])))
        f.close()
        print "Soft: ", self.soft
        print "Hard: ", self.hard

    def alo(self, lits):
        self.hard.append(lits)
 
    def amo(self, lits):
        for i in range(len(lits) - 1):
            for j in range(i+1, len(lits)):
                self.hard.append([-lits[i], -lits[j]])
    def eo(self, lits):
        self.alo(lits)
        self.amo(lits)
        print "Soft: ", self.soft
        print "Hard: ", self.hard
    
    def tosat(self, fname):
        aux = 500
        f = open(fname,"w")
        # header
        print >>f, "p cnf", aux+self.nvar-1, (len(self.soft)*2)+len(self.hard)
        
        # soft
        for c, w in self.soft:
            for lit in c:
                print >>f, lit,
            print >>f,aux, "0"
            aux += 1    
        # hard
        for c in self.hard:
            for lit in c:
                print >>f, lit,
            print >>f, "0"
        aux = 500
        for c in self.soft:
            print >>f, -aux , "0" 
            aux += 1 
        f.close()
        command = '../picosat-951/picosat -c ../maxsat/core.cnf file.cnf'     
        output = os.popen(command).readlines()
        for l in output:
            print l

if __name__ == "__main__":
    sat = MaxSAT()
    sat.read(sys.argv[1])
    sat.tosat("file.cnf")
