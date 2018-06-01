#==============================================================================#
# lp_gen.py
# Generates the lp file for CPLEX.
# Assignment 2 - Flow planning
# Shan Koo (ysk28) and Kate Chamberlin (kch114)
# Due date 25th May 2018
#==============================================================================#

import sys
PATHS = 3 #the number of paths the load must be balanced between
STD = "S{}T{}D{}" #Standard format for most nodes - Source #, Transit #, Dest #.

#==============================================================================#
# Format writers
#==============================================================================#

def writeAll(file, source, transit, dest):
    """ Writes entire LP file"""
    writeHeader(file)
    writeConstraints(file, source, transit, dest)
    writeTrailer(file, source, transit, dest)
    return

def writeHeader(file):
    """ Writes the header out to the given file"""
    file.write("Minimize\n")
    file.write("    r\n")
    file.write("Subject to\n")
    return

#==============================================================================#
# Constraint writers
#==============================================================================#

def writeConstraints(file, source, transit, dest):
    """ Writes all constraints to the given file"""
    writeMinimiseObjectiveFormula(file, source, transit)
    writeLoadBalancingConstraints(file, source, transit, dest)
    writeDemandVolConstraints(file, source, transit, dest)
    writeDemandFlowConstraints(file, source, transit, dest)
    writeSourceCapacityConstraints(file, source, transit, dest)
    writeDestCapacityConstraints(file, source, transit, dest)
    writeBinaryConstraints(file, source, transit, dest)
    
def writeMinimiseObjectiveFormula(file, source, transit):
    """ Writes the minimisation of r objective constraints to the given file.
        Sum of all capacities through a transit node - r <= 0 
        This auxilliary variable r is what we are minimising. """
    line = ""
    for k in range(1, transit + 1):
        line += "    r{}: ".format(k)
        for i in range(1, source + 1):
            line += ("yS{}T{}".format(i, k))     
            if (i == source): line += (" - r <= 0\n")
            else: line += (" + ")
    file.write(line)
    return    

def writeLoadBalancingConstraints(file, source, transit, dest):
    """ Writes the load balancing constraints to the given file.
        Sum of all path flows through a transit node - load = 0. """
    line = ""
    for k in range(1, transit + 1):
        line += "    load{}: ".format(k)
        for i in range(1, source + 1):
            for j in range(1, dest + 1):
                line += ("x" + STD.format(i, k, j))
                if (i == source and j == dest): line += (" - lT{} = 0\n".format(k))
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

def writeTrailer(file, source, transit, dest):
    """ Writes all other LP information to file"""
    file.write("Bounds\n")
    writeFlowBounds(file, source, transit, dest)
    writeSourceBounds(file, source, transit)
    writeDestBounds(file, transit, dest)
    file.write("    r >= 0\n")
    file.write("Binaries\n")
    writeBinaries(file, source, transit, dest)
    file.write("End")
    return

def writeFlowBounds(file, source, transit, dest):
    """ Writes the flow bounds to given file"""
    line = ""
    for i in range(1, source + 1):
        for j in range(1, dest + 1):
            for k in range(1, transit + 1):
                line += ("    x" + STD.format(i, k, j) + " >= 0\n")
    file.write(line)
    return

def writeSourceBounds(file, source, transit):
    """ Writes the source -> transit capacity bounds to given file"""
    line = ""
    for i in range(1, source + 1):
        for k in range(1, transit + 1):
            line += ("    yS{}T{} >= 0\n".format(i, k)) 
    file.write(line)
    return

def writeDestBounds(file, transit, dest):
    """ Writes the transit -> dest capacity bounds to given file"""
    line = ""
    for j in range(1, dest + 1):
        for k in range(1, transit + 1):
            line += ("    yT{}D{} >= 0\n".format(k, j))
    file.write(line)
    return

def writeBinaries(file, source, transit, dest):
    """ Writes all the binary variables to the given file"""
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
    
    ### Appendix generation
    #f = open("appendix.lp", 'w')
    #source, transit, dest = 3, 2, 4
    #writeAll(f, source, transit, dest)
    #f.close()
    
    #generic lp generation
    for y in range(3, 8):
        f = open("out%s.lp" %y, 'w')
        source, transit, dest = 7, y, 7
        writeAll(f, source, transit, dest)
        f.close()