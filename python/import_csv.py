import csv
import sys
import models

# Input data into row for SQL database
def inputLocforAnimal(unique_animal, loc_point, row):
    if unique_animal.tag_id != row[11]:
        new_unique_animal = Animal(animal_name="white-fronted-goose", tag_id=row[11])
        new_loc_point = new_unique_animal_set.create(timestamp=row[2],
            location_long=int(row[3]), location_lat=int(row[4]),
            migration_stage=row[7], miration_status=row[8])
        return new_unqiue_animal
        new_loc_point
    else:



f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for count, row in enumerate(reader):
        if (count == 0):
            row = row
        else:
            inputLocforAnimal()
finally:
    f.close()
"""
def inputLocforAnimal(unique_animal, loc_point):
    loc_point.animal = unqi

f = open('*.csv', 'r')
unique_animal = Animal(animal_name=)
for count, line in enumerate(f):
    if (count === 0):
        line = line.split(',')
    else:
        line = line.split(',')
        if (line[13] != unique_animal.tag_id):
            new_unique_animal = Animal(animal_name=line[13], tag_id=line[11])
            unique_animal = new_unique_animal
        loc_point = LocationPoint(animal=unique_animal)
        loc_point.timestamp = line[2]
        loc_point.location_long = int(line[3])
        loc_point.location_lat = int(lint[4])
        loc_point.migration_status = ([line[7])"""


    