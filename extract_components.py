# importing required modules
from PyPDF2 import PdfReader
import re
import sys

if __name__ == '__main__':
	# creating a pdf reader object
	#reader = PdfReader('Sony_BVM-D14_Service_Manual.pdf')
	#reader = PdfReader('Sony_BVM-A20F1U_ServiceManual.pdf')
	#reader = PdfReader('Sony_BVM-D9_Maintenance_Manual.pdf')
	reader = PdfReader(sys.argv[1])

	# printing number of pages in pdf file
	pages = len(reader.pages)

	# getting a specific page from the pdf file
	#page = reader.pages[0]

	# extracting text from page
	#text = page.extract_text()
	#print(text)

	# extract text and do the search
	print("Searching for 'Electrical Components List'")
	counter = 0

	doSearch = False

	for page in reader.pages:
		# Get text from current page
		try:
			text = page.extract_text()
		except:
			print("Failed to read page " + str(counter))

		# Look for parts list text
		found = text.lower().find("electrical parts list")
		if found != -1 and counter > 10:
			doSearch = True

		if doSearch:

			# Grab the next page and display it
			#print(text)

			# Parse page using sony part number REGEX:
			#n = re.split("[1-9]-\d{3}-\d{3}-\d{2}",text)
			#n = re.findall("[A-Z]{1,3}[0-9]{3,4} [1-9]-\d{3}-\d{3}-\d{2}",text)
			#n = re.findall("[A-Za-z0-9]+\s([0-9]+(-[0-9]+)+)(\s+([A-Za-z]+\s+)+)[0-9]*\.[0-9]+μ[A-Za-z]\s[0-9]+%\s[A-Za-z0-9]+",text)
			#board = re.findall("(A-[0-9]{4}-[0-9]{3}-A)([\s\S]*)\n",text)
			board = re.findall("(A-[0-9]{4}-[0-9]{3}-A)(.*?)\n",text)
			lines = re.findall("(C[0-9]{3,4})(.*?)(µF|PF)(.*?)(V)",text)

			if len(board) > 0:
				print(board)
			if len(lines) > 0:
				print(lines)

			if len(lines) > 0:
				with open('output.txt', 'a') as f:
					if len(board) > 0:
						f.write(" ".join(board[0]))
						f.write('\n')
					for line in lines:
						f.write(" ".join(line))
						f.write('\n')

		# Increment Counter
		counter = counter + 1
		print("Searching Page " + str(counter) + "/" + str(pages))
