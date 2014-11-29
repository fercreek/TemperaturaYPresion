import csv
with open('table.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ',quotechar = ',')
	for row in spamreader:
		print ", ".join(row)
		