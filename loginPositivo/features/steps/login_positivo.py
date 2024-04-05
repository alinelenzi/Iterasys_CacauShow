from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Cacau Show')
def step_impl(context):
    context.driver = webdriver.Chrome();
    context.driver.maximize_window();
    context.driver.implicitly_wait(10);
    context.driver.get('https://www.cacaushow.com.br');

@when(u'preencho o campo do email {email}')
def step_impl(context, email):
    context.driver.find_element(By.CSS_SELECTOR, '.user-message').click();
    context.driver.find_element(By.ID, 'login-form-email').send_keys(email);
    context.driver.find_element(By.ID, 'login-btn-toggle').click();

@then(u'sou direcionado para pagina Entrar')
def step_impl(context):
    context.driver.find_element(By.ID, 'login-form-password').send_keys('YIFZ5mBRxB');
    context.driver.find_element(By.ID, 'login-btn-toggle').click();
    context.driver.find_element(By.CSS_SELECTOR,'.col-12 .navbar-header .it_header--logo').click();
    context.driver.find_element(By.CSS_SELECTOR, '.col-xl-3 .it__login--options .popover').click();
    context.driver.find_element(By.LINK_TEXT, 'Sair').click();