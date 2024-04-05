from behave import given, when, then
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'entro no site Cacau Show e clico no link Entrar')
def step_impl(context):
    #setup/inicialização
    context.driver = webdriver.Chrome();
    context.driver.maximize_window();
    context.driver.implicitly_wait(10);
    context.driver.get('https://www.cacaushow.com.br/');

@when(u'preencho o campo entrar com email {email}')
def step_impl(context, email):
    context.driver.find_element(By.CSS_SELECTOR, '.user-message').click();
    context.driver.find_element(By.ID, "login-form-email").send_keys(email);
    context.driver.find_element(By.ID, "login-btn-toggle").click();

@then(u'sou direcionado para pagina')
def step_impl(context):
        context.driver.find_element(By.ID, 'registration-form-fname').send_keys('Daiane');
        context.driver.find_element(By.ID, 'registration-form-lname').send_keys('Rosângela Isabella Silva');
        context.driver.find_element(By.ID, 'registration-form-bdate').send_keys('19/03/1987');
        context.driver.find_element(By.ID, 'registration-form-gender').send_keys('Feminino');
        context.driver.find_element(By.ID, 'registration-form-cpf').send_keys('476.357.078-17');
        context.driver.find_element(By.ID, 'registration-form-phone').send_keys('(67)98531-5240');
        context.driver.find_element(By.ID, 'registration-form-email').send_keys('daiane_isabella_silva@multieventos.art.br');
        context.driver.find_element(By.ID, 'registration-form-email-confirm').send_keys('daiane_isabella_silva@multieventos.art.br');
        context.driver.find_element(By.ID, 'registration-form-password').send_keys('F3U6OCPSWC');
        context.driver.find_element(By.ID, 'registration-form-password-confirm').send_keys('F3U6OCPSWC');
        context.driver.find_element(By.ID, 'registration-form-cacaulover-accept').click();
        context.driver.find_element(By.CSS_SELECTOR, '.btn:nth-child(16)').click();
        context.driver.find_element(By.CSS_SELECTOR, '.col-12 .navbar-header .it_header--logo').click();
        context.driver.find_element(By.CSS_SELECTOR, '.col-xl-3 .it__login--options .popover').click();
        context.driver.find_element(By.LINK_TEXT, 'Sair').click();

