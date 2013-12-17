#
import sys
def read(data, file_name):
	f = open(file_name,'r')
	for line in f:
		data.append(line.split())
	data.pop(0)	
	f.close()

def unique_counts(part):
	result = {}
	for line in part:
		value = line[-1]
		if value not in result:
			result[value] = 1
		else:
			result[value] += 1
	return result
def gini_impurity(part):
	total = len(part)
	results = unique_counts(part)
	imp = 0
	clases = results.keys()
	values = float(total)
	total_sum = 0
	for i in range(len(results)):
		t = results[clases[i]]/ values
		print "probability of ", clases[i], " = " , t
		imp += (t)*(t)
		print "Gini index = ", 1-imp
	return imp

if __name__ == "__main__":
		data = []
		read(data, sys.argv[1])
		gini_impurity(data)

