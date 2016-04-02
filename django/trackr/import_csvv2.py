import csv
from .map import models

def import_csv(csv_file):
    f = open(csv_file, 'rt')
    try:
        reader = csv.reader(f)
        for count, row in enumerate(reader):
            if (count == 0):
                row = row
            else:
                new_data = migration_csv_import(event_id=row[0], timestamp=row[2],
                    location_long=row[3], location_lat=row[4], individual_local_identifier = row[12],
                    study_name='white fronted goose')
                new_data.save()
    finally:
        f.close()