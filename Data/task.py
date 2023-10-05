import aspose.words as aw

# Şablon belgeyi oluşturun
doc = aw.Document()

# Belgeye başlık eklemek için bir başlık paragrafı oluşturun
baslik = doc.sections[0].body.append_paragraph()
baslik.alignment = aw.ParagraphAlignment.CENTER
run = baslik.append_run("Kişisel Bilgiler")
run.bold = True

# İsim ve Soyisim yer tutucularını ekleyin
doc.sections[0].body.append_paragraph("Ad:")
doc.sections[0].body.append_paragraph("Soyad:")

# E-posta yer tutucusunu ekleyin
doc.sections[0].body.append_paragraph("E-posta:")

# Şablon belgeyi kaydedin
doc.save("sablon.docx")

# Şablon Word belgesini açın
doc = aw.Document("sablon.docx")

# Yer tutucuları doldurun
yer_tutucular = {
    "Ad:": "John",
    "Soyad:": "Doe",
    "E-posta:": "johndoe@example.com"
}

for section in doc.sections:
    for paragraph in section.body.paragraphs:
        for yer_tutucu, deger in yer_tutucular.items():
            if yer_tutucu in paragraph.text:
                for run in paragraph.runs:
                    run.text = run.text.replace(yer_tutucu, deger)

# Düzenlenmiş belgeyi kaydedin
doc.save("doldurulmus_belge.docx")
