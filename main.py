from docx import Document

def create_word_document(text):
    doc = Document()
    doc.add_paragraph(text)

    filename = "output.docx"
    doc.save(filename)
    print(f"Файл '{filename}' успешно создан.")

def main():
    user_input = input("Aslanbek Smagulov HW ")
    create_word_document(user_input)

if __name__ == "__main__":
    main()