from pypdf import PdfReader, PdfWriter, Transformation
import img2pdf
from os import remove

def extraer_Texto(archivo, pagin, pagfin):
    reader = PdfReader(open(archivo, "rb"))

    open(f"{archivo}.txt","w").close()
    for i in range((pagin - 1), pagfin):
        page = reader.pages[i]
        with open(f"{archivo}.txt","at") as fp:
            fp.write(page.extract_text())

def extraer_Imagenes(archivo, pagin, pagfin):
    reader = PdfReader(open(archivo, "rb"))
    count = 0

    for i in range((pagin - 1), pagfin):
        page = reader.pages[i]

        for image_file_object in page.images:
            with open( str(count) + image_file_object.name, "wb") as fp:
                fp.write(image_file_object.data)
                count += 1

def extraer_Docs(archivo):
    reader = PdfReader(open(archivo, "rb"))

    for name, content_list in reader.attachments:
        for i, content in enumerate(content_list):
            with open(f"{name}-{i}", "wb") as fp:
                fp.write(content)

def encrypt(archivo, clave):
    reader = PdfReader(archivo)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(clave, algorithm="AES-256")

    with open(f"{archivo}-encriptado.pdf", "wb") as f:
        writer.write(f)

def decrypt(archivo, clave):
    reader = PdfReader(open(archivo, "rb"))
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt(clave)

    for page in reader.pages:
        writer.add_page(page)

    with open(f"{archivo}-desencriptado.pdf", "wb") as f:
        writer.write(f)

def unirPDF(archivos):
    merger = PdfWriter()

    for pdf in archivos:
        merger.append(pdf)

    merger.write("merged.pdf")
    merger.close()

def separarPDF(archivo, pagin, pagfin):
    reader = PdfReader(open(archivo, "rb"))
    
    for i in range((pagin - 1), pagfin):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        writer.write(f"{archivo}-page-{i+1}.pdf")
        writer.close()

def sello(archivo, marca, escalado):
    with open("sello.pdf", "wb") as documento:
        documento.write(img2pdf.convert(marca))
    
    stamp = PdfReader('sello.pdf').pages[0]
    writer = PdfWriter(clone_from=archivo)
    
    for page in writer.pages:
        page.merge_transformed_page(stamp,Transformation().scale(escalado), over=True,)

    writer.write(f"{archivo}-sellado.pdf")
    remove("sello.pdf")

def marcaAgua(archivo, marca, escalado):
    with open("marca.pdf", "wb") as documento:
        documento.write(img2pdf.convert(marca))
    
    stamp = PdfReader('marca.pdf').pages[0]
    writer = PdfWriter(clone_from=archivo)
    
    for page in writer.pages:
        page.merge_transformed_page(stamp,Transformation().scale(escalado), over=False,)

    writer.write(f"{archivo}-marcado.pdf")
    remove("marca.pdf")

def reducir(archivo):
    reader = PdfReader(archivo)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        page.compress_content_streams()

    with open(f"{archivo}-comprimido.pdf", "wb") as f:
        writer.write(f)