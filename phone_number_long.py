def main():
	
	return 0
if __name__ == '__main__':
	main()

#long hand version to find number - non regex
#.isdecimal() == .isdigit in 2.7
#see if just a string is a number
def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdigit():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdigit():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdigit():
			return False
	return True

#check if there is a phone number in a string
message = "Call me at 415-555-1011 tomorrow,\
 415-555-9999 is my office."
for i in range(len(message)):
	chunk=message[i:i+12]
	if isPhoneNumber(chunk):
		print 'Phone number found: ' + chunk
print 'Done'
