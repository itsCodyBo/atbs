def main():
	
	return 0
if __name__ == '__main__':
	main()

#The following is chapter 8 - Reading and Writing Files from ATBS
#returns a files path using correct path seperators

import os
import shelve
import pprint

'''
print 'Print file path:'
print os.path.join('usr','bin','spam')
#creates a string for the following file names
myFiles = ['accounts.txt','details.csv','invite.docx']
print "Join string filenames together in a path string:"
for filename in myFiles:
	print os.path.join('/usr/cody/filename')

#find the working directory
print "Print working directory:"
print os.getcwd()
#change working directory
os.chdir('/home')
print 'Change working directory:'
print os.getcwd()

#make a new directory
os.makedirs('/delicious/walnut/waffles')
'''
'''
#HANDLING ABSOLUTE AND RELATIVE PATHS
#print an absolute path and check if a path is absolute
print 'Print absolute path:'
print os.path.abspath('.')
print 'Print absolute path of script:'
print os.path.abspath('./Scripts')
print 'Check if path is absolute:'
print os.path.isabs('.')
print 'Check if path is absolute for an absolute path:'
print os.path.isabs(os.path.abspath('.'))
print "Print relative path:"
print os.path.relpath('/home','/')
print "Print relative path:"
os.path.relpath('/home','/spam/eggs')
print "Print working directory:"
print os.getcwd()


#find the path using the basename
path = '/home/cody/workspace/first_server/src/server'
print "Prints the basename, or file:"
print os.path.basename(path)
print "Print the directory path:"
print os.path.dirname(path)

#used calc path in book, serverpath used here
#get a path's dir name and base name together as tuples
server_path = '/home/cody/workspace/first_server/src/server'
print "Print directory path and basename:"
print os.path.split(path)


#Finding Files Sizes and Folder Contents
print 'Print size in bytes of path:'
print os.path.getsize('/home/cody/workspace')
print 'Print filename as strings in path:'
print os.listdir('/home/cody/workspace')

print 'Use listdir() and getsize() together:'
totalSize = 0
for filename in os.listdir('/home/cody/workspace'):
	totalSize = totalSize + os.path.getsize(os.path.join('/home/cody/workspace'))
print totalSize	


#checking path validity
print 'Check if file or folder path exists:'
print os.path.exists('/home')
print 'Check if a fake folder is or file path exists:'
print os.path.exists('/some_made_up_folder')
print 'Check if the path exists AND if it is a directory:'
print os.path.isdir('/home')
print 'Check if the path exists AND if it is a file:'
print os.path.isfile('/home/cody/release.key')
print os.path.isfile('/home/cody/workspace/weekdays.py')


#This starts the reading and writing portion of chapter 8
#open hello.txt document in read mode

helloFile = open('/home/cody/workspace/ATBS/hello.txt','r')
print 'Calling open() returns a file object:'
print helloFile

#the read method will return the file contents as a string
helloContent = helloFile.read()
print 'This is the string that read() returns from the file:'
print helloContent


#read line by line using readlines() to return a list of strings
sonnetFile = open('sonnet29.txt')
print 'Use readlines() to return individual strings'
print sonnetFile.readlines()


#reading and writing files 
#write mode will overwrite the existing file and start from scratch, append will add text to end of existing file
baconFile = open('bacon.txt','w')
baconFile.write('Hello World!\n')
#Now we close the file and then open it again to append a new sentence
baconFile.close()
baconFile = open('bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
#baconFile is returning file objects b/c we have not closed it yet and read() it 
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print 'baconFile after we created it with w and appened to it with a:'
print content


#Saving Variables with the Shelf Module
#Shelve is used to store variables as binary data

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
print 'We should now have a mydata.db file in the current working directory:'
print os.listdir

#once opened, shelf files can be read and written on
#shelfFile type and read, returns instance in 2.7?
shelfFile = shelve.open('mydata')
print type(shelfFile)
print shelfFile['cats']
print shelfFile.close()

#shelve files have keys and values just like dicts
print 'Print shelve file values:'
shelfFile = shelve.open('mydata')
print list(shelfFile.values())
print 'Print shelve value keys:'
print list(shelfFile.keys())



#Use pprint.pprint() save dict as a string and write it to python file
import pprint
cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
print 'Use pprint.pprint() to pretty print the dict input:'
print pprint.pformat(cats)
fileObj = open('myCats.py','w')
fileObj.write('cats = ' + pprint.pformat(cats) +'\n')
fileObj.close()
'''

