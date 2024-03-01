#Importação do sync_playwright da biblioteca playwright
from playwright.sync_api import sync_playwright

#Importando a biblioteca time para visualizar a página melhor
import time

#Cria a lista com as labels das moedas que serâo convertidas
labels = ['Dólar', 'Euro', 'Libra Esterlina', 'Iene']

#Pergunta o valor que será convertido
valor = input('Digite o valor a ser convertido (INSIRA OS CENTAVOS SEM VÍRGULA NO FINAL): R$')

#Criando o navegador
with sync_playwright() as p:
    navegador = p.chromium.launch()

    #Criando a página
    pagina = navegador.new_page()

    #Indica qual página deve ser acessada
    pagina.goto("https://www.idinheiro.com.br/calculadoras/calculadora-conversor-de-moeda/")
    time.sleep(1)

    #Insere o valor a ser convertido
    pagina.fill('xpath=//*[@id="value_convert"]', valor)
    pagina.wait_for_load_state("load")

    #Seleciona o Real Brasileiro para a conversão
    pagina.query_selector('xpath=//*[@id="currency_for_convertion"]').select_option(label='Real Brasileiro')

    for label in labels:

        #Seleciona as moedas que serão convertidas
        pagina.query_selector('xpath=//*[@id="currency_converted"]').select_option(label=label)
        pagina.wait_for_load_state("load")

        #Clica no botão para calcular
        pagina.locator('xpath=//*[@id="__next"]/div/div/div[3]/div/div[1]/article/div/div[2]/form/div/div[2]/button[2]').click()
        pagina.wait_for_load_state("load")

        #Pega o texto com a cotação e o armazena em uma variavel
        valor_convertido = pagina.text_content('xpath=//*[@id="__next"]/div/div/div[3]/div/div[1]/article/div/div[2]/form/div/div[3]/div[1]/div/div/p[1]')
        pagina.wait_for_load_state("load")

        #Printa o texto no console
        print(valor_convertido)

    #Fecha o browser
    navegador.close()
