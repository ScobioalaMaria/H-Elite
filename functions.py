import csv
import artist
import string
from prettytable import PrettyTable as pt

def loadCSV() -> list:
    """The function loads the CSV file into a dictionary
    making it easier to use"""
    final_list = []
    with open('artists.csv', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        for row in reader[1:]:
            temp_list = {}
            temp_list["name_surname"] = row[0]
            temp_list["birthday"] = row[1]
            temp_list["gender"] = row[2]
            temp_list["nationality"] = row[3]
            temp_list["ydeath"] = row[4]
            temp_list["movement"] = row[5]
            final_list.append(temp_list)
    return final_list


def createObjectList(lista: list):
    """It creates a list of objects Artist starting from 
    a list"""
    result_list = []
    for i in lista:
        oggetto = artist.Artist(i['name_surname'],
                                i['birthday'],
                                i['gender'],
                                i['nationality'],
                                i['ydeath'],
                                i['movement'])
        result_list.append(oggetto)
    return result_list

def displayObject(lista: list):
    """It prints nicely from a list of objects"""
    tb = pt()
    tb.title = 'H-ELITE results of the query'
    tb.field_names = ["Name & Surname", "Birthday",
                      "Gender", "Nationality", "Year of death", "Movement"]
    for obj in lista:
        tb.add_row([obj.name_surname, obj.birthday, obj.gender,
                   obj.nationality, obj.death, obj.movement])
    print(tb)
    return

def writeCSV(dictionary: dict):
    """It writes a new line into the CSV file
    from a dictionary"""
    with open('artists.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([dictionary['name_surname'],
                         dictionary['birthday'],
                         dictionary['gender'],
                         dictionary['nationality'],
                         dictionary['ydeath'],
                         dictionary['movement']])
    return

def addArtist(dictionary: dict) -> artist.Artist :
    """It adds the information in the dictionary into the CSV file"""
    writeCSV(dictionary)
    lista=[dictionary]
    oggetto = createObjectList(lista)
    return oggetto

def search(searchW: string):
    """Search function, searches inside the CSV file and returns a list 
    with objects that correspond to the search done"""
    with open('artists.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result_list_t = []
        for line in csv_reader:
            if searchW.casefold() in line['name_surname'].casefold():
                result_list_t.append(line)
        print(result_list_t)
    result_list = createObjectList(result_list_t)
    return result_list

def searchMovement(searchW: string):
    """Search function, searches inside the CSV file and returns a list 
    with objects that correspond to the search done"""
    with open('artists.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result_list_t = []
        for line in csv_reader:
            if searchW.casefold() in line['movement'].casefold():
                result_list_t.append(line)
    result_list = createObjectList(result_list_t)
    return result_list

def compareArtists(searchW: string):
    """Compare artists function, given an artist, 
    it shows you the artist and all the other artists
    that have the same nationality and the same art movement"""
    artist_found = search(searchW)
    if artist_found:
        with open('artists.csv', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            result_list_t = []
            for line1 in csv_reader:
                if artist_found[0].nationality in line1['nationality']:
                    if artist_found[0].movement in line1['movement']:
                        result_list_t.append(line1)
        result_list = createObjectList(result_list_t)
        return result_list
    else:
        return []
