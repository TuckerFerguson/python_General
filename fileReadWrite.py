#Author Tucker Ferugson
#writing and reading files in python

#Create and write to file 'test.txt'
fileWritten = open("test.txt","w")
fileWritten.write("one,\ntwo,\nthree")
fileWritten.close()

#Read from 'text'
fileOpened = open("test.txt","r")
outputList = fileOpened.readlines()

#should contain ['one\n','two\n','three']
print(outputList)