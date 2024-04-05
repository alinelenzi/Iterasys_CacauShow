from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que entro no site Cacau Show')
def step_impl(context):
    context.driver = webdriver.Chrome();
    context.driver.maximize_window();
    context.driver.implicitly_wait(10);
    context.driver.get('https://www.cacaushow.com.br');

@when(u'preencho o campo de email {email}')
def step_impl(context, email):
    context.driver.find_element(By.CSS_SELECTOR, '.user-message').click();
    context.driver.find_element(By.ID, 'login-form-email').send_keys(email);
    context.driver.find_element(By.ID, 'login-btn-toggle').click();

@when(u' preencho o campo de email {email}')
def step_impl(context, email):
    context.driver.find_element(By.CSS_SELECTOR, '.user-message').click();
    context.driver.find_element(By.ID, 'login-form-email').send_keys(email);
    context.driver.find_element(By.ID, 'login-btn-toggle').click();

@then(u'recebo uma mensagem de erro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, '.custom-error-message').text == "Por favor inserir um endereço de e-mail válido"

@then(u'preencho o campo de senha {senha} e recebo uma {mensagem} de erro')
def step_impl(context, senha, mensagem):    
    context.driver.find_element(By.ID, 'login-form-password').send_keys(senha);
    context.driver.find_element(By.ID, 'login-btn-toggle').click();
    #validar a mensagem de texto
    context.driver.find_element(By.CSS_SELECTOR, '.custom-error-message').text == mensagem

@then(u'preencho o campo de senha  e recebo uma {mensagem} de erro')
def step_impl(context, senha, mensagem):    
    #não preencho a senha
    context.driver.find_element(By.ID, 'login-btn-toggle').click();
    #validar a mensagem de texto
    context.driver.find_element(By.CSS_SELECTOR, '.custom-error-message').text == mensagem
    
    #teardown/encerramento
    context.driver.quit()