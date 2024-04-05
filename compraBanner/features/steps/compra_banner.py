from behave import given, when, then
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'entro no site Cacau Show')
def step_impl(context):
    context.driver = webdriver.Chrome();
    context.driver.maximize_window();
    context.driver.implicitly_wait(10);
    context.driver.get('https://www.cacaushow.com.br')

@when(u'preencho o campo com email {email}')
def step_impl(context, email):
    context.driver.find_element(By.CSS_SELECTOR, '.user-message').click();
    context.driver.find_element(By.ID, 'login-form-email').send_keys('sergio_gustavo_martins@athos.srv.br');
    context.driver.find_element(By.ID, 'login-btn-toggle').click();
    context.driver.find_element(By.ID, 'login-form-password').send_keys('YIFZ5mBRxB');
    context.driver.find_element(By.ID, 'login-btn-toggle').click();



@then(u'sou direcionado para pagina Entrar')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.top .form-control').send_keys('ENFEITE HARRY POTTER 120G');
    context.driver.find_element(By.CSS_SELECTOR, '.swatch-circle').click();
    assert context.driver.find_element(By.CSS_SELECTOR, '.product-name').text == 'ENFEITE HARRY POTTER 120G';
    assert context.driver.find_element(By.CSS_SELECTOR, '.it__shelf__discountPrice').text == 'R$79.90';
    assert context.driver.find_element(By.ID, 'quantity-null').text == '1';
    context.driver.find_element(By.CSS_SELECTOR, '.add-to-cart.btn.btn-primary.it_product__tocart__btn').click();
    assert context.driver.find_element(By.CSS_SELECTOR, '.text-right.shipping-cost').text == 'R$16.00';
    assert context.driver.find_element(By.CSS_SELECTOR, '.text-right.grand-total').text == 'R$95.90';
    context.driver.find_element(By.CSS_SELECTOR, '.mb-sm-3.d-flex').click();
    context.driver.find_element(By.CSS_SELECTOR, '.btn.btn-continuar.js-zipcode-modal').click();
    context.driver.find_element(By.CSS_SELECTOR, 'name=phone').send_kys('casa');
    context.driver.find_element(By.CSS_SELECTOR, 'name=firstName').send_keys('Jose');
    context.driver.find_element(By.CSS_SELECTOR, 'name=lastName2').send_keys('Antonio');
    context.driver.find_element(By.CSS_SELECTOR, 'name=phone').send_keys('+55 (27) 98877-0088');
    context.driver.find_element(By.CSS_SELECTOR, '.js-step1-newAddress:nth-child(1)').click();
    context.driver.find_element(By.CSS_SELECTOR, '.js-nextStep1:nth-child(1)').click();
    context.driver.find_element(By.CSS_SELECTOR, '.pix-tab').click();
    context.driver.find_element(By.CSS_SELECTOR, '.btn .btn-continuar .btn-block .next-summary .js-finish-order-pix').click();

