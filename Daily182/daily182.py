from array import *

def readFile(fileName):
	file_contents = open(fileName, 'r')
	return file_contents.read();

def columnize():
	columnNum = int(raw_input("How many columns? "))
	columnWidth = int(raw_input("What is the width of each column? "))
	spaceWidth = int(raw_input("How much space between each column? "))
	inputFile = raw_input("What is the name of the input file? ")
	index = 0

	columnSpace = ""
	for x in range(0, spaceWidth):
		columnSpace += " "

	inputData = readFile(inputFile)
	length = len(inputData)
	lineNum = length / columnWidth
	lineNum += lineNum % columnWidth
	totalLines = lineNum / columnNum
	totalLines += lineNum % columnNum
	counter = 0
	index = array('i')
	index.append(0);

	# create the indices for the number of columns
	for x in range(1, (columnNum + 1)):
		if x == 1:
			index.append(0)
		else:
			index.append(((x - 1) * totalLines) * columnWidth)
		print index[x]

	# create output string
	output = ""

	while totalLines > 0:

		for x in range(1, (columnNum + 1)):
			i = 1
			while i <= columnWidth and index[x] < length:
				if inputData[index[x]] == "\n":
					output += "  "
					i += 1
					counter += 1
				else:	
					output += inputData[index[x]]
				index[x] += 1
				i += 1
				counter += 1
			output += "   "

		output += "\n"
		totalLines -= 1

	return output

print columnize()