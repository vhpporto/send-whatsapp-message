from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "this is a test"
        self.numeros = ["xxxxxxxxxxx", "xxxxxxxxxxx", "xxxxxxxxxxx"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get("https://web.whatsapp.com/'")
        time.sleep(10)

        for numero in self.numeros:
            try:
                print(
                    f'https://web.whatsapp.com/send?phone={numero}&text={self.mensagem}')

                self.driver.get(
                    f'https://web.whatsapp.com/send?phone={numero}&text={self.mensagem}')
                time.sleep(5)
                botao_enviar = self.driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                time.sleep(2)
                botao_enviar.click()
                time.sleep(2)
            except Exception as e:
                print(str(e))


bot = WhatsappBot()
bot.EnviarMensagens()
