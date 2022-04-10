import csv
final_dict=[]

def loadCSV():
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
  
