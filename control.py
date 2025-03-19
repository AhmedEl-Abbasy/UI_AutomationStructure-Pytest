# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 01:30:48 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""
import pytest
import os 



if __name__ == "__main__":
    print("""\033[33m
        \nThis is a simple structure that I used in automation scripts using the pytest framework.\n \033[0m""")
    
    
    pytest.main([r".\tests", "--tb=no",'-v', "-s","-m","test_1"])
    # pytest.main([r".\tests",'-v', "-s","-m","test_1"])

