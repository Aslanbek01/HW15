from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

doc = Document()
doc.add_paragraph('Hello Python', 'Title')
doc.save(r"C:\Users\Aslan\Desktop\HW15.docx")

doc = Document(r"C:\Users\Aslan\Desktop\HW15.docx")
for para in doc.paragraphs:
    for run in para.runs:
        if run.bold:
            print(run.text)

new_doc = Document()
para = new_doc.add_paragraph('Новый абзац текста')
run = para.runs[0]
run.font.name = 'Arial'
run.font.size = Pt(14)
para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
new_doc.save(r"C:\Users\Aslan\Desktop\HW15.docx")
print(run.bold)
print(para.alignment)