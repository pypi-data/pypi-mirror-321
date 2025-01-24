from functools import wraps
import os
import time
from typing import Callable
from selenium.webdriver import Chrome
from Adlib.api import *
from Adlib.funcoes import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import inspect


def login_decorator(func):

    def loginFunctionPrototype(driver: Chrome, usuario: str, senha: str):
        pass


    def loginCaptchaFunctionPrototype(driver: Chrome, usuario: str, senha: str, 
                                      enumBanco: EnumBanco, enumProcesso: EnumProcesso) -> tuple[bool, str, str]:
        pass


    loginFunctionModel = inspect.signature(loginFunctionPrototype)
    loginCaptchFunctionModel = inspect.signature(loginCaptchaFunctionPrototype)

    def validateLoginFunction(func: Callable) -> bool:
        funcSignature = inspect.signature(func)
        if funcSignature not in [loginFunctionModel, loginCaptchFunctionModel]:
            raise TypeError(
                f"A função {func.__name__} não está no formato adequado!\
                \n{loginFunctionModel}\
                \n{loginCaptchFunctionModel}"
            )
        return True

    @wraps(func)
    def wrapper(driver: Chrome, usuario: str, senha: str, *args):
        isValidLoginFunction = validateLoginFunction(func)
        if isValidLoginFunction:
            try:
                return func(driver, usuario, senha, *args)
            except Exception as e:
                print(f"Erro ao realizar login: {func.__name__}")
                print(e)
    return wrapper


def captcha_decorator(loginFunc):
    @wraps(loginFunc)
    def wrapper(driver: Chrome, usuario: str, senha: str, enumBanco: EnumBanco, enumProcesso: EnumProcesso) -> tuple[bool, str, str]:
        while True:
            logou, imgPath, captcha = loginFunc(driver, usuario, senha, enumBanco, enumProcesso)

            if logou:
                timestamp = int(time.time())
                novo_nome = f"{timestamp}_{captcha}.png"
                novo_caminho = os.path.join(os.path.dirname(imgPath), novo_nome)

                os.rename(imgPath, novo_caminho)
                
                return logou
            
            driver.refresh()
        
    return wrapper



@login_decorator
def loginIBConsig(driver: Chrome, usuario: str, senha: str, captcha: str):
    
    driver.get('https://portal.icconsig.com.br/')
    sleep(10)

    iframe = esperarElemento(driver, '/html/body/cc-lib-dialog/div/div[1]/div[2]/div/app-auth-dialog/div/iframe')
    driver.switch_to.frame(iframe)

    esperarElemento(driver, '//*[@id="username"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="password"]').send_keys(senha + Keys.ENTER)
    
    sleep(10)


@login_decorator
def loginDigio(driver: Chrome, usuario: str, senha: str):

    driver.get("https://funcaoconsig.digio.com.br/FIMENU/Login/AC.UI.LOGIN.aspx")

    esperarElemento(driver, "//*[@id='EUsuario_CAMPO']").send_keys(usuario)
    esperarElemento(driver, "//*[@id='ESenha_CAMPO']").send_keys(senha)
    clickarElemento(driver, '//*[@id="lnkEntrar"]').click()
    clickarElemento(driver, '//*[@id="ctl00_ContentPlaceHolder1_DataListMenu_ctl00_LinkButton2"]').click()


@login_decorator
def loginBlip(driver: Chrome, usuario: str, senha: str):

    driver.get('https://takegarage-7ah6a.desk.blip.ai/')
    sleep(5)
    shadow_host = driver.find_element('css selector', '#email-input')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    
    shadow_root.find_element('class name', 'input__container__text').send_keys(usuario)
    driver.find_element('css selector', ".input__container__text").send_keys(senha + Keys.ENTER + Keys.ENTER)

    sleep(5)


@login_decorator
def loginFacta(driver: Chrome, usuario: str, senha: str):

    driver.get('https://desenv.facta.com.br/sistemaNovo/login.php')
    
    esperarElemento(driver, '//*[@id="login"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="senha"]').send_keys(senha)

    esperarElemento(driver,'//*[@id="btnLogin"]').click()

    sleep(5)


@login_decorator
def loginMargem(driver: Chrome, usuario: str, senha: str):
    driver.get('https://adpromotora.promobank.com.br/') 

    esperarElemento(driver, '//*[@id="inputUsuario"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="passField"]').send_keys(senha + Keys.ENTER)
    sleep(5)


@login_decorator
def loginBanrisul(driver: Chrome, usuario: str, senha: str):

    driver.get('https://desenv.banrisul.com.br/sistemaNovo/login.php')
 
    esperarElemento(driver, '//*[@id="usuario"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="senha"]').send_keys(senha)

    esperarElemento(driver,'//*[@id="btnLogin"]').click()
    sleep(5)


@login_decorator
def loginCashCard(driver: Chrome, usuario: str, senha: str):
    
    driver.get(f"http://18.217.139.90/WebAppBPOCartao/Login/ICLogin?ReturnUrl=%2FWebAppBPOCartao%2FPages%2FRelatorios%2FICRLProducaoAnalitico")
    
    esperarElemento(driver, '//*[@id="txtUsuario_CAMPO"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="txtSenha_CAMPO"]').send_keys(senha)

    esperarElemento(driver, '//*[@id="bbConfirmar"]').click()

    sleep(5)


@login_decorator
def loginVirtaus(driver: Chrome, usuario: str, senha: str):
    driver.get("https://app.fluigidentity.com/ui/login")
    sleep(5)

    esperarElemento(driver, '//*[@id="username"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="password"]').send_keys(senha + Keys.ENTER)
    sleep(10)


@login_decorator
def loginMaster(driver: Chrome, usuario: str, senha: str):
    
    driver.get('https://autenticacao.bancomaster.com.br/login')

    esperarElemento(driver, '//*[@id="mat-input-0"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="mat-input-1"]').send_keys(senha)
    clickarElemento(driver, '/html/body/app-root/app-login/div/div[2]/mat-card/mat-card-content/form/div[3]/button[2]').click()
    try:
        clickarElemento(driver, '//*[@id="mat-dialog-0"]/app-confirmacao-dialog/div/div[3]/div/app-botao-icon-v2[2]/button').click()
    except:
        pass


@login_decorator
@captcha_decorator
def loginBMG(driver: Chrome, usuario: str, senha: str, enumBanco: EnumBanco, enumProcesso: EnumProcesso) -> tuple[bool, str, str]:

    driver.get("https://www.bmgconsig.com.br/Index.do?method=prepare")

    esperarElemento(driver,'//*[@id="usuario"]').send_keys(usuario + Keys.ENTER)
    esperarElemento(driver, '//*[@id="j_password"]').send_keys(senha + Keys.ENTER)

    captchaElement = esperarElemento(driver, '/html/body/section[1]/div/div[1]/div/div/form/div[3]/iframe')
    imgFolder = r"C:\Users\dannilo.costa\Images\Captchas"

    imgPath = saveCaptchaImage(driver, captchaElement, imgFolder, enumBanco, enumProcesso)

    captcha = enviarCaptcha(None, None, imgPath, enumBanco, enumProcesso)
    
    esperarElemento(driver, '//*[@id="captcha"]').send_keys(captcha)

    return True, imgPath, captcha


if __name__=="__main__":

    driver = setupDriver(r"C:\Users\dannilo.costa\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")

    user, senha = getCredenciais(107)
    loginBMG(driver, user, senha, EnumBanco.BMG, EnumProcesso.CRIACAO)
    input("FECHAR????")
    input("FECHAR????")
    input("FECHAR????")
    input("FECHAR????")
    input("FECHAR????")