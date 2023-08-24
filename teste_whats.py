
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver

driver_path = f'F:/chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://web.whatsapp.com/")

# Aguarde até que o usuário faça o login manualmente no WhatsApp Web
input("Faça o login no WhatsApp Web e pressione Enter para continuar...")

# Número de telefone do destinatário
numero_destinatario = '+5544991576676'

# Mensagem
mensagem = "Olá, aqui está o relatório em PDF!"

# Caminho do arquivo PDF
caminho_arquivo_pdf = f'C:/Users/zuca/Downloads/pedido_lecoq.pdf'

# Abre a conversa com o destinatário
driver.get(f"https://web.whatsapp.com/send?phone={numero_destinatario}")

# Espere um pouco para que a página seja totalmente carregada
time.sleep(5)

# Insere a mensagem e pressiona Enter
mensagem_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="9"]')
mensagem_input.send_keys(mensagem)
mensagem_input.send_keys(Keys.ENTER)

# Espere mais um pouco antes de enviar o arquivo
time.sleep(5)

# Anexa o arquivo PDF
anexo_input = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
anexo_input.send_keys(caminho_arquivo_pdf)

# Espere um pouco antes de enviar
time.sleep(5)

# Envia o arquivo
enviar_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
enviar_button.click()

# Espere um pouco para que a mensagem seja enviada
time.sleep(5)

# Fecha o navegador
driver.quit()
