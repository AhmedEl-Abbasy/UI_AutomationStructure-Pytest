# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 16:17:13 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""
import os , sys
sys.path.append(os.path.abspath(r"../_LIB"))

from _Page import Page
import _ExecuteFields as F
class Login_page(Page):
    
    _page_fields={
        "url"               : [F.URL_field       , "URL", ""             ],
        "Enter your email"  : [F.InputText_field , "ID" , "username"     ],
        "Continue"          : [F.Click_field     , "ID" , "login-submit" ],        
        }
    def __init__(self,data_received):
        self.update_fields(data_received)
    