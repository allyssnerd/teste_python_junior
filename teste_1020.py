#!/usr/bin/env python
# -- coding: utf-8 -- 

ano = 365
mes = 30
dia = 1

input_dias = input('Informe sua idade em dias: ')
input_dias = int(input_dias)

anos = input_dias/ano
meses = (input_dias%ano)/mes
dias = (input_dias%ano)%mes

print('{} anos\n{} meses\n{} dias'.format(int(anos), int(meses), int(dias)))