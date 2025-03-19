# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 01:59:39 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""

from _Field import Field


class InputText_field(Field):
    
    def execute_field(self, value):
            if (value[0] == "ID"):
                element_box=self._driver.find_element(self._By.ID, f"{value[1]}")
                element_box.clear()
                element_box.send_keys("{}".format(value[2]))
                
