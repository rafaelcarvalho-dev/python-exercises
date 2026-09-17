acumulador = 0
contador = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        contador += 1
        acumulador += n
print(f'a soma de todos os {contador} valores solicitados é {acumulador}')