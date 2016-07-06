def main():
	
	return 0
if __name__ == '__main__':
	main()

#Python 2.7
# phoneAndEmail.py - finds phone numbers and email addresses on clipboard.
#use sudo pip install pyperclip if you don't have it already on linux

import pyperclip , re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? 
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

#TODO:CREATE EMAIL REGEX
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

#TODO: FIND MATCHES IN CLIPBOARD TEXT. pyperclip.paste() returns string of clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

#TODO: COPY RESULTS TO CLIPBOARD
if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print 'Copied to clipboard:'
	print '\n'.join(matches)
else:
	print'No phone numbers or email adresses found :('
