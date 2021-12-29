import csv
fields = ['Name', 'IIT-', 'Year', 'GPA']
rows = [['Karibasappa', 'BOM', '4', '9.8'],
        ['karrishma', 'DEL', '4', '9.71'],
        ['James hunt', 'MAD', '3.5', '9.7'],
        ['Sambit ', 'KAN', '4', '9.5'],
        ['Prajwall ', 'DHW', '3', '9.9'],
        ['Maleguldhu', 'BHU', '2', '9.7']]
filename = "RA&W agents from IIT.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
