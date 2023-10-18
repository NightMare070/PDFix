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
    
    ventana_img.mainloop()

def ventanaEncrypt():
    def datos():
        clave = str(password.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        encrypt(archivo, clave)
    
    password = tk.StringVar()
    
    ventana_enc = tk.Toplevel()
    ventana_enc.title("Encriptar PDF")
    ventana_enc.configure(background="#CFE1F7")
    ventana_enc.geometry("300x300")
    ventana_enc.resizable(False, False)
    ventana_enc.iconbitmap("pdf.ico")

    tk.Label(ventana_enc, text="Ingrese la clave que se usara para desencriptar: ", bg="white").pack(expand=True)
    tk.Entry(ventana_enc, textvariable=password, bg="white").pack(expand=True)
    tk.Button(ventana_enc, text="Iniciar la encriptación del PDF",bg="white", command=datos).pack(expand=True)
    
    ventana_enc.mainloop()

def ventanaDecrypt():
    def datos():
        clave = str(password.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        decrypt(archivo, clave)
    
    password = tk.StringVar()
    
    ventana_dec = tk.Toplevel()
    ventana_dec.title("Desencriptar PDF")
    ventana_dec.configure(background="#CFE1F7")
    ventana_dec.geometry("300x300")
    ventana_dec.resizable(False, False)
    ventana_dec.iconbitmap("pdf.ico")

    tk.Label(ventana_dec, text="Ingrese la clave de desencriptación: ", bg="white").pack(expand=True)
    tk.Entry(ventana_dec, textvariable=password, bg="white").pack(expand=True)
    tk.Button(ventana_dec, text="Iniciar la desencriptación del PDF",bg="white", command=datos).pack(expand=True)
    
    ventana_dec.mainloop()

def ventanaSeparar():
    def datos():
        pagin = int(pgin.get())
        pagfin = int(pgfin.get())
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        separarPDF(archivo, pagin, pagfin)
    
    pgin = tk.StringVar()
    pgfin = tk.StringVar()
    
    ventana_sep = tk.Toplevel()
    ventana_sep.title("Separar páginas de PDF")
    ventana_sep.configure(background="#CFE1F7")
    ventana_sep.geometry("300x300")
    ventana_sep.resizable(False, False)
    ventana_sep.iconbitmap("pdf.ico")

    tk.Label(ventana_sep, text="Ingrese el primer número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_sep, textvariable=pgin, bg="white").pack(expand=True)
    tk.Label(ventana_sep, text="Ingrese el último número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_sep, textvariable=pgfin, bg="white").pack(expand=True)
    tk.Button(ventana_sep, text="Iniciar separación de páginas",bg="white", command=datos).pack(expand=True)
    
    ventana_sep.mainloop()

def ventanaSello():
    def datos():
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        marca = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.img")])
        sello(archivo, marca)

    ventana_sel = tk.Toplevel()
    ventana_sel.title("Agregar sello")
    ventana_sel.configure(background="#CFE1F7")
    ventana_sel.geometry("300x300")
    ventana_sel.resizable(False, False)
    ventana_sel.iconbitmap("pdf.ico")

    tk.Button(ventana_sel, text="Ingresa primero el archivo y despues el sello",bg="white", command=datos).pack(expand=True)

    ventana_sel.mainloop()

def ventanaAgua():
    def datos():
        archivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        marca = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.img")])
        marcaAgua(archivo, marca)

    ventana_agu = tk.Toplevel()
    ventana_agu.title("Agregar marca de agua")
    ventana_agu.configure(background="#CFE1F7")
    ventana_agu.geometry("300x300")
    ventana_agu.resizable(False, False)
    ventana_agu.iconbitmap("pdf.ico")

    tk.Button(ventana_agu, text="Ingresa primero el archivo y despues la marca de agua",bg="white", command=datos).pack(expand=True)

    ventana_agu.mainloop()