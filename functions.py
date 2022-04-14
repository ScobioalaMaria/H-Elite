import csv
from operator import truediv
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
            temp_dict["death"] = row[4]
            temp_dict["movement"] = row[5]
            final_dict.append(temp_dict)
    return final_dict

def createObject(dictionary: dict):
    """It creates an object Artist starting from 
    a dictionary"""
    object = artist.Artist(dictionary['name_surname'], 
                           dictionary['birthday'], 
                           dictionary['gender'], 
                           dictionary['nationality'],
                           dictionary['death'],
                           dictionary['movement'])
    return object

def writeCSV(dictionary: dict):
    """It writes a new line into the CSV file
    from a dictionary"""
    with open('artists.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([dictionary['name_surname'], 
                           dictionary['birthday'], 
                           dictionary['gender'], 
                           dictionary['nationality'],
                           dictionary['death'],
                           dictionary['movement']])
    return 

def addArtist():
    """It requests the informations and creates a dictionary"""
    temp_dict = {}
    temp_dict["name_surname"] = input("Enter the name and surname: ")
    temp_dict["birthday"] = input("Enter the birthday dd/mm/yyyy: ")
    temp_dict["gender"] = input("Enter the gender: ")
    temp_dict["nationality"] = input("Enter the nationality: ")
    temp_dict["death"] = input("Enter the year of death yyyy: ")
    temp_dict["movement"] = input("Enter the movement: ")
    writeCSV(temp_dict)
    return
