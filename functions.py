import csv
import artist
final_dict=[]

def loadCSV() -> dict:
    """The function loads the CSV file into a dictionary
    making it easier to use"""
    with open('artists.csv', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        for row in reader[1:]:
            temp_dict = {}
            temp_dict["name_surname"] = row[0]
            temp_dict["birthday"] = row[1]
            temp_dict["gender"] = row[2]
            temp_dict["nationality"] = row[3]
            temp_dict["ydeath"] = row[4]
            temp_dict["movement"] = row[5]
            final_dict.append(temp_dict)
    return final_dict

def createObjectList(lista: list):
    """It creates a list of objects Artist starting from 
    a list"""
    result_list = []
    for i in lista:
        oggetto=artist.Artist(i['name_surname'], 
                           i['birthday'], 
                           i['gender'], 
                           i['nationality'],
                           i['ydeath'],
                           i['movement'])
        result_list.append(oggetto)
    return result_list

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

def addArtist():
    """It requests the informations and creates a dictionary"""
    temp_dict = {}
    temp_dict["name_surname"] = input("Enter the name and surname: ")
    temp_dict["birthday"] = input("Enter the birthday dd/mm/yyyy: ")
    temp_dict["gender"] = input("Enter the gender: ")
    temp_dict["nationality"] = input("Enter the nationality: ")
    temp_dict["ydeath"] = input("Enter the year of death yyyy: ")
    temp_dict["movement"] = input("Enter the movement: ")
    writeCSV(temp_dict)
    return

def search(searchW: string):
    """Search function, searches inside the CSV file and returns a list 
    with objects that correspond to the search done"""
    with open('artists.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result_list_t = []
        for line in csv_reader:
            if searchW in line['name_surname']:
                result_list_t.append(line)
    result_list = createObjectList(result_list_t)
    return result_list

def compareArtists(searchW: string):
    """Compare artists function, given an artist, 
    it shows you the artist and all the other artists
    that have the same nationality and the same art movement"""
    artist_found = search(searchW)
    with open('artists.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result_list_t = []
        for line1 in csv_reader:
            if artist_found[0].nationality in line1['nationality']:
                if artist_found[0].movement in line1['movement']:
                    result_list_t.append(line1)
    result_list = createObjectList(result_list_t)
    return result_list
