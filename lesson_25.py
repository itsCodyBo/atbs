def main():
	
	return 0
if __name__ == '__main__':
	main()
import re

#you can use ? to optionally match based on a certain pattern. Group 2 displays batman
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print 'Use ? to optionally select a phrase: '   
print mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
print 'Same search but for Batwoman in Phrase:'
print mo2.group()
#make area code optional in phone number search from last lesson
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print 'Optionally search with area code:'
print mo1.group()
mo2 = phoneRegex.search('My number is 555-4242')
print "Optionally search without area code:"
print mo2.group()

#Matching all instances using *
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print 'One instance of Batman, using * to find all instances with or w/o (wo):'
print mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
print 'One instance of Batwoman using *:'
print mo2.group()
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
print 'One instance of Batwowowowowowoman using *:'
print mo3.group()

#Matching one or more with +. Group preceding + must appear at least once
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print 'Search for Batwoman using +:'
print mo1.group()
mo2 = batRegex.search('The adventures of Batwowowowowoman')
print 'Search through Batwowowowoman:'
print mo2.group()
mo3 = batRegex.search('The Adventures of Batman')
print 'Search for batwoman in batman:'
print mo3 == None

#Using {} in order to specify repeting patterns. Important step
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print 'Search "HaHaHa" for a match using (Ha){3}:'
print mo1.group()
mo2 = haRegex.search('Ha')
print 'Search in "Ha" using (Ha){3}:'
print mo2 == None

#Python is greedy by Default (grabs longest string). See following:
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print 'This is the Greedy regEx search using {3,5}:'
print mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
print 'This is the Non-Greedy regEx search using {3,5}?:'
print mo2.group()

#The findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print 'Using .search() to search for multiple numbers in a string:'
print mo.group()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print 'Using .findall() to find multiple numbers:'
print mo

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print 'Using .findall() to find multiple numbers with groups:'
print mo

#Using alternate character classes
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids\
7 swans, 6 geese, 5 rings, 4 birds, 3 hends, 2 doves, 1 partridge')
print "Use \s and \w to find phrases quicker:"
print mo

#creating you're own character classes using []
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print 'Search using custom character class [aeiouAEIOU]'
print mo

#use the caret (^) to return everything NOT specified
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print 'Find consonants in previous example using ^:'
print mo

#use ^ to ensure that the message begins with 'Hello'
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello World!')
print "check if message begins with hello using ^:"
print mo.group()
mo = beginsWithHello.search('He said hello.') 
print mo == None

#Use r'\d$' to find string matches that end with a numberic character 0 to 9
endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print 'Check to see if string ends with number using $'
print mo.group()

#use the wildcard . to search for any character that isn't a new line
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print 'Search for .at in "the cat in the hat sat on the flat mat.":'
print mo

#match everything with .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Cody Last Name: Bordelon')
print 'Find First Name:'
print mo.group(1)
print 'Find Last Name:'
print mo.group(2)
#use re.DOTALL to find all matching objects including new lines
noNewlineRegex = re.compile('.*')
print 'Do Not Include new line elements in search:'
print noNewlineRegex.search('Server the public trust. \nProtect the innocent.\nUphold the law.').group()

newlineRegex = re.compile('.*',re.DOTALL)
print 'Include new lines in search using re.DOTALL:' 
print newlineRegex.search('Server the public trust. \nProtect the innocent.\nUphold the law.').group()

#entering re.IGNORECASE or re.I as a 2nd argument to .compile() makes regex case insensetive
robocop = re.compile(r'robocop',re.I)
mo =robocop.search('Robocop is part man, part machine, all cop.')
print 'Search Robocop in case insenestive setting:'
print mo.group()
print robocop.search('ROBOCOP protects the innocent.').group()
print robocop.search('Al, why does your programming book talk about robocop so much?').group()

#can use .sub() to find and substitute text in regex string
namesRegex = re.compile(r'Agent \w+',re.I)
print "Replace Agent Names with CENSORED:"
print namesRegex.sub('CENSORED','Agent Alice gave the secret docs to agent Bob.')
#it is also possible to use the matched object as part of the sub
agentNamesRegex = re.compile(r'Agent (\w)\w*',re.I)
print "Include first letter of Agent's name in sub:"
print agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol thata Agent Eve knew Agent Bob was a double Agent.')

