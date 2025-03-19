# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 01:14:24 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""
import pytest
import os , sys
sys.path.append(os.path.abspath(r"./_LIB"))

from selenium import webdriver
from _Field import Field

driver = 0

@pytest.fixture(scope="session",autouse=True)
def control_driver():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    Field.set_driver(driver)
    yield driver
    driver.quit()



@pytest.fixture(scope="function")
def browser():
    pass
    yield driver
    pass



@pytest.fixture(scope="function")
def page_functions():
    pass
    yield Execute_page
    pass


def Execute_page(page):
    for key,value in page.items():
        field = value[0]()
        field.execute_field(value[1:])



