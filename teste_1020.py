#!/usr/bin/env python
# -- coding: utf-8 -- 

ano = 365
mes = 30
dia = 1

input_dias = input()
input_dias = int(input_dias)

anos = input_dias/ano
meses = (input_dias%ano)/mes
dias = (input_dias%ano)%mes

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(int(anos), int(meses), int(dias)))