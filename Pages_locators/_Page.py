# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 16:31:51 2025
File name: 

@author:   Ahmed El-Abbasy
@contact:  https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""

from abc import ABC 

class Page(ABC):
    _page_fields={}
    
    def Print_name(self):
        print("Ahmed ElAbbasy")
    
    def update_fields(self, data_received):
        if not isinstance(data_received, dict):
            print("this element not dictionary type")
            return
        for key in data_received:
            if key in self._page_fields:
                self._page_fields[key].append(data_received[key])
    
    def get_page_fields(self):
        used_fields = {}
        
        for key in self._page_fields:
            if isinstance(self._page_fields[key] ,list) and len(self._page_fields[key]) >3:
                used_fields[key] = self._page_fields[key]
        return used_fields
    
    @classmethod
    def get_fields_name(cls):
        return list(cls._page_fields.keys())




