# coincidenceIndex

The coincidence index of a piece of text is used in cryptography.
https://en.wikipedia.org/wiki/Index_of_coincidence

This is a simple python app that takes in a string or image of some text and calculates the coincidence index.
Reading text imput requires no additional setup, however reading from an image does.

It uses python tesseract ocr to convert an image to text
To set up on Linux:
1) sudo apt-get install tesseract-ocr
2) pip3 install pytesseract pillow
