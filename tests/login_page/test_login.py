# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 01:33:56 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""

import os ,sys
import pytest

sys.path.append(os.path.abspath(r"./Pages_locators"))

from Login_page import Login_page as P


@pytest.mark.test_1
def test_trial(page_functions,browser):
    
    element ={
        "url"               : "https://trello.com/login",
        "Enter your email"  : "ahmed.elabbasy00@gmail.com",
        "Continue"          : True,        
        }
    
    page = P(element)
    page_functions(page.get_page_fields())
    
    assert "Log in" in browser.title, "Login page title is incorrect"
