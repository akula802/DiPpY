#!/usr/bin/env python


#-----------------------------------------------------------------------------#
#                                                                             #
#   DiPpY is a simple, 2-D formation dip calculator.                          #
#   Copyright (C) 2015 Brian Hartley (www.bhartley.com)                       #
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU General Public License as published by      # 
#   the Free Software Foundation, either version 3 of the License, or         # 
#   (at your option) any later version.                                       #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU General Public License for more details.                              #
#                                                                             #
#   You should have received a copy of the GNU General Public License         #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
#-----------------------------------------------------------------------------#


import re
import math
#from Tkinter import *
from tkinter import * #(use for Python 3, lowercase T)
root = Tk()


# BLOCK_1 ********************************************************************


# Gives the application a title in the window
root.title("DiPpY v0.1")


# Makes the window a fixed size
root.resizable(width=FALSE, height=FALSE)


# Defines an image for the title in the application window
titleGIF = PhotoImage(file="title4.gif")
appTitle = Label(root, image=titleGIF)
appTitle.titleGIF = titleGIF
appTitle.grid(row=1, column=1, columnspan=2, pady=5, padx=5)


# BLOCK_2 ********************************************************************


# Creates a "Results" variable that will hold the calculated result
# Sets the dipResult, and thus dipResultField to a default value
dipResult = StringVar()
dipResult.set("Formation dip = ...")


# Creates a text box to display the calculated result and sets a default display value
dipResultField = Entry(root, textvariable=dipResult, bd=5, font=30, relief=GROOVE)
dipResultField.grid(row=2, column=1, columnspan=2, sticky=E+W, pady=10, padx=10)


# Creates the labels for the text input boxes
lab_vs1 = Label(root, text="VS of point 1:").grid(row=3, column=1, padx=5, sticky=W)
lab_tvd1 = Label(root, text="TVD of point 1:").grid(row=4, column=1, padx=5, sticky=W)
lab_vs2 = Label(root, text="VS of point 2:").grid(row=5, column=1, padx=5, sticky=W)
lab_tvd2 = Label(root, text="TVD of point 2:").grid(row=6, column=1, padx=5, sticky=W)


# Creates the text input boxes and places them in the grid
vs1 = Entry(root)
tvd1 = Entry(root)
vs2 = Entry(root)
tvd2 = Entry(root)


vs1.grid(row=3, column=2, pady=5, padx=10)
tvd1.grid(row=4, column=2, pady=5, padx=10)
vs2.grid(row=5, column=2, pady=5, padx=10)
tvd2.grid(row=6, column=2, pady=5, padx=10)


# BLOCK_3 ********************************************************************


# Check all dipCalc inputs for non-numeric characters
def checkDCalpha():
    badInput_vs1 = re.search('[a-zA-Z]', vs1.get())
    badInput_tvd1 = re.search('[a-zA-Z]', tvd1.get())
    badInput_vs2 = re.search('[a-zA-Z]', vs2.get())
    badInput_tvd2 = re.search('[a-zA-Z]', tvd2.get())
    if badInput_vs1 == None and badInput_tvd1 == None and badInput_vs2 == None and badInput_tvd2 == None:
        return False
    else:
        return True


# Check for empty or missing dipCalc inputs
def checkDCempty():
    if vs1.get() == '' or tvd1.get() == '' or vs2.get() == '' or tvd2.get() == '':
        dipResult.set("All fields required")
        return True
    else:
        return False


# Validate dipCalc inputs with checkDCalpha() and checkDCempty()
def validateDC():
    if checkDCempty() == True:
        dipResult.set("All fields required")
        return False
    elif checkDCalpha() == True:
        dipResult.set("Input is non-numeric")
        return False
    else:
        return True


# Creates the dip calculation function
def dipCalc():
    if validateDC() == True:
        deltaVS = float(vs2.get())-float(vs1.get())
        deltaTVD = float(tvd2.get())-float(tvd1.get())
    else:
        return

    if deltaTVD < 0.00:
        dip = str(180-round(math.degrees((math.atan(abs(deltaVS / deltaTVD)))), 2))
        dipResult.set("Formation dip = " + dip + " degrees")
        return
    elif deltaTVD == 0.00:
        dipResult.set("Formation dip is 90.00 degrees")
        return
    elif deltaTVD > 0.00:
        dip = str(round(math.degrees((math.atan(abs(deltaVS / deltaTVD)))), 2))
        dipResult.set("Formation dip = " + dip + " degrees")
        return
    else:
        dipResult.set("You somehow broke DiPpY")
        return


def dipClear():
    dipResult.set("Formation dip = ...")
    vs1.delete(0, END)
    tvd1.delete(0, END)
    vs2.delete(0, END)
    tvd2.delete(0, END)
    return


# Creates the Calculate Dip button and places it in the grid
calcDip = Button(root, command=dipCalc, bd=4, text="Calculate Fm Dip").grid(row=7, column=2, pady=10)


# Creates a button to clear the dip calculator
clearDip = Button(root, command=dipClear, bd=4, text="Clear Dip").grid(row=7, column=1, pady=10)


# BLOCK_4 ********************************************************************


# Creates a "0' VS TVD" variable that will hold the calculated result
# Sets the zeroVS, and thus dipResultField to a default value
zeroVS = StringVar()
zeroVS.set("TVD @ 0\' VS = ...")


# Creates a text box to display the calculated result and sets a default display value
zeroVSField = Entry(root, textvariable=zeroVS, bd=5, font=30, relief=GROOVE)
zeroVSField.grid(row=8, column=1, columnspan=2, sticky=E+W, pady=10, padx=10)


# Creates the labels for the text input boxes
lab_curTVD = Label(root, text="Current TVD:").grid(row=9, column=1, padx=5, sticky=W)
lab_curVS = Label(root, text="Current VS:").grid(row=10, column=1, padx=5, sticky=W)
lab_vurDip = Label(root, text="Current dip:").grid(row=11, column=1, padx=5, sticky=W)


# Creates the text input boxes and places them in the grid
tvdCurrent = Entry(root)
vsCurrent = Entry(root)
dipCurrent = Entry(root)

tvdCurrent.grid(row=9, column=2, pady=5, padx=10)
vsCurrent.grid(row=10, column=2, pady=5, padx=10)
dipCurrent.grid(row=11, column=2, pady=5, padx=10)


# BLOCK_5 ********************************************************************


# Check all zeroVStvd inputs for non-numeric characters
def checkZVSalpha():
    badInput_tvd = re.search('[a-zA-Z]', tvdCurrent.get())
    badInput_vs = re.search('[a-zA-Z]', vsCurrent.get())
    badInput_dip = re.search('[a-zA-Z]', dipCurrent.get())
    if badInput_tvd == None and badInput_vs == None and badInput_dip == None:
        return False
    else:
        return True


# Check for empty or missing dipCalc inputs
def checkZVSempty():
    if tvdCurrent.get() == '' or vsCurrent.get() == '' or dipCurrent.get() == '':
        zeroVS.set("All fields required")
        return True
    else:
        return False


# Validate dipCalc inputs with checkDCalpha() and checkDCempty()
def validateZVS():
    if checkZVSempty() == True:
        zeroVS.set("All fields required")
        return False
    elif checkZVSalpha() == True:
        zeroVS.set("Input is non-numeric")
        return False
    else:
        return True


# Creates the Calculate 0' VS TVD function
def zeroVStvd():
    if validateZVS() == True:
        absDip = 90-(float(dipCurrent.get()))
        zVStvd = None
    else:
        return

    if absDip == 90:
        zeroVS.set("TVD = " + round(tvdCurrent, 0) + " @ 0\' VS")
    elif absDip > 90:
        zVStvd = round((int(tvdCurrent.get()) + (math.tan(math.radians(absDip)) * int(vsCurrent.get()))), 2)
        zeroVS.set("TVD = " + str(round(zVStvd, 1)) + " @ 0\' VS")
    elif absDip < 90:
        zVStvd = round((int(tvdCurrent.get()) - (math.tan(math.radians(absDip)) * int(vsCurrent.get()))), 2)
        zeroVS.set("TVD = " + str(round(zVStvd, 1)) + " @ 0\' VS")
    else:
        zeroVS.set("You somehow broke DiPpY")


# Function to clear Zero VS calculator
def zeroVSclear():
    zeroVS.set("TVD @ 0\' VS = ...")
    tvdCurrent.delete(0, END)
    vsCurrent.delete(0, END)
    dipCurrent.delete(0, END)
    return

	
# Creates the Calculate 0' VS TVD button and places it in the grid
calcZVS = Button(root, command=zeroVStvd, bd=4, text="Calculate TVD @ 0\' VS").grid(row=12, column=2, pady=10)


# Creates a button to clear the ZVS calculator
clearZVS = Button(root, command=zeroVSclear, bd=4, text="Clear ZVS").grid(row=12, column=1, pady=10)


# BLOCK_6 ********************************************************************


# Begins main application functionality
root.mainloop()