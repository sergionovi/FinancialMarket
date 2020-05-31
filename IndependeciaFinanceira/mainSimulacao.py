# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:59:36 2020

@author: Sergio Novi
"""



### 1-Parametros do Modelo

# Inflacao (Percentagem ao Ano)
Inflacao = 4.6; 
# Rendimento Mensal Esperado (Percentagem ao Mes)
Rend =  0.7;
# Aporte Mensal (Em reais) 
Aporte = 1500;
# Capital Inicial
capital = 0; 
# Objetivo 
obj = 5000;


RendaMensal = [0]

capital = capital+Aporte;

Meses=0;

while RendaMensal[-1]<obj:
    
    RendaMensal.append((Rend/100)*capital);
    obj = (1 + (Inflacao/(12*100)))*obj;
    Aporte = (1 + (Inflacao/(12*100)))*Aporte;
    
    capital = capital + RendaMensal[-1] + Aporte;
    
    
    
    Meses=Meses+1;
    
    
print('Anos: ' + str(round(Meses/12)) + ' Objetivo: ' + str(round(obj))
+ ' Aporte Mensal: ' + str(round(Aporte))) 
    
    





 

