#!/usr/bin/env python
# -- coding: utf-8 -- 

x_a, y_a = input('Informe o valor de x1 e y1: ').split()
x_b, y_b = input('Informe o valor de x2 e y2: ').split()

x_a = float(x_a)
y_a = float(y_a)
x_b = float(x_b)
y_b = float(y_b)

soma = ((x_b - x_a)**2 + (y_b - y_a)**2)**(1/2)

print('O resultado da raiz quadrada é {:.4f}'.format(soma))