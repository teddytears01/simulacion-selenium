from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# CONFIGURACIÓN DEL DRIVER
service = Service("C:\\Users\\duart\\Desktop\\Driver\\msedgedriver.exe")

def iniciar_driver():
    driver = webdriver.Edge(service=service)
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    return driver

# FUNCIÓN REUTILIZABLE DE LOGIN
def login(driver, user, password):
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


# CASO 1: COMPRA COMPLETA

def test_caso1():
    driver = iniciar_driver()

    login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(items) > 0

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    assert "checkout-step-two" in driver.current_url

    driver.find_element(By.ID, "finish").click()

    mensaje = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you" in mensaje

    print("TC01 PASS")
    time.sleep(3)
    driver.quit()


# CASO 2: LOGIN INVÁLIDO

def test_caso2():
    driver = iniciar_driver()

    login(driver, "usuario_falso", "1234")

    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error

    print("TC02 PASS")
    time.sleep(3)
    driver.quit()


# CASO 3: AGREGAR PRODUCTOS

def test_caso3():
    driver = iniciar_driver()

    login(driver, "standard_user", "secret_sauce")

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(items) >= 2

    print("TC03 PASS")
    time.sleep(3)
    driver.quit()


# CASO 4: ELIMINAR PRODUCTOS

def test_caso4():
    driver = iniciar_driver()

    login(driver, "standard_user", "secret_sauce")

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(items) == 0

    print("TC04 PASS")
    time.sleep(3)
    driver.quit()


# CASO 5: CHECKOUT INCOMPLETO

def test_caso5():
    driver = iniciar_driver()

    login(driver, "standard_user", "secret_sauce")

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "continue").click()

    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Error" in error

    print("TC05 PASS")
    time.sleep(3)
    driver.quit()


# CASO 6: NAVEGACIÓN ABOUT

def test_caso6():
    driver = iniciar_driver()

    login(driver, "standard_user", "secret_sauce")

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "about_sidebar_link").click()

    assert "saucelabs" in driver.current_url.lower()

    print("TC06 PASS")
    time.sleep(3)
    driver.quit()


# ============================
# EJECUCIÓN (elige uno quitando el #)
# ============================

if __name__ == "__main__":
    # test_caso1()
    # test_caso2()
    # test_caso3()
    # test_caso4()
    # test_caso5()
    # test_caso6()