import os
import glob
import csv
import random
with open ('C:/Users/pritam/Desktop/BTech Project 2/GA_ReliefShelter-master/getdata.csv', mode='w') as ofile:
	data_writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for filepath in glob.glob(os.path.join('C:/Users/pritam/Desktop/BTech Project 2/GA_ReliefShelter-master/my dataset','*.csv')):
		with open(filepath) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count<50:
					if list({row[10]})[0] in ['Rural']: 	
						data_writer.writerow([list({row[9]})[0],list({row[12]})[0],random.randint(1,20), round(random.uniform(0, 15), 1)])					
						line_count+=1
		
		

		
		
