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
# Format writers
#==============================================================================#
def writeAll(file, source, transit, dest):
    writeHeader(file)
    writeConstraints(file, source, transit, dest)
    writeOthers(file, source, transit, dest)
    writeEnd(file)
    return

def writeHeader(file):
    """ Writes the header out to the given file"""
    file.write("Minimize\n")
    file.write("    r\n")
    file.write("Subject to\n")
    return

def writeEnd(file):
    """ Finishes off the given file"""
    file.write("End")
    return

#==============================================================================#
# Constraint writers
#==============================================================================#

def writeConstraints(file, source, transit, dest):
    writeLoadBalancingConstraints(file, source, transit, dest)
    writeDemandVolConstraints(file, source, transit, dest)
    writeDemandFlowConstraints(file, source, transit, dest)
    writeSourceCapacityConstraints(file, source, transit, dest)
    writeDestCapacityConstraints(file, source, transit, dest)
    writeBinaryConstraints(file, source, transit, dest)

def writeLoadBalancingConstraints(file, source, transit, dest):
    """ Writes the load balancing constraints to the given file.
        Sum of all path flows through a transit node <= r 
        This auxilliary variable r is what we are minimising. """
    line = ""
    for k in range(1, transit + 1):
        line += "    r{}: ".format(k)
        for i in range(1, source + 1):
            for j in range(1, dest + 1):
                line += ("x" + STD.format(i, k, j))
                if (i == source and j == dest): line += (" - r <= 0\n")
                else: line += (" + ")
    file.write(line)
    return

def writeDemandVolConstraints(file, source, transit, dest):
    """ Writes the demand volume constraints out to the given file
        Here the demand volume is equal to i + j. """
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            line += ("    hS{}D{}: ".format(i, j))
            for k in range(1, transit + 1):
                line += ("x" + STD.format(i, k, j))
                if (k != transit): line += (" + ")
                else: line += (" = {}\n".format(i + j))
    file.write(line)
    return

def writeDemandFlowConstraints(file, source, transit, dest):
    """ Writes the demand flow constraints out to the given file.
        This is for load balancing equation x=(u*h)/n"""
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            for k in range(1, transit + 1):
                line += ("    df{}: {} x{} - {} u{} = 0\n"
                                .format(STD.format(i, k, j),
                                        PATHS,
                                        STD.format(i, k, j),
                                        i + j,
                                        STD.format(i, k, j)))
    file.write(line)
    return

def writeSourceCapacityConstraints(file, source, transit, dest):
    """ Writes the capacity constraints for the source to transit link. 
        Writes to the given file"""
    line = ""
    for i in range(1, source + 1):
        for k in range(1, transit + 1):
            line += "    cS{}T{}: ".format(i,k)
            for j in range(1, dest + 1):
                line += ("x" + STD.format(i, k, j))
                if (j != dest): line += (" + ")
                else: line += (" - yS{}T{} = 0\n".format(i, k))
    file.write(line)
    return

def writeDestCapacityConstraints(file, source, transit, dest):
    """ Writes the capacity constraints for the transit to destination link. 
        Writes to the given file"""    
    line = ""
    for j in range(1, dest + 1):
        for k in range(1, transit + 1):
            line += "    dT{}D{}: ".format(k, j)
            for i in range(1, source + 1):
                line += ("x" + STD.format(i, k, j))
                if (i != source): line += (" + ")
                else: line += (" - yT{}D{} = 0\n".format(k, j))
    file.write(line)
    return

def writeBinaryConstraints(file, source, transit, dest):
    """ Writes the binary constraints to the given file.
        Sum of binaries should equal the PATHS constant."""
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            line += "    uS{}D{}: ".format(i, j)
            for k in range(1, transit + 1):
                line += ("u" + STD.format(i, k, j))
                if (k != transit): line += (" + ")
                else: line += (" = {}\n".format(PATHS)) 
    file.write(line)
    return

#==============================================================================#
# Other writers
#==============================================================================#

def writeOthers(file, source, transit, dest):
    file.write("Bounds\n")
    writeFlowBounds(file, source, transit, dest)
    writeSourceBounds(file, source, transit, dest)
    writeDestBounds(file, source, transit, dest)
    file.write("    r >= 0\n")
    file.write("Binaries\n")
    writeBinaries(file, source, transit, dest)
    return

def writeFlowBounds(file, source, transit, dest):
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            for k in range(1, transit + 1):
                line += ("    x" + STD.format(i, k, j) + " >= 0\n")
    file.write(line)
    return

def writeSourceBounds(file, source, transit, dest):
    line = ""
    for i in range(1, dest + 1):
        for k in range(1, transit + 1):
            line += ("    cS{}T{} >= 0\n".format(i, k)) 
    file.write(line)
    return

def writeDestBounds(file, source, transit, dest):
    line = ""
    for j in range(1, dest + 1):
        for k in range(1, transit + 1):
            line += ("    dT{}D{} >= 0\n".format(k, j))
    file.write(line)
    return

def writeBinaries(file, source, transit, dest):
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            for k in range(1, transit + 1):
                line += "    u" + STD.format(i, k, j) + "\n"
    file.write(line)
    return

#==============================================================================#
# Test
#==============================================================================#

if (__name__ == "__main__"):
    
    f = open("out.lp", 'w')
    source, transit, dest = 3, 3, 3
    #source, transit, dest = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    writeAll(f, source, transit, dest)
    f.close()