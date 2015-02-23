
# This variable represents the data from the nycdonors-cleanme.csv file as a
# list, with each item representing a string for each row.
# You'll add your output data here, using the .append() method
data = open('harsh.csv','r').read().split('\r')[1:]
output=[]

for line in data:
# 	 print type(line)
	 line = line.split(',')
	 line[11] = line[11].upper()
	 line[15]= line[15].replace('&','')
	 line[20] = float(line[20])
	 output.append(line)
	 if line[20] > 5000.0 :
	  print line
for i in output:
	print i