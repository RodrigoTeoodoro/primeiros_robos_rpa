import time
import xlsxwriter
import chromedriver_binary

from selenium import webdriver
from datetime import datetime

livro = xlsxwriter.Workbook('bibliotecas.xlsx')
planilha = livro.add_worksheet()


web = webdriver.Chrome()
web.get('https://pypi.org/')
web.find_element_by_xpath('//*[@id="search"]').send_keys('selenium')
web.find_element_by_xpath('//*[@id="content"]/div[1]/div/form/button').click()

time.sleep(1)

bibliotecas = web.find_elements_by_css_selector('.package-snippet__name')

planilha.write(0, 0, 'Bibliotecas')

linha_de_escrita = 1
for biblioteca in bibliotecas:
    planilha.write(linha_de_escrita, 0, biblioteca.text)
    print(biblioteca.text)
    linha_de_escrita = linha_de_escrita + 1


descricoes = web.find_elements_by_css_selector('.package-snippet__description')
planilha.write(0, 1, 'Descrição')

linha_de_escrita = 1
for descricao in descricoes:
    planilha.write(linha_de_escrita, 1, descricao.text)
    print(descricao.text)
    linha_de_escrita = linha_de_escrita + 1

web.close()
livro.close()
