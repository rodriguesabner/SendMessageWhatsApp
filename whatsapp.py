from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import socket

mensagem = 'Olá essa é uma mensagem automatizada de WhatsApp escrita pelo computador e enviada via Python. Projeto executado com sucesso!!'  # message
quantidade = 1  # quantidade de mensagens.
lista_numeros = [5511912345678, 5511912345678]  # numeros que receberão a mensagem


def element_presence(by, xpath, time):
    element_present = ec.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:
        # testa se a internet ta funcionando
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        is_connected()


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10)  # tempo para scanear o código (sync com o whatsapp mobile)


def send_whatsapp_msg(phone_no, text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to.alert
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
        txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global quantidade
        for x in range(quantidade):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("Número Inválido:" + str(phone_no))


for moblie_no in lista_numeros:
    try:
        send_whatsapp_msg(moblie_no, mensagem)

    except Exception as e:
        sleep(10)
        is_connected()
