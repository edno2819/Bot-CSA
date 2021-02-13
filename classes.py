from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unicodedata
import re

class Site_csa():

    def iniciar_navegador(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get("http://www.csa-ma.com.br/")

    def atualizar_navegador(self):
        self.driver.refresh()
    
    def acessar_seguimentos(self,area):

        x=["home","solucoes","blog","treinamento","agende","depoimento","contato"]
        self.index_seguimentos=x.index(area)

        self.driver.find_element(By.XPATH, f'//*[@id="nav-item-{self.index_seguimentos+1577}"]/a').click()
          
    def carregar_all_news(self):
        if self.index_seguimentos==2:
            while True:
                
                if self.driver.find_element_by_class_name("load-more").text=="No more data":
                    break

                else:
                    self.driver.find_element_by_class_name("load-more-button").click()
                    time.sleep(5)

    def formulario(self,string_nome,string_telefone,string_empresa,string_email,string_menssagem,string_assunto="",string_web_site=""):
        if self.index_seguimentos==2:

            nome=self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/p[1]/span/input').send_keys(string_nome)   
            assunto=self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/p[2]/span/input').send_keys(string_assunto)
            telefone=self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/p[3]/span/input').send_keys(string_telefone)   
            empresa=self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/p[4]/span/input').send_keys(string_empresa)   
            email=self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/p[5]/span/input').send_keys(string_email)   
            web_site=self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/p[6]/span/input').send_keys(string_web_site)   
            menssagem=self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/p[8]/span/textarea').send_keys(string_menssagem)   
            enviar=self.driver.find_element(By.XPATH, '//*[@id="contact-page-button-blue"]').click()
            cont=0

            while True:
                if self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/div[2]').text=="Ocorreram erros de validação. Por favor confira os dados e envie novamente.":
                    return False
                elif self.driver.find_element(By.XPATH, '//*[@id="wpcf7-f2921-o1"]/form/div[2]').text=="Sua mensagem foi enviada com sucesso. Obrigado.":
                    return True
                else:
                    time.sleep(1)
                    cont+=1

                if cont>10:
                    return False

    def get_informacoes(self):
        if self.index_seguimentos==2:

            dados=[]
            noticias=BeautifulSoup(self.driver.page_source, "html.parser").find_all(class_="isotope-item post")

            for noticia in noticias:
                try:
                    url_img=noticia.img["src"]
                except:
                    url_img="Sem img"

                data=(noticia.find(class_="post-date").p).text
                data= ''.join(ch for ch in unicodedata.normalize('NFKD', data)  if not unicodedata.combining(ch))
                resumo=noticia.find(class_="post-excerpt").text
                resumo=''.join(ch for ch in unicodedata.normalize('NFKD', resumo)  if not unicodedata.combining(ch))
                titulo=noticia.find(class_="post-title").text
                titulo=''.join(ch for ch in unicodedata.normalize('NFKD', titulo)  if not unicodedata.combining(ch))

                dados.append({"titulo":re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]',"",titulo),"data":re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]',"",data),"resumo":re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]',"",resumo),"url":url_img.replace("\n","")})

            return dados

    def close_driver(self):
        self.driver.close()



