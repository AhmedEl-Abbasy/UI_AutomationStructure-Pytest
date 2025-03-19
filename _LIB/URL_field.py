# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:29:14 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""

from _Field import Field


class URL_field(Field):
    
    def execute_field(self, value):
            if value[0] == "URL":
                self._driver.get("{}".format(value[2]))
                self._driver.implicitly_wait(10)
                

