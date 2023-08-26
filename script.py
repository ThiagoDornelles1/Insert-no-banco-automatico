import  PyPDF2

pdfreader = PyPDF2.PdfReader(open('ramais_certos.pdf', 'rb'))
# Extrair texto de todas as páginas
pdf_text = ""
for page_number in range(len(pdfreader.pages)):
        page = pdfreader.pages[page_number]
        pdf_text += page.extract_text()

# Analisar o texto para extrair dados
# Isso depende da formatação e estrutura do PDF, e pode ser mais complexo
# Neste exemplo, vamos supor que cada linha do texto contenha um registro com campos separados por vírgulas

insert_statements = []
table_name = "HmedProducao.ramais_emergencia"

for line in pdf_text.split("\n"):
    fields = line.split(",")  # Supondo que os campos estejam separados por vírgulas
    if len(fields) > 0:
       
        values = ", ".join(fields)
        insert_statement = f"INSERT INTO {table_name} (IdHospital, Ramal, Descricao, Setor) VALUES (1, {values});"
        insert_statements.append(insert_statement)

# Juntar as instruções em uma única string
final_insert_string = "\n".join(insert_statements)

# Imprimir a string pronta para os inserts
print(final_insert_string)
