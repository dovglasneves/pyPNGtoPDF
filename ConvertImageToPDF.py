import os
from os.path import expanduser
from xmlrpc.client import Boolean
from PIL import Image
from fpdf import FPDF
from datetime import datetime

# App main
def main():
    print('\npyIMGtoPNDF v1.2')
    print('Convert your images to pdf easier.')
    if checkEmptyFolder == False:
        exit(FileNotFoundError)
    convertPdf()

# List files in the directory
def files_path10(path): # return string list
    return [os.path.join(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]

# Global Variables
userfolder = expanduser("~")
dirpath = f'{userfolder}/Documents/Scanned Documents/Convert'.replace("\\","/")
outputpath = f'{userfolder}/Documents/Scanned Documents/'.replace("\\","/")
listFiles = files_path10(dirpath)
listImages = []
now = datetime.now()
date_time = now.strftime("%d-%m-%Y")
  
# Check empty list
def checkEmptyFolder() -> Boolean:
    if len(listImages) == 0:
        print('\n--> Error: The folder is empty.\n')
        return False
    else:
        return True

# Ask if the output will be multiple pdfs or a single pdf
def convertPdf():
    PDFtype = input('\nConvert files in a single PDF? [Y/N]')
    if PDFtype.upper() == 'Y':
        outputname = input('Insert a filename for the output: ')
        if outputname == '':
            outputname = 'ConvertedFile'
        i = 1
        n = 0
        pdf = FPDF()
        x, y = 0, 0
        for image in listImages:
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
            print(str(i) +': " ' +image[:-4] +'.png" converted.') 
            i += 1
        # Export the pdf and print result
        pdf.output(f'{outputpath}/{outputname}-{date_time}.pdf', 'F')
        for img in listImages:
            n += 1
            filedir, filename = os.path.split(img)
            filename, ext = os.path.splitext(filename)
            os.rename(img, f'{outputpath}{outputname} ({n}){ext}')
        print(f'Salvo em : "{dirpath}/{outputname}-{date_time}.pdf"')
    else:
        # Convert every image to a new pdf
        i = 1
        n = 0
        pdf = FPDF()
        x, y = 0, 0
        for image in listImages:
            img = Image.open(image)
            filedir, file = os.path.split(img)
            filename, ext = os.path.splitext(file)
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
            print(str(i) +': " ' +image[:-4] +'.png" converted.') 
            i += 1
            # Export the pdf and print result
            pdf.output(f'{outputpath}/{filename}-{date_time}.pdf', 'F')
            print(f'Salvo em : "{dirpath}/{filename}-{date_time}.pdf"')
        # Clear folder
        for img in listImages:
            n += 1
            filedir, file = os.path.split(img)
            filename, ext = os.path.splitext(filename)
            os.rename(img, f'{outputpath}{filename}-Converted{ext}')

    print('\nFinished!')

# Create imagelist
for file in listFiles:
    if str(file).endswith('png') or str(file).endswith('jpg') == True:
        listImages.append(file)

if __name__ == '__main__':
    main()