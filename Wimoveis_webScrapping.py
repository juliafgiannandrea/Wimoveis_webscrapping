from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options #para mudar o navegador, mudar aqui 
import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path
from dotenv import load_dotenv
import os 


#VARIÁVEIS DA BUSCA: 
TIPO = 'APARTAMENTO'
MODALIDADE = "VENDA"
ESTADO = "DF"
CIDADE = "BRASILIA / PLANO PILOTO"
BAIRRO = "ASA NORTE"
QUARTOS = "1"
VALOR = "2000000"
ENDERECO = "sqn 115"



options = Options() #personalização do navegador
url = "https://www.dfimoveis.com.br/" 
driver = webdriver.Chrome(options=options) #para mudar o navegador, mudar aqui 
driver.get(url)
wait = WebDriverWait(driver,10) #esperar o upload da página - para todos componentes aparecerem ao abrir a página


#para o robo fazer: (tipo o que faríamos com o mouse)

#MODALIDADE 
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-selection--single')))
element.click() #clica no componone
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-search__field') ))
element.send_keys(MODALIDADE)
element.send_keys(Keys.ENTER)

#TIPO 
xpath = "/html/body/main/div[1]/section/section[1]/div[2]/div/form/div[1]/div[2]/span/span[1]/span"
element2 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
element2.click()
element2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"select2-search__field" )))
element2.send_keys(TIPO)
element2.send_keys(Keys.ENTER)

#ESTADO: 
xpath = "/html/body/main/div[1]/section/section[1]/div[2]/div/form/div[1]/div[3]/span/span[1]/span/span[1]"
element3 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
element3.click()
element3 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"select2-search__field" )))
element3.send_keys(ESTADO)
element3.send_keys(Keys.ENTER)

#CIDADE: 
xpath = "/html/body/main/div[1]/section/section[1]/div[2]/div/form/div[1]/div[4]/span"
element4 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
element4.click()
element4 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"select2-search__field" )))
element4.send_keys(CIDADE)
element4.send_keys(Keys.ENTER)

#BAIRRO:
xpath = '/html/body/main/div[1]/section/section[1]/div[2]/div/form/div[1]/div[5]/span'
element5 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
element5.click()
element5 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"select2-search__field" )))
element5.send_keys(BAIRRO)
element5.send_keys(Keys.ENTER)


#QUARTOS: 
# xpath = "/html/body/main/div[1]/section/section[1]/div[2]/div/form/div[1]/div[6]/div[1]/span/span[1]/span"
# element6 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
# element6.click()
# element6_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"select2-search__field" )))
# element6_1.send_keys(QUARTOS)
# element6_1.send_keys(Keys.ENTER)

#VALOR:
xpath = "/html/body/main/div[1]/section/section[1]/div[2]/div/form/div[1]/div[6]/div[2]/input"
element7 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
element7.click()
element7.send_keys(VALOR)
element7.send_keys(Keys.ENTER)

#ENDEREÇO:
xpath = "/html/body/main/div[1]/section/section[1]/div[2]/div/form/div[1]/div[7]/input"
element8=  wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
element8.click()
element8.send_keys(ENDERECO)
element8.send_keys(Keys.ENTER)


#BUSCAR: 
botao_busca = wait.until(EC.element_to_be_clickable((By.ID, "botaoDeBusca")))
#botao_busca.click() #ESTÁ FUNCIONANADO SEM 

#RESULTADOS: 
sleep(5) #para esperar a página carregar
lst_imoveis = []
xpath_resultados = "/html/body/main/div[1]/div[1]/div[2]/div[2]/div[2]"
resultados = wait.until(EC.presence_of_element_located((By.XPATH, xpath_resultados)))

#links = resultados.find_elements(By.TAG_NAME, "a") 
links = [a.get_attribute("href") for a in resultados.find_elements(By.TAG_NAME, "a") if a.get_attribute("href")]
imoveis_encontrados = len(links)
print("Total de imóveis encontrados:", imoveis_encontrados)


for link in links:
    driver.get(link) #abre o link do imovel (página por página)
    imovel = {}
    
    title_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/div/div/div[3]/div/div[3]/h1")))
    imovel["titulo"] = title_element.text

    preco_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/div/div/div[3]/div/div[4]/div/h6/small")))
    imovel["preco"] = preco_element.text
    
    metragem_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/div/div/div[3]/div/div[5]/h6/small")))
    imovel["metragem"] = metragem_element.text

    quartos_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/div/div/div[3]/div/div[7]/div/div[3]/h6")))
    imovel["quartos"] = quartos_element.text


    suites_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/div/div/div[3]/div/div[7]/div/div[4]/h6")))
    imovel["suites"] = suites_element.text


    descricao_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div[1]/div/div/div[6]/p")))
    imovel["descricao"] = descricao_element.text

    imovel["link"] = link 
    
    lst_imoveis.append(imovel)

driver.quit() #fechar o navegador


#Data frame: 
df_resultados = pd.DataFrame(lst_imoveis)

#Tratamento dos dados retirados do site para inserção no banco de dados: 
df_resultados['quartos'] = df_resultados['quartos'].str.replace('Quartos: ', '', regex=False)
    
df_resultados['suites'] = df_resultados['suites'].str.replace('Suítes: ', '', regex=False)

df_resultados['descricao'] = df_resultados['descricao'].str.slice(0, 255)

#converter preço para float:
df_resultados['preco'] = df_resultados['preco'].str.replace(r'[^\d,]', '', regex=True)
df_resultados['preco'] = df_resultados['preco'].str.replace(',', '.').astype(float)



#Inserção dos resultados no banco de dados:  
load_dotenv() 
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
senha = os.getenv("PASSWORD")
database_name = os.getenv("DATABASE")

BASE_DIR = Path(__file__).parent 
DATABASE_URL = f'mysql+pymysql://{user}:{senha}@{host}:{port}/{database_name}'
engine = create_engine(DATABASE_URL)

df_resultados.to_sql('tb_imoveis', con=engine, if_exists='append', index=False)



#FALTA: 
#fazer o filtro de quantidade de quartos funcionar 

#fazer passar de página para pegar todos os resultados e não só o da primeira pág de resultados 
#usar loop while 
