import file_functions as ff
from docx2pdf import convert
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog


#arch_word = ff.open()
    
#direct_to_save = ff.directory_to_save()


#WORD TO PDF
#convert(arch_word,direct_to_save)

#IMAGEN TO PDF

arch_image = ff.open(".jpg")
direct_to_save = ff.directory_to_save(".pdf")

if direct_to_save:
    can = canvas.Canvas(direct_to_save, pagesize=letter)
    width, height = letter
    can.drawImage(arch_image,0,0,width,height)
    can.showPage()
    can.save()
    print("Conversion completada.")




