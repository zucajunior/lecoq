from selenium import webdriver
import time
import urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

driver.get("https://web.whatsapp.com/")

# Aguarde até que o usuário faça o login manualmente no WhatsApp Web
#input("Faça o login no WhatsApp Web e pressione Enter para continuar...")

# Número de telefone do destinatário
numero_destinatario = '991576676'

# Mensagem
mensagem = "Olá, aqui está o relatório em PDF!"

# Caminho do arquivo PDF
caminho_arquivo_pdf = f'C:/Users/zuca/Downloads/pedido_lecoq.pdf'

# Abre a conversa com o destinatário
driver.get(f"https://web.whatsapp.com/send?phone={numero_destinatario}&text={urllib.parse.quote(mensagem)}")
time.sleep(20)
driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
time.sleep(10)