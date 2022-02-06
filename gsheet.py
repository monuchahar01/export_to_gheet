#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:21:56 2022

@author: monu
"""
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def export_to_gsheet():
    
    scope=['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file',
           'https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
    
    cred=ServiceAccountCredentials.from_json_keyfile_name('stocks.json',scope)
    client=gspread.authorize(cred)
    
    #sample=client.open('sample').sheet1
    
    #sample.update_cell(1,2,"monu")
    
    
    spreadsheet = client.open('sample')
    
    with open('main.csv', 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)
        

if __name__=="__main__":
    export_to_gsheet()        
