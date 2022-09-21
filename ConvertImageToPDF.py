import os
from PIL import Image
from fpdf import FPDF
from datetime import datetime

# Criar lista de arquivos do diretório
def files_path10(path): # return string list
    return [os.path.join(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]

print('pyPNGtoPDF v1.1')
print('Convert your files from PNG to PDF.')
print('')

# Declara variáveis
dirpath = 'D:\Coding\Python\pyPNGtoPDF\Convert'
listFiles = files_path10(dirpath)
l = []
now = datetime.now()
date_time = now.strftime("%m-%d-%Y")

# Insere arquivos PNG em lista específica
for file in listFiles:
    if str(file).endswith('png') == True:
        l.append(file)

if listFiles == []:
    print('--> Files not found.')
    exit()

# PDF único ou multiplo
PDFtype = input('Deseja converter todos os arquivos em um único PDF? [Y/N]')
if PDFtype.upper() == 'Y':
    outputname = input('Informe o nome do novo arquivo: ')
    if outputname == '':
        outputname = 'ConvertedFile'
    # Cria arquivo pdf
    i = 1
    pdf = FPDF()
    x, y = 0, 0
    for image in listFiles:
        pdf.add_page()
        pdf.image(image,x,y,w = pdf.epw,h = pdf.eph)
        print(str(i) +': " ' +image[:-4] +'.png" converted to', '"' +image[:-4]+'.pdf"') 
        i += i
    pdf.output(dirpath +"/" +outputname +"-" +date_time +".pdf", "F")
    print('Salvo em :' +'"' +dirpath +'/' +outputname +'-' +date_time +'.pdf"')
else:
    # Converte imagens para pdf
    print('Converting images to PDF')
    i = 1
    if len(l) == 0:
        print('--> Files not found.')
    for arc in l:
        filename = arc[:-4]
        image1 = Image.open(r'{}.png'.format(filename))
        imgConverted = image1.convert('RGB')
        imgConverted = image1.save(r'{}.pdf'.format(filename))
        print(str(i) +': " ' +filename +'.png" converted to', '"' +filename+'.pdf"')  
        i += i

print('Finished!')