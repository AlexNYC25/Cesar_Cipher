
import string

programFinished = False
option = 0

def cypher(theString, shift):
	stringToBeReturned = ""
	loc = 0
	theShift = int(shift)
	#print(type(string.ascii_uppercase[(loc+theShift)%26]))
	for x in range(len(theString)):
		if ( theString[x].isalnum() ):
			if ( theString[x].isupper() ):
				loc = string.ascii_uppercase.index(theString[x])

				stringToBeReturned = stringToBeReturned + string.ascii_uppercase[(loc+theShift)%26]
			else:
				loc = string.ascii_lowercase.index(theString[x])
				stringToBeReturned = stringToBeReturned + string.ascii_lowercase[(loc+theShift)%26]
		else:
			stringToBeReturned += theString[x]
	return str(stringToBeReturned)

def deCypher(theString, shift):
	stringToBeReturned = ""
	loc = 0
	theShift = int(shift)
	for a in range(len(theString)):
		if ( theString[a].isalnum() ):
			if ( theString[a].isupper() ):
				loc = string.ascii_uppercase.index(theString[a])
				stringToBeReturned = stringToBeReturned + string.ascii_uppercase[(loc-theShift)%26]
			else:
				loc = string.ascii_lowercase.index(theString[a])
				stringToBeReturned = stringToBeReturned + string.ascii_lowercase[(loc-theShift)%26]
		else:
			stringToBeReturned += theString[a]
	return str(stringToBeReturned)


while(programFinished == False):
	print("Hello and welcome to the Cesar Cipher.")
	print("Enter 1 to cypher a text")
	print("Enter 2 to decypher a text")
	print("Enter 3 to end the program")
	option = input("What would you like to do today? ")

	if(int(option) == 1):
		print("Enter a string to be cyphered")
		stringToBeUsed = input()
		stm = " \" " + str(stringToBeUsed) + " \" "
		shift = input("What would you like the shift to be, ex. -4, 5, 6 ")
		print("The result is " + cypher( stm, int(shift)) + "\n" )
	elif(int(option) == 2):
		print("Enter the string to be decyphered ")
		stringToBeUsed = input()
		stm = " \" " + str(stringToBeUsed) + " \" "
		shift = input("What was the shift ")
		print("The result is: " + deCypher(stringToBeUsed, int(shift)) + "\n")
	elif(int(option) == 3):
		print("Ok ending progran now")
		programFinished = True

	else:
		print("Not a valid Input")




	
