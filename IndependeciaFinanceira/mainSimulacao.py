# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:52:51 2020

@author: Sergio Novi
"""
import matplotlib.pyplot as plt
import FII_models as FII

teste = FII.ModeloRendaMensal()

[Meses,capital,RendaMensal,obj]=teste.TempoParaIndependenciaFinanceira()

plt.subplot(1,2,1)
plt.plot(capital,'-r')
plt.legend(['Capital Investido'])
plt.ylabel('Montante (R$)')
plt.xlabel('Tempo (Meses)')

plt.subplot(1,2,2)
plt.plot(RendaMensal,'-b')
plt.plot(obj,'-g')
plt.legend(['Renda Passiva Mensal', 'Objetivo'])
plt.ylabel('Montante (R$)')
plt.xlabel('Tempo (Meses)')
