# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:59:36 2020
Simulacoes para atingir a independencia financeira com um modelo
muito simples que considera uma inflacao fixa e um rendimento mensal fixo. 
Alem, disso o modelo assume que todo o rendimento mensal eh reinvestido. 
O que nao eh sempre possivel dado a vinculos de precos  e etc... 
Um plus para o modelo eh que o mesmo atualiza o valor Objetivo pela inflacao
mes a mes. 
@author: Sergio Novi, sergiolnovi@gmail.com
"""

class ModeloRendaMensal:
    def __init__(self, Inflacao=4.6, Rend=0.7, Aporte=1500,capital=0,obj=3000):
        # Inflacao (Percentagem ao Ano)
        self.Inflacao = 4.6; 
        # Rendimento Mensal Esperado (Percentagem ao Mes)
        self.Rend =  0.7;
        # Aporte Mensal (Em reais) 
        self.Aporte = [Aporte];
        # Capital Inicial
        self.capital = [capital]; 
        # Objetivo 
        self.obj = [obj];
        
    def TempoParaIndependenciaFinanceira(self):
        # Monthly income is calculated based on the invested capital
        RendaMensal = [0];
        capital = self.capital+self.Aporte;
        obj = self.obj;
        Aporte = self.Aporte;
        Meses=0;       

        while RendaMensal[-1]<obj[-1]:
    
            RendaMensal.append((self.Rend/100)*capital[-1]);
    
            obj.append((1 + (self.Inflacao/(12*100)))*obj[-1]);
            Aporte.append((1 + (self.Inflacao/(12*100)))*Aporte[-1]);
    
            capital.append(capital[-1] + RendaMensal[-1] + Aporte[-1]);
    
            Meses=Meses+1;
        return Meses,capital,RendaMensal,obj
    
    
    




 

