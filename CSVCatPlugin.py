import PyPluMA

class CSVCatPlugin:
    def input(self, inputfile):
        infile = open(inputfile, 'r')
        self.csvfiles = []
        for line in infile:
            self.csvfiles.append(PyPluMA.prefix()+"/"+line.strip())

    def run(self):
        pass

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        for i in range(len(self.csvfiles)):
            infile = open(self.csvfiles[i], 'r')
            firstline = infile.readline()
            if (i == 0):
                outfile.write(firstline)
            for line in infile:
                outfile.write(line)

