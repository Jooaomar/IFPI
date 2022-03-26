r = float(input("Escreva o valor do Raio: "))
PI = 3.141592
c_circulo = 2*PI*r
a_circulo = PI*r**2
a_esfera = 4*PI*r**2
v_esfera = (4*PI*r**3)/3
print('Comprimento da circunferência: %1.6f'%(c_circulo))
print('Área do círculo: %1.6f'%(a_circulo))
print('Área da esfera: %1.6f'%(a_esfera))
print('Volume da esfera: %1.6f'%(v_esfera))
