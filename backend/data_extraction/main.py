import os, zipfile
import tabula
import PyPDF2
import pandas as pd

# Caminho do PDF
path_pdf = os.path.join("..", "scraping", "files", "anexo1.pdf")
print(f"Caminho do PDF: {path_pdf}")

df_final = []

with open(path_pdf, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    total_pages = len(reader.pages)

pages_to_read = f"{3}-{total_pages}"


# Ler o conteúdo do PDF (em formato de tabelas)
pdf = tabula.read_pdf(path_pdf, pages=pages_to_read, multiple_tables=True, lattice=True)

# Exibir as tabelas extraídas do PDF
print(pdf)
for i, table in enumerate(pdf):
    print(f"Tabela {i+1}:")
    print(table)

    # Limpar os nomes das colunas
    table.columns = table.columns.str.strip()

    # Tratar as quebras de linha nas células (aplicar nas colunas)
    for col in table.columns:
        table[col] = table[col].apply(
            lambda x: " ".join(x.splitlines()) if isinstance(x, str) else x
        )

    # Adicionar a tabela limpa à lista final
    df_final.append(table)

# Salvar o DataFrame ajustado em CSV
df_final = pd.concat(df_final, ignore_index=True)

# Troca o nome das colunas conforme solicitado no exercicio
df_final.rename(
    columns={"OD": "Seg.Odontológica", "AMB": "Seg.Ambulatorial"}, inplace=True
)


# Salvar o DataFrame final em CSV
df_final.to_csv("tabelas.csv", index=False, sep=";", encoding="utf-8-sig")

# Confirmar se o arquivo CSV foi criado
print("CSV convertido com sucesso!")

# Transformar em .zip
try:

    zip_path = os.path.join("Teste_Davi_Araujo_Alves.zip")
    print("Criando arquivo zip...")
    with zipfile.ZipFile(
        zip_path, "w"
    ) as zip:  # Cria o arquivo zip com os pdfs e renomeia.
        zip.write(os.path.join("tabelas.csv"), "tabelas.csv")

        print("Arquivo zip criado. ")
except:
    print("Erro ao criar arquivo zip")
