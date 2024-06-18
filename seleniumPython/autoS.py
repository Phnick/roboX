from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



options =webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(options=options,service=servico)


#  1- entrar no twiter
def entrar():
    navegador.get('https://x.com/i/flow/login')
    time.sleep(6)

#  2- clicar e digitar o email,celular ou nome do usuário
def click_digita_usuario():
    elemento = navegador.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    time.sleep(2)
    elemento.click()
    time.sleep(2)
    elemento.send_keys("usuário")
    time.sleep(2)

#-clicar no botão
def clica_botao():
    elemento2 = navegador.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
    elemento2.click()
    time.sleep(2)

# - Digitar senha
def digita_senha():
    elemento3 = navegador.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    time.sleep(2)
    elemento3.send_keys("senha")


# clicar no botão log in
def clica_botao_login():
    elemento4 = navegador.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button/div')
    time.sleep(2)
    elemento4.click()
    time.sleep(6)



#  clicar no serarch  
def clica_pesquisar():
    nome =["Band Jornalismo"]
    elemento5 = navegador.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
    elemento5.click()
    time.sleep(4)
    elemento5.send_keys(nome)
    time.sleep(4)
    elemento5.send_keys(Keys.ENTER)
    time.sleep(4)

# clicando no perfil e entrando na conta
def clica_perfil():
    clica_nome = navegador.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[3]/div/div/button/div')
    time.sleep(4)
    clica_nome.click()



# pegar os ultimos posts e printar na tela
def printando_tweet():
    time.sleep(4)
    # peguei o nome e printei
    nome = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/a/div/div[1]/span')
    nome_usuario =nome.text
    print('Novo tweet')
    print('Nome: ', nome_usuario)
    
    # Peguei o texto e printei
    texto = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]/div')

    teste = texto.text
    print('Texto: ', teste)
    

    #  Peguei video ou imagem
    img = navegador.find_element(By.CLASS_NAME,'css-9pa8cd')
    if img.get_attribute('src'):
        link_imagem = img.get_attribute('src')
        print('link img: ',link_imagem)

    else:
        print('Null')
    
    print()

# ----------------------------------------------
entrar()
click_digita_usuario()
clica_botao()          
digita_senha()
clica_botao_login()
clica_pesquisar()
clica_perfil()
time.sleep(3)
# --------------------------------------------------


id_usuario = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[3]/a")
link_id = id_usuario.get_attribute("href")
separa_id =link_id.split("/")[5]
print(separa_id)
ultimo_id = ''
i = 0
while i < 3:
    navegador.refresh()
    time.sleep(5)
    if separa_id != ultimo_id:
      printando_tweet()
      ultimo_id = separa_id
    else:
        print('Tweet igual')  
    time.sleep(7)
    
    i += 1
        



 






