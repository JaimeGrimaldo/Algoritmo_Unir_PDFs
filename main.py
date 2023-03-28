from PyPDF2 import PdfFileMerger

pdfs = ["hoja1.pdf", "hoja2.pdf"]
nombre_archivo_salida = "salida.pdf"
fusionador = PdfFileMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)