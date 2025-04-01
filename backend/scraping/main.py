from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, time, os, zipfile
from selenium.webdriver.firefox.options import Options

pdf_links = []
options = Options()
options.add_argument("--headless")

# Cria uma instancia do firefox
browser = webdriver.Firefox(options=options)

# Entra no site
browser.get(
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
)
browser.maximize_window()

time.sleep(5)

try:
    print("Iniciando...")

    aceita_cookies = browser.find_element(
        By.XPATH, "/html/body/div[5]/div/div/div/div/div[2]/button[3]"
    )

    aceita_cookies.click()

    print("Cookies Aceito!")
except:
    print("Janela de Cookies não encontrada ou já estava fechada.")

# Pega os links do pdf no atributo href
pdf1_link = browser.find_element(
    By.XPATH,
    "/html/body/div[2]/div[1]/main/div[2]/div/div/div/div/div[2]/div/ol/li[1]/a[1]",
).get_attribute("href")
pdf2_link = browser.find_element(
    By.XPATH,
    "/html/body/div[2]/div[1]/main/div[2]/div/div/div/div/div[2]/div/ol/li[2]/a",
).get_attribute("href")

# Adiciona os links na lista
pdf_links.append(pdf1_link)
pdf_links.append(pdf2_link)

# Fecha o navegador
browser.quit()


# Itera sobre a lista e salva o indice númerico começando de 1
for i, link in enumerate(pdf_links, start=1):

    try:
        print(f"Baixando PDF {i}...")

        # Faz uma requisição GET para o servidor e guarda a resposta do servidor na variavel response.
        response = requests.get(link)

        # Caminho onde vai ser salvo o pdf e nome especifico.
        caminho = os.path.join("files", f"anexo{i}.pdf")

        # Salva o pdf no caminho especifico
        with open(caminho, "wb") as file:
            file.write(response.content)

        print(f"PDF {i} salvo.")

    except:
        print(f"Erro ao salvar o pdf {i}. ")

# Caminho onde vai ser criado o arquivo zip.
zip_path = os.path.join("files", "arquivos.zip")


# Cria arquivo .zip
try:
    print("Criando arquivo zip...")
    with zipfile.ZipFile(zip_path, "w") as zip:  # Cria o arquivo zip com os pdfs
        zip.write(os.path.join("files", "anexo1.pdf"), "anexo_1.pdf")
        zip.write(os.path.join("files", "anexo2.pdf"), "anexo_2.pdf")
        print("Arquivo zip criado. ")
except:
    print("Erro ao criar arquivo zip")
