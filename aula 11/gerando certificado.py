from docx import Document
from docx.shared import Pt

#Abre o arquivo do word
arquivoWord = Document("Certificado1.docx")

#seleciona o estilo
estilo = arquivoWord.styles["Normal"]
for paragrafo in arquivoWord.paragraphs:

    #Substitui o @nome pelo nome do aluno
    if '@nome' in paragrafo.text:
        paragrafo.text = "Kauã da Cunha Rodrigues"
        fonte = estilo.font
        fonte.name = "Calibri (Corpo)"
        fonte.size = Pt(24)

arquivoWord.save("Certificado.docx")
