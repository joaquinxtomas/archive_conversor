from tkinter import filedialog

def open(filetype):
    arch = filedialog.askopenfilename(filetypes=[("Archivo", filetype)])
    if arch:
        print(f"Archivo seleccionado: {arch}")
        return arch
    
def directory():
    directory = filedialog.askdirectory()
    if directory:
        print(f"Direccion seleccionada: {directory}")
        return directory

def directory_to_save(typefile):
    filename = filedialog.asksaveasfilename(defaultextension=typefile)
    return filename