#!/usr/bin/python

#uses pytesseract to convert image to text
#this will not always be 100% accurate
import pytesseract
from PIL import Image
import string

print('This program calculates the co-incidence index of a piece of text') 
print('Press 1 to enter a file path to an image\nPress 2 to enter text directly')


#calculates the co-incidence index
def calcIndex(text):
	parsed = ''.join(filter(str.isalpha, text))
	parsed = parsed.lower() 
	frequency = dict.fromkeys(string.ascii_lowercase, 0)


	for i in range(len(parsed)):
		frequency[parsed[i]] += 1

	sumFreq = 0
	for i in string.ascii_lowercase:
		sumFreq += (frequency[i] * (frequency[i] - 1))

	return  sumFreq / (len(parsed) * (len(parsed)-1))


#handles input/output
text = input()
while text != '1' and text != '2':
	text = input()
	print('please enter a valid input')	

index = 0

if text == '1':
	print('enter file path')	
	text = input()
	img = Image.open(text)
	text = pytesseract.image_to_string(img, lang="eng")
	print(text)
	index = calcIndex(text)		
else:
	print('enter text')
	text = input()
	index = calcIndex(text)

print("The co-incedece index is: %8.4f" %(index))
