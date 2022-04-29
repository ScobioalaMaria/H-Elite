import argparse
import os
from queue import Empty
from unittest import result
import functions
import artist

parser = argparse.ArgumentParser(prog='h-elite',
                                 description='Welcome to H-Elite! '
                                 'This program lets you save and retrieve information about your favourite artists')

parser.add_argument('--view','-v',  action='store_true',
                    help='View all the saved artists in a table')

parser.add_argument('--add','-a', type=str, nargs=7, metavar=('name', 'surname', 'birthday*dd/mm/yyyy*', 'gender', 'nationality', 'year_of_death', 'movement'),
                    help='Add an artist to the file')

parser.add_argument('--search','-s', type=str, nargs=1, metavar=('name_or_surname'),
                    help='Search an artist by inputting its name or surname')

parser.add_argument('--movement','-m', type=str, nargs=1, metavar=('movement'),
                    help='Search for artists by inputting their movement')

parser.add_argument('--compare','-c', type=str, nargs=1, metavar=('artist'),
                    help='Compare artists by nationality and movement by inputting ones name')

args = parser.parse_args()
###
if not any(vars(args).values()):
    print("Good morning, you have not made any selection,\nplease use:  \nmain.py -h \nor \nmain.py --help")
### 

if args.view:
    print((functions.loadCSV()))
    result = functions.createObjectList(functions.loadCSV())
    functions.displayObject(result)

if args.add:
    temp_dict= {}
    name = args.add[0]
    surname = args.add[1]
    name_surname = name + ' ' + surname
    temp_dict['name_surname'] = name_surname
    temp_dict['birthday'] = args.add[2]
    temp_dict['gender'] = args.add[3]
    temp_dict['nationality'] = args.add[4]
    temp_dict['ydeath'] = args.add[5]
    temp_dict['movement'] = args.add[6]
    result = functions.addArtist(temp_dict)
    print("Success I added the following into the CSV file!")
    functions.displayObject(result)

if args.search:
    result = functions.search(args.search[0])
    if result:
        functions.displayObject(result)
    else:
        print("Sorry no matches found")

if args.movement:
    result = functions.searchMovement(args.movement[0])
    if result:
        functions.displayObject(result)
    else:
        print("Sorry no matches found")

if args.compare:
    result = functions.compareArtists(args.compare[0])
    if result:
        functions.displayObject(result)
    else:
        print("Sorry no matches found")
