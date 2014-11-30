# import csv
# with open('table.csv', 'rb') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ',quotechar = ',')
# 	for row in spamreader:
# 		print "hola ", row[0]
# 		# print " , ".join(row)
# 		

# import csv
# from collections import defaultdict

# columns = defaultdict(list) # each value in each column is appended to a list

# with open('table.csv') as f:
#     reader = csv.DictReader(f) # read rows into a dictionary format
#     for row in reader: # read a row as {column1: value1, column2: value2,...}
#         for (k,v) in row.items(): # go over each column name and value 
#             columns[k].append(v) # append the value into the appropriate list
#                                  # based on column name k

# print(columns['Temp'] + columns["Densidad"])
import csv


try:
	with open('table.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			# print row[0]
			if '60' == row[0]:
				print "wuu"
				print row
finally: 
	f.close()


