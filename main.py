# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

'''Instanciamos un objeto WebDriver de Firefox para controlar el navegador'''
browser = webdriver.Firefox()
'''Abrimos twitter en Firefox'''
browser.get("https://twitter.com/")

'''Introducimos el usuario y la contraseña en los campos adecuados'''
usuario = browser.find_element_by_name("session[username_or_email]")
usuario.send_keys("seleniumlopeta@gmail.com")

clave = browser.find_element_by_name("session[password]")
clave.send_keys("verificacioneslomas")

'''Pulsamos el boton de 'Inicio de Sesion' para iniciar sesion'''
browser.find_element_by_css_selector(".submit").click()

'''Escribimos el tweet en el campo de escritura de tweets'''
tweet = browser.find_element_by_id("tweet-box-home-timeline")
tweet.send_keys("I’m using Selenium!!!")

'''Buscamos el botón de publicar tweet y esperamos a que sea visible para después pulsarlo '''
post_tweet = browser.find_element_by_class_name("tweet-action")
wait = WebDriverWait(browser, 20).until(ec.visibility_of_element_located((By.CLASS_NAME, "tweet-action")));
post_tweet.click()

'''Cerramos el navegador'''
browser.close()
