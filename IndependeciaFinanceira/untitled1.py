# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:52:51 2020

@author: Sergio Novi
"""
import matplotlib.pyplot as plt
import mainSimulacao as ms

teste = ms.ModeloRendaMensal()

[Meses,capital,RendaMensal,obj]=teste.TempoParaIndependenciaFinanceira()

plt.subplot(1,2,1)
plt.plot(capital,'-r')

plt.subplot(1,2,2)
plt.plot(RendaMensal,'-b')
plt.plot(obj,'-g')
plt.legend(['Renda Passiva Mensal', 'Objetivo'])

