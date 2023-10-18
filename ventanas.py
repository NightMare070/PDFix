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
    ventana_img.title("Extraer Texto")
    ventana_img.configure(background="#CFE1F7")
    ventana_img.geometry("300x300")
    ventana_img.resizable(False, False)
    ventana_img.iconbitmap("pdf.ico")

    tk.Label(ventana_img, text="Ingrese el primer número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=pgin, bg="white").pack(expand=True)
    tk.Label(ventana_img, text="Ingrese el último número de página: ", bg="white").pack(expand=True)
    tk.Entry(ventana_img, textvariable=pgfin, bg="white").pack(expand=True)
    tk.Button(ventana_img, text="Iniciar extracción de texto",bg="white", command=datos).pack(expand=True)

    ventana_img.mainloop()