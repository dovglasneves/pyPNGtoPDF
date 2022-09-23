import os
from tkinter import W
from PIL import Image
from fpdf import FPDF
from datetime import datetime

# App title
print('\npyIMGtoPNDF v1.2')
print('Convert your images to pdf easier.')

# List files in the directory
def files_path10(path): # return string list
    return [os.path.join(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]

# Variables
dirpath = 'D:\Coding\Python\pyPNGtoPDF\Convert'
listFiles = files_path10(dirpath)
l = []
now = datetime.now()
date_time = now.strftime("%m-%d-%Y")

# Create imagelist
for file in listFiles:
    if str(file).endswith('png') or str(file).endswith('jpg') == True:
        l.append(file)

# Check for empty list
if len(l) == 0:
    print('\n--> Error: The folder is empty.\n')
    exit()

# Ask if the output will be multiple pdfs or a single pdf
PDFtype = input('\nConvert files in a single PDF? [Y/N]')
if PDFtype.upper() == 'Y':
    outputname = input('Insert a filename for the output: ')
    if outputname == '':
        outputname = 'ConvertedFile'
    i = 1
    pdf = FPDF()
    x, y = 0, 0
    for image in listFiles:
        img = Image.open(image)
        w, h = img.size
        w, h = float(w * 0.264583), float(h * 0.264583)
        # Difine the page format 
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
        # Define the orientation of the page
        orientation = 'P' if w < h else 'L'
        # Campare image size with the page size to define de page orientation
        w = w if w < pdf_size[orientation]['w'] else pdf_size[orientation]['h']
        h = h if h < pdf_size[orientation]['h'] else pdf_size[orientation]['w']
        # Add the page to the document
        pdf.add_page(orientation=orientation)
        pdf.image(image,x,y,h,w)
        print(str(i) +': " ' +image[:-4] +'.png" converted to', '"' +image[:-4]+'.pdf"') 
        i += 1
    # Export the pdf and print result
    pdf.output(dirpath +"/" +outputname +"-" +date_time +".pdf", "F")
    print('Salvo em :' +'"' +dirpath +'/' +outputname +'-' +date_time +'.pdf"')
else:
    # Convert all images to single pdfs
    print('Converting images to PDF')
    i = 1
    if len(l) == 0:
        print('\n--> Error: Files not found.\n')
    for arc in l:
        filename = arc[:-4]
        image1 = Image.open(r'{}.png'.format(filename))
        imgConverted = image1.convert('RGB')
        imgConverted = image1.save(r'{}.pdf'.format(filename))
        print(str(i) +': " ' +filename +'.png" converted to', '"' +filename+'.pdf"')  
        i += i
    print('Process complete: [' +str(i) +'/' +str(i) +']')

print('\nFinished!')