import json
import csv
from datetime import datetime

# select the file and load the data from the file using.
file = open("data.json")
data = json.load(file)
file.close()

with open("data.csv", mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=",", quotechar="|", quoting = csv.QUOTE_MINIMAL)
    writer.writerow(["","", "", "Inhale", "Hold 1", "Exhale", "Hold 2"])
    for name in data["users"]:
        writer.writerow([name])
        for date in data["users"][name]:
            d = datetime.strptime(date, '%a %b %d, %Y').strftime( '%a %b-%d-%Y')
            writer.writerow(["", d])
            for time in data["users"][name][date]:
                writer.writerow(["", "", time + ": ",\
                    data["users"][name][date][time]["exhale"],\
                    data["users"][name][date][time]["hold 1"],\
                    data["users"][name][date][time]["inhale"],\
                    data["users"][name][date][time]["hold 2"]\
                ])
        writer.writerow([])
    