def main():
	
	return 0
if __name__ == '__main__':
	main()



#import re module for regex

import re
#following line is telling re 'this is the program you're looking for'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#next line takes a string as an input and applies the regex to it
#call search of string and save it in variable mo if found
mo = phoneNumRegex.search('My number is 415-555-4242.')
#call .group() on mo to return the found match 'object (mo)
print '1. Phone number found: ' + mo.group()


#introduce groups into function
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
#print group 1,2,all,all
print 'MO GROUP 1:' + mo.group(1)
print 'MO GROUP 2:' + mo.group(2)
print 'MO GROUP 0:' + mo.group(0)
print 'ALL:' + mo.group()
#note that in 2.7 python recognizes the .groups() function as a tuple
#(cont.) thus the need for a str() call
print 'ALL IN GROUPS:' + str(mo.groups())
#assign specific groups to variables and call them
areaCode,mainNumber = mo.groups()
print "Area code:" + areaCode
print "Phone number:" + mainNumber

#use pipe | to search for one of many expressions. Batman or Tina Fey in this case
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print "Batman - group 1:" + mo1.group()
mo2 = heroRegex.search('Batman and Tina Fey.')
mo2.group()
print "Tina Fey - group 2:" + mo2.group()
#use pipe to search prefix "Bat" and endings man,mobile,copter,bat
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print 'Search "Batmobile lost a wheel":' + mo.group()
#Return only what is in the first parentheses group
print 'Return group 1 of previous search:'+mo.group(1)
