import argparse
import os
import functions
import artist
global artistDict

artistDict = functions.loadCSV()
print(artistDict[0])

Tobject = functions.createObject(artistDict[0]) 
print(Tobject.movement)
#functions.addArtist()
