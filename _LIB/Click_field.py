# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:31:15 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""

from _Field import Field


class Click_field(Field):
    
    def execute_field(self, value):
            if (value[0] == "ID"):
                element_box = self._driver.find_element(self._By.ID, "{}".format(value[1]))
                element_box.click()