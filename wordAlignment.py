# This script takes a time-alined .textgrid that marks pauses (in this
# case generated wtih the mark_pauses.praat script by Mietta Lennes) and 
# a list of the words read (in this case taken from a PsychoPy output file) 
# and puts the words in the correct places in the TextGrid. You can then use
# that for force alignment. 
#
# September 2015: Updated to run on all relevent files in a folder.
#
# This script was written by Rachael Tatman (rctatman at uw.edu) while at the 
# University of Washington. Devlopment of this script was made possible by 
# the National Science Foundation Graduate Research Fellowship Program.

# we'll need this later
import glob
import os

# finds every TextGrid.txt (Renamed text grids) in our current directory 
for filename in glob.iglob('*.TextGrid'):
	# opens existing file in same directory
	# inputWordlist should contain a list of words (or sentences; whatever stretch of 
	# text was deliniated by pauses) with each utterance as a new line. Do not include 
	# a header. 
	inputWordlist = open(filename.replace(".TextGrid", ".txt"), "r")
		
	# inputTextgrid should be a textgrid file with pauses deliniated. It should begin with a pause. 	
	inputTextgrid = open(filename, "r")

	# open a new file to write to 
	newFile = open((os.path.splitext(filename)[0]+ '_inserted.TextGrid'), "w")


	# set a counter to help us with stepping thorugh the lines of inputWordlist 
	i = 0
	# set up an object containing all the lines from inputWordlist
	lines=inputWordlist.readlines()

	# defines a function for determining if a number is odd
	def is_odd(num):
		return bool(i % 2)

	# Steps through our file and looks to see if this line should contian text information
	# if it does, it checks to see if the line count (i) is odd. (The first line, 0, is even and it
	# and every alternating subsecuent line should contain silences. If it is a silence, no change is
	# made and the text is copied exactly and the counter is iterated. If it is even (non-silent) then 
	# the next word from our wordlist textfile is inserted into the textgrid. 
	for line in inputTextgrid: 
		# checks to see if a line contains the string "text"
		if "text" in line:
			if is_odd(i):
				# get the next word from inputWordlist and saves it to a variable
				j = (i/2)
				word = lines[j]
				word = word.replace("\n", "")

				# iterate our counter
				i = i + 1 
	
				# writes the information you extracted to a new file in
				# correct textgrid syntax
				newline = '            text = ' + '"' + word + '" \n'
				newFile.write(newline)

			else:
				# copies the current line into our newfile, since there's no to copy here			
				newFile.write(str(line))
		
				# iterate our counter
				i = i + 1
		
		else:
			# copies the current line into our newfile		
			newFile.write(str(line))
	

print  filename + " done!"

# close our files
newFile.close()
inputTextgrid.close()
inputWordlist.close()
