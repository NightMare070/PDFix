import tkinter as tk
from tkinter import filedialog
from funtions import *
from ventanas import *

def docs():
    archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    extraer_Docs(archivo)

def merge():
    archivos = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    unirPDF(archivos)

def compress():
    archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    reducir(archivo)

# Crea una ventana principal
window = tk.Tk()
window.title("PDFix")
window.iconbitmap("pdf.ico")
window.geometry("300x300")
window.resizable(False, False)
window.configure(background="#CFE1F7")

# Agrega botones para cada función
btn_extraer_texto = tk.Button(window, text="Extraer Texto", command=ventanaTexto)
btn_extraer_texto.pack(expand=True)

btn_extraer_imagenes = tk.Button(window, text="Extraer Imagenes", command=ventanaImagenes)
btn_extraer_imagenes.pack(expand=True)

btn_extraer_docs = tk.Button(window, text="Extraer Documentos", command=docs)
btn_extraer_docs.pack(expand=True)

btn_encrypt = tk.Button(window, text="Encriptar", command=ventanaEncrypt)
btn_encrypt.pack(expand=True)

btn_encrypt = tk.Button(window, text="Desencriptar", command=ventanaDecrypt)
btn_encrypt.pack(expand=True)

btn_merge = tk.Button(window, text="Unir PDFs", command=merge)
btn_merge.pack(expand=True)

btn_separar = tk.Button(window, text="Separar PDF", command=ventanaSeparar)
btn_separar.pack(expand=True)

btn_stamp = tk.Button(window, text="Sellar PDF", command=ventanaSello)
btn_stamp.pack(expand=True)

btn_watermark = tk.Button(window, text="Marca de Agua", command=ventanaAgua)
btn_watermark.pack(expand=True)

btn_compress = tk.Button(window, text="Comprimir PDF", command=compress)
btn_compress.pack(expand=True)

# Ejecuta la interfaz gráfica
window.mainloop()
