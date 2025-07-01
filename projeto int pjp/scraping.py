from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def extrair_perguntas_respostas():
    driver = webdriver.Chrome()
    driver.get('https://www.jovemprogramador.com.br/sobre.php')

    sleep(5)  # Aguarda o carregamento inicial

    perguntas = driver.find_elements(By.XPATH, "//h4[i[contains(@class, 'fa-arrow-down')]]")

    faq = []

    for pergunta in perguntas:
        try:
            pergunta.click()  # Expande a pergunta para revelar a resposta
            sleep(0.5)  # Dá tempo para expandir
        except:
            pass

    # Após expandir todas, extrair as perguntas e respostas visíveis
    perguntas = driver.find_elements(By.XPATH, "//h4[i[contains(@class, 'fa-arrow-down')]]")
    respostas = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'collapse-')]/div[@class='card-body']")

    for pergunta, resposta in zip(perguntas, respostas):
        pergunta_txt = pergunta.text.strip()
        resposta_txt = resposta.text.strip()
        faq.append({
            'pergunta': pergunta_txt,
            'resposta': resposta_txt
        })

    driver.quit()
    return faq

def salvar_em_txt(faq, nome_arquivo="dados.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for item in faq:
            arquivo.write(f"❓ {item['pergunta']}\n")
            arquivo.write(f"💬 {item['resposta']}\n")
            arquivo.write("-" * 40 + "\n")

# Executar extração e salvar
faq = extrair_perguntas_respostas()
salvar_em_txt(faq)

print("✅ Perguntas e respostas salvas com sucesso!")
