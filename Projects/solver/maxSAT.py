import sys
import os
import subprocess
class MaxSAT:
    def __init__(self):
        self.soft = []
        self.hard = []
        self.infinit = -1
        self.nvar = 0
        self.aux = 500

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

    def alo(self, lits):
        self.hard.append(lits)
 
    def amo(self, lits):
        for i in range(len(lits) - 1):
            for j in range(i+1, len(lits)):
                self.hard.append([-lits[i], -lits[j]])
    def eo(self, lits):
        self.alo(lits)
        self.amo(lits)
        #print "Soft: ", self.soft
        #print "Hard: ", self.hard


    
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
        

    def getLits(self,fname):
        """
        Metodo que lee el archivo generado por el picosat, para obtener las variables indicador 
        leemos el archivo al revés y paramos cuando encontramos más de una variables por
        linea.
        """
        lines = []
        lits = []
        f = open(fname, "r")
        for line in f:
            l = line.split()
            lines.append(line)
        for line in reversed(lines):
            l = line.split()
            if len(l) > 2:
                break
            else:
                lits.append(l[0])
        f.close()
        return lits[::-1]

    def relaxe(self,lits):
        #Relaxing new variables in Soft
        rel = []
        for i in range(len(lits)):
            pos = (- int(lits[i]) - self.aux )
            first = self.soft[pos]
            self.nvar = self.nvar + 1
            rel.append(self.nvar)
            first[0].append(self.nvar)
            self.soft[pos] = first
        return rel


if __name__ == "__main__":

    coreFile = "core"
    satFile = "file"
    cnf = ".cnf"
    #command = './maxsatz2009 '+ sys.argv[1]    
    #output = os.popen(command).readlines()
    #for l in output:
    #    print l
    sat = MaxSAT()
    sat.read(sys.argv[1])

    #sat.solver(coreFile,satFile,cnf)

    s=0
    while True:
        sat.tosat('test/'+satFile+str(s)+cnf )
        command = 'picosat-951/picosat -c test/'+coreFile+str(s)+cnf+ ' test/'+satFile+str(s)+cnf   
        output = os.popen(command).readlines()
        for line in output:
            l = line.split()
            print l
            if l[0] == "o":
                print l
            if l[0] == "s":
                if l[1] == "SATISFIABLE":
                    sys.exit("END")
        lits = sat.getLits('test/'+coreFile+str(s)+cnf)
        sat.eo(sat.relaxe(lits))
        s = s +1
