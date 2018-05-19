#==============================================================================#
# lp_gen.py
# Generates the lp file for CPLEX.
# Assignment 2 - Flow planning
# Shan Koo (ysk28) and Kate Chamberlin (kch114)
# Due date 25th May 2018
#==============================================================================#

import sys
PATHS = 3 #the number of paths the load must be balanced between
STD = "S{}T{}D{}"

#==============================================================================#
# Printers to output file
#==============================================================================#

def writeHeader(file):
    """ Writes the header out to the given file"""
    file.write("Minimize\n")
    file.write("    r\n")
    file.write("Subject to\n")
    return

def writeDemandVolConstraints(file, source, transit, dest):
    """ Writes the demand flow constraints out to the given file"""
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            line = line + ("    hS{}D{}: ".format(i, j))
            for k in range(1, transit + 1):
                line = line + ("x" + STD.format(i, j, k))
                if (k != transit): line = line + (" + ")
                else: line = line + (" = {}\n".format(i + j))
    file.write(line)
    return

def writeDemandFlowConstraints(file, source, transit, dest):
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            for k in range(1, transit + 1):
                line = line + ("    df{}: {} x{} - {} u{} = 0\n"
                                .format(STD.format(i, j, k),
                                        PATHS,
                                        STD.format(i, j, k),
                                        i + j,
                                        STD.format(i, j, k)))
    file.write(line)
    return
                
    

#==============================================================================#
# Test
#==============================================================================#

if (__name__ == "__main__"):
    
    f = open("out.lp", 'w')
    source, transit, dest = 3, 3, 3
    #source, transit, dest = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    writeHeader(f)
    writeDemandVolConstraints(f, source, transit, dest)
    writeDemandFlowConstraints(f, source, transit, dest)
    f.close()