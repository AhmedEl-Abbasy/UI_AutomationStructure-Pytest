# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 02:41:00 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""
from abc import ABC ,abstractmethod
from selenium.webdriver.common.by import By


class Field(ABC):
    _driver = 0
    _By = By
    
    @abstractmethod
    def execute_field(self, value):
        pass
    
    @staticmethod
    def set_driver(driver):
        Field._driver = driver
        


