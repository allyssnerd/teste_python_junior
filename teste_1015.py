#!/usr/bin/env python
# -- coding: utf-8 -- 

x_a, y_a = input().split()
x_b, y_b = input().split()

x_a = float(x_a)
y_a = float(y_a)
x_b = float(x_b)
y_b = float(y_b)

soma = ((x_b - x_a)**2 + (y_b - y_a)**2)**(1/2)

print('{:.4f}'.format(soma))