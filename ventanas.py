import tkinter as tk
from tkinter import filedialog
from funtions import *

def ventanaTexto():
    def datos():
        pagin = int(pgin.get())
        pagfin = int(pgfin.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        extraer_Texto(archivo, pagin, pagfin)
    
    pgin = tk.StringVar()
    pgfin = tk.StringVar()
    
    ventana_texto = tk.Toplevel()
    ventana_texto.title("Extraer Texto")
    ventana_texto.configure(background="#CFE1F7")
    ventana_texto.geometry("300x300")
    ventana_texto.resizable(False, False)
    ventana_texto.iconbitmap("pdf.ico")

    tk.Label(ventana_texto, text="Ingrese el primer número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_texto, textvariable=pgin, bg="white").pack(expand=True)
    tk.Label(ventana_texto, text="Ingrese el último número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_texto, textvariable=pgfin, bg="white").pack(expand=True)
    tk.Button(ventana_texto, text="Iniciar extracción de texto",bg="white", command=datos).pack(expand=True)

    ventana_texto.mainloop()

def ventanaImagenes():
    def datos():
        pagin = int(pgin.get())
        pagfin = int(pgfin.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        extraer_Imagenes(archivo, pagin, pagfin)
    
    pgin = tk.StringVar()
    pgfin = tk.StringVar()
    
    ventana_img = tk.Toplevel()
    ventana_img.title("Extraer Imagenes")
    ventana_img.configure(background="#CFE1F7")
    ventana_img.geometry("300x300")
    ventana_img.resizable(False, False)
    ventana_img.iconbitmap("pdf.ico")

    tk.Label(ventana_img, text="Ingrese el primer número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=pgin, bg="white").pack(expand=True)
    tk.Label(ventana_img, text="Ingrese el último número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=pgfin, bg="white").pack(expand=True)
    tk.Button(ventana_img, text="Iniciar extracción de imagenes",bg="white", command=datos).pack(expand=True)

    tk.Button(ventana_img, text="Iniciar extracción de documentos",bg="white", command=datos).pack(expand=True)

def ventanaEncrypt():
    def datos():
        clave = str(password.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        encrypt(archivo, clave)
    
    password = tk.StringVar()
    
    ventana_img = tk.Toplevel()
    ventana_img.title("Encriptar PDF")
    ventana_img.configure(background="#CFE1F7")
    ventana_img.geometry("300x300")
    ventana_img.resizable(False, False)
    ventana_img.iconbitmap("pdf.ico")

    tk.Label(ventana_img, text="Ingrese la clave que se usara para desencriptar: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=password, bg="white").pack(expand=True)
    tk.Button(ventana_img, text="Iniciar la encriptación del PDF",bg="white", command=datos).pack(expand=True)

def ventanaDecrypt():
    def datos():
        clave = str(password.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        decrypt(archivo, clave)
    
    password = tk.StringVar()
    
    ventana_img = tk.Toplevel()
    ventana_img.title("Desencriptar PDF")
    ventana_img.configure(background="#CFE1F7")
    ventana_img.geometry("300x300")
    ventana_img.resizable(False, False)
    ventana_img.iconbitmap("pdf.ico")

    tk.Label(ventana_img, text="Ingrese la clave de desencriptación: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=password, bg="white").pack(expand=True)
    tk.Button(ventana_img, text="Iniciar la desencriptación del PDF",bg="white", command=datos).pack(expand=True)

def ventanaSeparar():
    def datos():
        pagin = int(pgin.get())
        pagfin = int(pgfin.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        separarPDF(archivo, pagin, pagfin)
    
    pgin = tk.StringVar()
    pgfin = tk.StringVar()
    
    ventana_img = tk.Toplevel()
    ventana_img.title("Separar páginas de PDF")
    ventana_img.configure(background="#CFE1F7")
    ventana_img.geometry("300x300")
    ventana_img.resizable(False, False)
    ventana_img.iconbitmap("pdf.ico")

    tk.Label(ventana_img, text="Ingrese el primer número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=pgin, bg="white").pack(expand=True)
    tk.Label(ventana_img, text="Ingrese el último número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=pgfin, bg="white").pack(expand=True)
    tk.Button(ventana_img, text="Iniciar separación de páginas",bg="white", command=datos).pack(expand=True)

def ventanaSello():
    def datos():
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        marca = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.img")])
        sello(archivo, marca)

    ventana_img = tk.Toplevel()
    ventana_img.title("Agregar sello")
    ventana_img.configure(background="#CFE1F7")
    ventana_img.geometry("300x300")
    ventana_img.resizable(False, False)
    ventana_img.iconbitmap("pdf.ico")

    tk.Button(ventana_img, text="Ingresa primero el archivo y despues el sello",bg="white", command=datos).pack(expand=True)

    ventana_img.mainloop()

def ventanaAgua():
    def datos():
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        marca = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.img")])
        marcaAgua(archivo, marca)

    ventana_img = tk.Toplevel()
    ventana_img.title("Agregar marca de agua")
    ventana_img.configure(background="#CFE1F7")
    ventana_img.geometry("300x300")
    ventana_img.resizable(False, False)
    ventana_img.iconbitmap("pdf.ico")

    tk.Button(ventana_img, text="Ingresa primero el archivo y despues la marca de agua",bg="white", command=datos).pack(expand=True)

    ventana_img.mainloop()